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
    const dineroRecibidoInput = document.getElementById('dinero_recibido');
    const cambioElement = document.getElementById('cambio');
    let validationTimeout = null;

        function addProductRow() {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td class="product-column">
                    <input class="product-id product-select" style="width: 100%;" required />
                </td>
                <td class="quantity-column"><input type="number" class="product-quantity" min="1" required></td>
                <td class="price-column"><input type="number" class="product-price" min="0" step="0.01" required readonly></td>
                <td class="stock-column"><span class="product-stock">0</span></td>
                <td class="delete-column">
                    <i type="button" class="delete-row fas fa-trash-alt" style="color: #04644B; font-size: 25px;"
                        onmouseover="this.style.color='#ff0000';"
                        onmouseout="this.style.color='#04644B';"></i>
                </td>
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
                                valor: producto.valor,
                                cantidad: producto.cantidad
                            }))
                        };
                    },
                    cache: true
                }
            }).on('select2:select', function (e) {
                const data = e.params.data;
                const priceInput = row.querySelector('.product-price');
                const stockSpan = row.querySelector('.product-stock');
                const quantityInput = row.querySelector('.product-quantity');
                
                priceInput.value = data.valor || 0;
                stockSpan.textContent = data.cantidad || 0;
                quantityInput.max = data.cantidad || 0;
                quantityInput.value = 1; 

                $(this).data('select2').$container.find('.select2-selection__placeholder').text(data.text);

                validateInputs();
            });

            productRows.appendChild(row);

            row.querySelector('.product-quantity').addEventListener('input', function() {
                clearTimeout(validationTimeout);
                validationTimeout = setTimeout(validateInputs, 500);
            });
            row.querySelector('.product-price').addEventListener('input', validateInputs);
            row.querySelector('.delete-row').addEventListener('click', function () {
                if (window.confirm('¿Estás seguro de que quieres eliminar esta fila?')) {
                    row.remove();
                    validateInputs();
                }
            });

            validateInputs();
        }

    function validateInputs() {
        let isValid = true;
        let ids = new Set();
        let subtotal = 0;
        let duplicateError = false;
    
        document.querySelectorAll('#product-rows tr').forEach(row => {
            const select = $(row.querySelector('.product-select')).val();
            const quantityInput = row.querySelector('.product-quantity');
            const priceInput = row.querySelector('.product-price');
            const stockSpan = row.querySelector('.product-stock');
    
            const quantity = Number(quantityInput.value);
            const price = Number(priceInput.value);
            const maxQuantity = Number(quantityInput.max);
    
            if (ids.has(select)) {
                $(row.querySelector('.product-select')).next().addClass('error');
                isValid = false;
                duplicateError = true;
            } else {
                $(row.querySelector('.product-select')).next().removeClass('error');
                ids.add(select);
            }
    
            if (quantity <= 0 || quantity > maxQuantity) {
                quantityInput.classList.add('error');
                if (quantity > maxQuantity) {
                    Swal.fire({
                        title: 'Advertencia!',
                        text: `La cantidad ingresada (${quantity}) supera el stock disponible (${maxQuantity}).`,
                        icon: 'warning',
                    });
                }
                isValid = false;
            } else {
                quantityInput.classList.remove('error');
            }
    
            if (price < 0) {
                priceInput.classList.add('error');
                isValid = false;
            } else {
                priceInput.classList.remove('error');
            }
    
            const total = (quantity * price).toFixed(2);
            row.querySelector('.product-total').textContent = `$${total}`;
    
            subtotal += parseFloat(total);
        });
    
        subtotalElement.textContent = `$${subtotal.toFixed(2)}`;
        if (totalVentaField) {
            totalVentaField.value = subtotal.toFixed(2);
        }
    
        if (duplicateError) {
            Swal.fire({
                title: 'Error!',
                text: 'No se pueden guardar productos duplicados.',
                icon: 'error',
            });
        }
    
        return isValid && !duplicateError;
    }

    function calculateChange() {
        const dineroRecibido = parseFloat(dineroRecibidoInput.value) || 0;
        const subtotal = parseFloat(subtotalElement.textContent.replace('$', '')) || 0;
        const cambio = dineroRecibido - subtotal;

            cambioElement.value = cambio.toFixed(2);
        
    }

    function prepareForm(event) {
        if (!validateInputs()) {
            event.preventDefault();
            return;
        }
    
        const dineroRecibido = parseFloat(dineroRecibidoInput.value) || 0;
        const subtotal = parseFloat(subtotalElement.textContent.replace('$', '')) || 0;
    
        if (dineroRecibido < subtotal) {
            event.preventDefault();
            Swal.fire({
                title: 'Error!',
                text: 'El dinero recibido no puede ser menor al total de la venta.',
                icon: 'error',
            });
            return;
        }
    
        const detallesVenta = [];
        let productosLista = '';
    
        document.querySelectorAll('#product-rows tr').forEach(row => {
            const idProducto = $(row.querySelector('.product-select')).val();
            const productoText = $(row.querySelector('.product-select')).text();
            const cantidadProducto = row.querySelector('.product-quantity').value;
            const subtotalVenta = row.querySelector('.product-total').textContent.replace('$', '').trim();
    
            detallesVenta.push({
                id_producto: idProducto,
                cantidad_producto: cantidadProducto,
                subtotal_venta: parseFloat(subtotalVenta.replace('$', '')) || 0
            });
    
            productosLista += `<li>${productoText} - Cantidad: ${cantidadProducto} - Subtotal: $${subtotalVenta}</li>`;
        });
    
        const detallesVentaJSON = JSON.stringify(detallesVenta);
        document.getElementById('detalles_venta').value = detallesVentaJSON;
    
        Swal.fire({
            title: 'Venta Generada',
            html: `<ul>${productosLista}</ul>`,
            icon: 'info',
            showCancelButton: true,
            confirmButtonText: 'Confirmar',
            cancelButtonText: 'Cancelar',
            reverseButtons: true
        }).then((result) => {
            if (result.isConfirmed) {
                document.querySelector('form').submit();
            }
        });
    
        console.log("Detalles de Venta JSON:", detallesVentaJSON);
    }
    
    dineroRecibidoInput.addEventListener('input', calculateChange);
    
    document.querySelector('form').addEventListener('submit', prepareForm);

    productRows.addEventListener('input', validateInputs);

    addProductRow();

    window.addProductRow = addProductRow;
});

