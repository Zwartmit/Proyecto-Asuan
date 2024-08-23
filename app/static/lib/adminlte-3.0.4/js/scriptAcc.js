document.addEventListener('DOMContentLoaded', function() {
    

    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode');
        const isDarkMode = document.body.classList.contains('dark-mode');
        localStorage.setItem('dark-mode', isDarkMode);
    }

    if (localStorage.getItem('dark-mode') === 'true') {
        document.body.classList.add('dark-mode');
    }

    function resetAccessibility() {
        document.body.style.fontSize = '';
        document.body.classList.remove('dark-mode');
    }
    
    window.toggleDarkMode = toggleDarkMode;
});

document.addEventListener('DOMContentLoaded', function () {
    const productRows = document.getElementById('product-rows');
    const subtotalElement = document.getElementById('subtotal');
    const totalVentaField = document.getElementById('total_venta');

    function addProductRow() {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>
                <input class="product-id product-select" style="width: 100%;" required />
            </td>
            <td><input type="number" class="product-quantity" min="1" required></td>
            <td><input type="number" class="product-price" min="0" step="0.01" required readonly></td>
            <td><i type="button" class="delete-row fas fa-trash-alt" style="color: #04644B; font-size: 25px;"
                onmouseover="this.style.color='#ff0000';"
                onmouseout="this.style.color='#04644B';"></i></td>
            <td><span class="product-total">$0.00</span></td>
        `;
    
        $(row.querySelector('.product-select')).select2({
            placeholder: 'Seleccione un producto',
            ajax: {
                url: '/app/venta/productos_api/',
                dataType: 'json',
                delay: 250,
                data: function (params) {
                    return {
                        term: params.term
                    };
                },
                processResults: function (data) {
                    return {
                        results: data.map(producto => ({
                            id: producto.id,
                            text: producto.producto,
                            valor: producto.valor
                        }))
                    };
                },
                cache: true
            }
        }).on('select2:select', function (e) {
            const data = e.params.data;
            const priceInput = row.querySelector('.product-price');
            priceInput.value = data.valor || 0;
            $(this).data('select2').$container.find('.select2-selection__placeholder').text(data.text);
            validateInputs();
        });

        productRows.appendChild(row);

        row.querySelector('.product-quantity').addEventListener('input', validateInputs);
        row.querySelector('.product-price').addEventListener('input', validateInputs);
        row.querySelector('.delete-row').addEventListener('click', function () {
            row.remove();
            validateInputs();
        });

        validateInputs();
    }

    function validateInputs() {
        let isValid = true;
        let ids = new Set();
        let subtotal = 0;

        document.querySelectorAll('#product-rows tr').forEach(row => {
            const select = $(row.querySelector('.product-select')).val();
            const quantity = row.querySelector('.product-quantity').value;
            const price = row.querySelector('.product-price').value;

            if (ids.has(select)) {
                $(row.querySelector('.product-select')).next().addClass('error');
                isValid = false;
            } else {
                $(row.querySelector('.product-select')).next().removeClass('error');
                ids.add(select);
            }

            if (quantity <= 0) {
                row.querySelector('.product-quantity').classList.add('error');
                isValid = false;
            } else {
                row.querySelector('.product-quantity').classList.remove('error');
            }

            if (price < 0) {
                row.querySelector('.product-price').classList.add('error');
                isValid = false;
            } else {
                row.querySelector('.product-price').classList.remove('error');
            }

            const total = (quantity * price).toFixed(2);
            row.querySelector('.product-total').textContent = `$${total}`;

            subtotal += parseFloat(total);
        });

        subtotalElement.textContent = `$${subtotal.toFixed(2)}`;
        if (totalVentaField) {
            totalVentaField.value = subtotal.toFixed(2);
        }

        return isValid;
    }

    function printInvoice() {
        if (validateInputs()) {
            window.print();
        } else {
            alert('Por favor, corrija los errores antes de imprimir la factura.');
        }
    }

    function prepareForm() {
        const detallesVenta = [];
        document.querySelectorAll('#product-rows tr').forEach(row => {
            const idProducto = $(row.querySelector('.product-select')).val();
            const cantidadProducto = row.querySelector('.product-quantity').value;
            const subtotalVenta = row.querySelector('.product-total').textContent.replace('$', '').trim();
    
            detallesVenta.push({
                id_producto: idProducto,
                cantidad_producto: cantidadProducto,
                subtotal_venta: parseFloat(subtotalVenta.replace('$', '')) || 0
            });
        });
        
        const detallesVentaJSON = JSON.stringify(detallesVenta);
        document.getElementById('detalles_venta').value = JSON.stringify(detallesVenta);

        console.log("Detalles de Venta JSON:", detallesVentaJSON);
    }
    
    document.querySelector('form').addEventListener('submit', prepareForm);

    productRows.addEventListener('input', validateInputs);

    addProductRow();

    window.addProductRow = addProductRow;
    window.printInvoice = printInvoice;
});