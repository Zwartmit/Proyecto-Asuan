from dataclasses import fields
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django_select2.forms import Select2Widget
from django import forms
from django.forms import *
from app.models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Select, NumberInput, EmailInput, PasswordInput
from app.models import Administrador
from app.models import Operador

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

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, NumberInput, Select
from app.models import Administrador

class AdministradorForm(ModelForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=TextInput(attrs={"placeholder": "Nombre de usuario"})
    )
    email = forms.EmailField(
        label="Email",
        max_length=150,
        widget=EmailInput(attrs={"placeholder": "Correo electrónico"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=PasswordInput(attrs={"placeholder": "Contraseña"}),
        required=False  
    )
    conf_password = forms.CharField(
        label="Confirmar contraseña",
        widget=PasswordInput(attrs={"placeholder": "Confirmar contraseña"}),
        required=False  
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email
        self.fields["username"].widget.attrs["autofocus"] = True

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("conf_password")
    
        errors = {}

        if User.objects.filter(username=username).exclude(pk=self.instance.user.pk if self.instance and self.instance.pk else None).exists():
            errors['username'] = "Este nombre de usuario ya está en uso."
        
        if User.objects.filter(email=email).exclude(pk=self.instance.user.pk if self.instance and self.instance.pk else None).exists():
            errors['email'] = "Este correo electrónico ya está en uso."
        
        if password1 or password2:
            if password1 != password2:
                errors['password'] = "Las contraseñas no coinciden."
            if not password1:
                errors['password'] = "La contraseña es obligatoria para guardar los cambios."
    
        if errors:
            raise ValidationError(errors)
    
        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if self.instance.pk:
            user = self.instance.user
            if username and user.username != username:
                user.username = username
            if email and user.email != email:
                user.email = email
            if password:
                user.set_password(password)
            user.save()
        else:
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



# -----------------------------------------------------------------------------------------------

class OperadorForm(ModelForm):
    username = forms.CharField(
        label="Nombre de usuario",
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Nombre de usuario"})
    )
    email = forms.EmailField(
        label="Email",
        max_length=150,
        widget=forms.EmailInput(attrs={"placeholder": "Correo electrónico"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=PasswordInput(attrs={"placeholder": "Contraseña"}),
        required=False
    )
    conf_password = forms.CharField(
        label="Confirmar contraseña",
        widget=PasswordInput(attrs={"placeholder": "Confirmar contraseña"}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["autofocus"] = True
        
        if self.instance and self.instance.pk and hasattr(self.instance, 'user'):
            self.fields['username'].initial = self.instance.user.username
            self.fields['email'].initial = self.instance.user.email

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get("password")
        password2 = cleaned_data.get("conf_password")
    
        errors = {}

        if User.objects.filter(username=username).exclude(pk=self.instance.user.pk if self.instance and self.instance.pk else None).exists():
            errors['username'] = "Este nombre de usuario ya está en uso.  "
        
        if User.objects.filter(email=email).exclude(pk=self.instance.user.pk if self.instance and self.instance.pk else None).exists():
            errors['email'] = "Este correo electrónico ya está en uso."
        
        if password1 and password2 and password1 != password2:
            errors['password'] = "Las contraseñas no coinciden."
    
        if errors:
            raise ValidationError(errors)
    
        return cleaned_data

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if self.instance.pk and hasattr(self.instance, 'user'):
            user = self.instance.user
            user.username = username
            user.email = email
            if password:
                user.set_password(password)
            user.save()
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password or None  
            )
            self.instance.user = user 

        operador = super().save(commit=False)
        operador.contrasena = password if password else operador.contrasena
        operador.conf_contrasena = cleaned_data.get('conf_password') if password else operador.conf_contrasena
        if commit:
            operador.save()
        return operador

    class Meta:
        model = Operador
        fields = ["username", "email", "nombre", "tipo_documento", "numero_documento", "telefono", "password", "conf_password"]
        widgets = {
            "nombre": TextInput(attrs={"placeholder": "Nombre del operador"}),
            "tipo_documento": Select(attrs={"placeholder": "Tipo de documento"}),
            "numero_documento": NumberInput(attrs={"min": 8, "placeholder": "Número de documento"}),
            "telefono": NumberInput(attrs={"min": 1, "placeholder": "Teléfono"}),
            "password": PasswordInput(attrs={"min": 1, "placeholder": "Contraseña"}),
            "conf_password": PasswordInput(attrs={"min": 1, "placeholder": "Confirme su contraseña"})
        }


# -------------------------------------------------------------------------------------------
 
class VentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["total_venta"].widget.attrs["autofocus"] = True

    class Meta:
        model = Venta
        fields = "__all__"
        widgets = {
            "total_venta": NumberInput(
                attrs={
                    "placeholder": "Total",
                }
            ),
            "metodo_pago": Select(
                attrs={
                    "placeholder": "Metodo de pago",
                }
            )
        }

class DetalleVentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cantidad_producto"].widget.attrs["autofocus"] = True
        self.fields['id_producto'].queryset = Producto.objects.all()

    class Meta:
        model = Detalle_venta
        fields = "__all__"
        widgets = {
            "cantidad_producto": NumberInput(
                attrs={
                    "placeholder": "Cantidad"
                }
            ),
            "id_producto": Select2Widget(
                attrs={
                    "class": "product-select"
                }
            )
        }
        
class DetalleVentaCuentaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cantidad_producto"].widget.attrs["autofocus"] = True

    class Meta:
        model = Detalle_venta_cuenta
        fields = "__all__"
        widgets = {
            "cantidad_producto": NumberInput(
                attrs={
                    "placeholder": "Cantidad"
                }
            ),
            "cantidad_plato": NumberInput(
                attrs={
                    "placeholder": "Cantidad"
                }
            ),
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