document.addEventListener('DOMContentLoaded', function () {
    $(document).ready(function () {
        $('.client-select').select2({
            placeholder: 'Buscar cliente',
            ajax: {
                url: '/app/venta/clientes_api/', 
                dataType: 'json',
                delay: 250,
                data: function (params) {
                    return {
                        term: params.term
                    };
                },
                processResults: function (data) {
                    return {
                        results: data.map(cliente => ({
                            id: cliente.id,
                            text: `${cliente.tipo_documento}: ${cliente.numero_documento} - ${cliente.nombre}`,
                            nombre: cliente.nombre,
                            tipo_documento: cliente.tipo_documento,
                            numero_documento: cliente.numero_documento,
                            email: cliente.email,
                            pais_telefono: cliente.pais_telefono,
                            telefono: cliente.telefono
                        }))
                    };
                },
                cache: true
            }
        }).on('select2:select', function (e) {
            const data = e.params.data;
            console.log('Cliente seleccionado:', data);

            document.getElementById('client-name').value = data.nombre;
            document.getElementById('client-document_type').value = data.tipo_documento;
            document.getElementById('client-document_number').value = data.numero_documento;
            document.getElementById('client-email').value = data.email;
            document.getElementById('client-phone_prefix').value = data.pais_telefono;
            document.getElementById('client-phone_number').value = data.telefono;
        });
    });
    
    document.getElementById('save-client').addEventListener('click', function () {
        const clientForm = document.getElementById('clienteForm');
        const formData = new FormData(clientForm);

        fetch('/app/cliente/crear/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Actualiza la lista de clientes en el formulario principal
                const selectElement = document.querySelector('.product-select');
                const newOption = new Option(data.client_name, data.client_id, true, true);
                selectElement.add(newOption, undefined);
                $(selectElement).trigger('change');
                
                // Cierra el modal
                $('#modal').modal('hide');
                
                // Limpia el formulario del modal
                clientForm.reset();
                
                Swal.fire({
                    title: 'Cliente guardado',
                    text: 'El cliente ha sido guardado exitosamente.',
                    icon: 'success'
                });
            } else {
                Swal.fire({
                    title: 'Error!',
                    text: data.error_message,
                    icon: 'error'
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire({
                title: 'Error!',
                text: 'Hubo un problema al guardar el cliente.',
                icon: 'error'
            });
        });
    });
});

