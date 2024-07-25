from dataclasses import fields
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from django import forms
from django.forms import *
from app.models import *

class CategoriaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["categoria"].widget.attrs["autofocus"] = True

    class Meta:
        model = Categoria
        fields = "__all__"
        widgets = {
            "categoria": TextInput(
                attrs={
                    "placeholder": "Nombre de la categoria",
                }
            )
        }

class MarcaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["marca"].widget.attrs["autofocus"] = True

    class Meta:
        model = Marca
        fields = "__all__"
        widgets = {
            "marca": TextInput(
                attrs={
                    "placeholder": "Nombre de la marca",
                }
            )
        }

class PresentacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["presentacion"].widget.attrs["autofocus"] = True

    class Meta:
        model = Presentacion
        fields = "__all__"
        widgets = {
            "presentacion": TextInput(
                attrs={
                    "placeholder": "Nombre de la presentacion",
                }
            )
        }

class ProductoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["producto"].widget.attrs["autofocus"] = True

    class Meta:
        model = Producto
        fields = "__all__"
        widgets = {
            "producto": TextInput(
                attrs={
                    "placeholder": "Nombre del producto",
                }
            ),
            "cantidad": NumberInput(
                attrs={
                    "placeholder": "Cantidad a registrar",
                }
            ),
            "valor": NumberInput(
                attrs={
                    "placeholder": "Valor del producto",
                }
            ),
            "estado": Select(
                choices=[(True, "Activo"), (False, "Inactivo")],
                attrs={
                    "placeholder": "Estado del producto",
                },
            )
        }

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True

    def validar_num_doc_rep(self):
        numero_documento = self.cleaned_data.get("numero_documento")
        if Cliente.objects.filter(numero_documento=numero_documento).exists():
            raise ValidationError("Ya hay un cliente registrado con este número de documento.")
        return numero_documento
            
    def validar_email_rep(self):
        email = self.cleaned_data.get("email")
        if Cliente.objects.filter(email=email).exists():
            raise ValidationError("Ya hay un cliente registrado con este email.")
        return email
    
    class Meta:
        model = Cliente
        fields = "__all__"
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "Nombre del cliente",
                }
            ),
            "tipo_documento": Select(
                attrs={
                    "placeholder": "Tipo de documento",
                }
            ),
            "numero_documento": NumberInput(
                attrs={
                    "placeholder": "Número de documento",
                }
            ),
            "email": EmailInput(
                attrs={
                    "placeholder": "Email",
                }
            ),
            "telefono": NumberInput(
                attrs={
                    "placeholder": "Teléfono",
                }
            )
        }

class MeseroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True
            
    class Meta:
        model = Mesero
        fields = "__all__"
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "Nombre del mesero",
                }
            ),
            "tipo_documento": Select(
                attrs={
                    "placeholder": "Tipo de documento",
                }
            ),
            "numero_documento": NumberInput(
                attrs={
                    "placeholder": "Número de documento",
                }
            ),
            "email": EmailInput(
                attrs={
                    
                    "placeholder": "Email",
                }
            ),
            "telefono": NumberInput(
                attrs={
                    "placeholder": "Teléfono",
                }
            )
        }

class PlatoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["plato"].widget.attrs["autofocus"] = True

    class Meta:
        model = Plato
        fields = "__all__"
        widgets = {
            "plato": TextInput(
                attrs={
                    "placeholder": "Nombre del plato",
                }
            ),
            "descripcion": Textarea(
                attrs={
                    "placeholder": "Descripción del plato",
                }
            ),
            "valor": NumberInput(
                attrs={
                    "placeholder": "Valor del plato",
                }
            ),
            "estado": Select(
                choices=[(True, "Activo"), (False, "Inactivo")],
                attrs={
                    "placeholder": "Estado del plato",
                },
            )
        }

class CuentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cantidad"].widget.attrs["autofocus"] = True

    class Meta:
        model = Cuenta
        fields = "__all__"
        widgets = {
            "cantidad": NumberInput(
                attrs={
                    "placeholder": "Cantidad a registrar",
                }
            ),
            "subtotal": NumberInput(
                attrs={
                    "placeholder": "Subtotal",
                }
            ),
            "estado": Select(
                choices=[(True, "Activo"), (False, "Inactivo")],
                attrs={
                    "placeholder": "Estado del producto",
                },
            )
        }

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, Select, NumberInput, EmailInput, PasswordInput
from app.models import Administrador

class AdministradorForm(ModelForm):
    username = forms.CharField(label="Username", max_length=150)
    email = forms.EmailField(label="Email", max_length=150)
    password = forms.CharField(label="Password", widget=PasswordInput)
    conf_password = forms.CharField(label="Confirm Password", widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("conf_password")

        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        
        if not password2:
            raise ValidationError("Necesitas validar tu contraseña")
        
        if password1 != password2:
            raise ValidationError("Las contraseñas no coinciden")
        
        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if User.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        administrador = super().save(commit=False)
        administrador.user = user
        if commit:
            administrador.save()
        return administrador

    class Meta:
        model = Administrador
        fields = ["username", "email", "nombre", "tipo_documento", "numero_documento", "telefono", "password", "conf_password"]
        widgets = {
            "nombre": TextInput(attrs={"placeholder": "Nombre del administrador"}),
            "tipo_documento": Select(attrs={"placeholder": "Tipo de documento"}),
            "numero_documento": NumberInput(attrs={"min": 8, "placeholder": "Número de documento"}),
            "telefono": NumberInput(attrs={"min": 1, "placeholder": "Teléfono"}),
            "password": PasswordInput(attrs={"min": 1, "placeholder": "Contraseña"}),
            "conf_password": PasswordInput(attrs={"min": 1, "placeholder": "Confirme su contraseña"})
        }




class OperadorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs["autofocus"] = True

    class Meta:
        model = Operador
        fields = "__all__"
        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "Nombre del operador",
                }
            ),
            "tipo_documento": Select(
                attrs={
                    "placeholder": "Tipo de documento",
                }
            ),
            "numero_documento": NumberInput(
                attrs={
                    "min": 8,
                    "placeholder": "Número de documento",
                }
            ),
            "email": EmailInput(
                attrs={
                    "placeholder": "Email",
                }
            ),
            "telefono": NumberInput(
                attrs={
                    "min": 1,
                    "placeholder": "Teléfono",
                }
            )
        }
 
class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cantidad_producto"].widget.attrs["autofocus"] = True

    class Meta:
        model = Venta
        fields = "__all__"
        widgets = {
            "cantidad_producto": NumberInput(
                attrs={
                    "placeholder": "Cantidad del producto",
                }
            ),
            "total_venta": NumberInput(
                attrs={
                    "placeholder": "Total",
                }
            ),
            "total_venta_iva": NumberInput(
                attrs={
                    "placeholder": "Total IVA",
                }
            ),
            "metodo_pago": Select(
                attrs={
                    "placeholder": "Metodo de pago",
                }
            ),
            "fecha_venta": DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "Fecha de la venta",
                }
            )
        }
        
class FacturaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha_emision_factura"].widget.attrs["autofocus"] = True

    class Meta:
        model = Venta
        fields = "__all__"
        widgets = {
            "fecha_emision_factura": DateInput(
                attrs={
                    "type": "date",
                    "placeholder": "Fecha de la venta",
                }
            )
        }