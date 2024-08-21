from django.db import models
from .choices import codigos_telefonicos_paises
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.validators import MinLengthValidator

class Categoria (models.Model):
    categoria = models.CharField(max_length=50, verbose_name="Categoría", unique=True)

    def __str__(self):
        return f"{self.categoria}"

    class Meta:
        verbose_name= "categoria"
        verbose_name_plural ='categorias'
        db_table ='Categoria'
    
########################################################################################################################################
    
class Marca (models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca", unique=True)

    def __str__(self):
        return f"{self.marca}"

    class Meta:
        verbose_name= "marca"
        verbose_name_plural ='marcas'
        db_table ='Marca'
        
########################################################################################################################################

class Presentacion (models.Model):
    presentacion = models.CharField(max_length=50, verbose_name="Presentación", unique=True)

    def __str__(self):
        return f"{self.presentacion}"

    class Meta:
        verbose_name= "presentacion"
        verbose_name_plural ='presentaciones'
        db_table ='Presentacion'
        
########################################################################################################################################

class Producto(models.Model):
    producto = models.CharField(max_length=50, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")
    estado = models.BooleanField(default=True, verbose_name="Estado")
    id_categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name="Categoría")
    id_marca = models.ForeignKey(Marca, on_delete=models.PROTECT, verbose_name="Marca")
    id_presentacion = models.ForeignKey(Presentacion, on_delete=models.PROTECT, verbose_name="Presentación")

    def __str__(self):
        return f"{self.producto}"

    class Meta:
        verbose_name= "producto"
        verbose_name_plural ='productos'
        db_table ='Producto'

########################################################################################################################################

class Mesero(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        RC = 'RC', 'Registro Civil'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")
        
    def validar_email(value):
        value = "foo.bar@baz.qux"
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError("Correo rechazado")  
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    email = models.EmailField(max_length=50, verbose_name="Email", validators=[validate_email])
    pais_telefono = models.CharField(max_length=50, choices=[(pais, pais) for pais in codigos_telefonicos_paises], default='Colombia (+57)', verbose_name="Prefijo telefónico")
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name= "mesero"
        verbose_name_plural ='meseros'
        db_table ='Mesero'

########################################################################################################################################

class Cliente(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        RC = 'RC', 'Registro Civil'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")
        
    def validar_email(value):
        value = "foo.bar@baz.qux"
        try:
            validate_email(value)
        except ValidationError:
            raise ValidationError("Correo rechazado")  
        
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    email = models.EmailField(max_length=50, verbose_name="Email", validators=[validate_email])
    pais_telefono = models.CharField(max_length=50, choices=[(pais, pais) for pais in codigos_telefonicos_paises], default='Colombia (+57)', verbose_name="Prefijo telefónico")
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")

    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name= "cliente"
        verbose_name_plural ='clientes'
        db_table ='Cliente'

########################################################################################################################################

class Plato(models.Model):
    plato = models.CharField(max_length=50, verbose_name="Nombre del plato")
    descripcion = models.CharField(max_length=300, verbose_name="Descripción")
    valor = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    def __str__(self):
        return f"{self.plato}"

    class Meta:
        verbose_name= "plato"
        verbose_name_plural ='platos'
        db_table ='Plato'

########################################################################################################################################

class Administrador(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        CE = 'CE', 'Cédula de Extranjería'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")
    contrasena = models.CharField(max_length=128, validators=[MinLengthValidator(8)], verbose_name="Contraseña")
    conf_contrasena = models.CharField(max_length=128, verbose_name="Confirmación de contraseña", default="")

    def clean(self):
        super().clean()
        if self.contrasena != self.conf_contrasena:
            raise ValidationError({"conf_contrasena": "Las contraseñas no coinciden"})

    def save(self, *args, **kwargs):
        if not self.pk or 'user' not in kwargs:
            user, created = User.objects.get_or_create(username=self.user.username)
        else:
            user = self.user

        if self.contrasena:
            user.set_password(self.contrasena)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.user = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
        db_table = 'Administrador'

@receiver(post_delete, sender=Administrador)
def eliminar_usuario_relacionado(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()

########################################################################################################################################

class Operador(models.Model):
    class TipoDocumento(models.TextChoices):
        CC = 'CC', 'Cédula de Ciudadanía'
        TI = 'TI', 'Tarjeta de Identidad'
        CE = 'CE', 'Cédula de Extranjería'
        PSP = 'PSP', 'Pasaporte'

    def validar_numero_documento(value):
        if value < 10000000 or value > 9999999999:
            raise ValidationError("El número de documento debe tener entre 8 y 10 dígitos")

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='operador')
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    tipo_documento = models.CharField(max_length=3, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de documento")
    numero_documento = models.PositiveIntegerField(verbose_name="Número de documento", unique=True, validators=[validar_numero_documento])
    telefono = models.PositiveIntegerField(verbose_name="Teléfono")
    contrasena = models.CharField(max_length=128, validators=[MinLengthValidator(8)], verbose_name="Contraseña")
    conf_contrasena = models.CharField(max_length=128, verbose_name="Confirmación de contraseña", default="")

    def clean(self):
        super().clean()
        if self.contrasena != self.conf_contrasena:
            raise ValidationError({"conf_contrasena": "Las contraseñas no coinciden"})

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Operador"
        verbose_name_plural = "Operadores"
        db_table = 'Operador'

@receiver(post_delete, sender=Operador)
def eliminar_usuario_relacionado(sender, instance, **kwargs):
    user = instance.user
    if user:
        user.delete()

########################################################################################################################################        

class Venta(models.Model):
    class MedotoPago(models.TextChoices):
        EF = 'EF', 'Efectivo'
        TF = 'TF', 'Transferencia'

    fecha_venta = models.DateTimeField(auto_now=True)
    total_venta = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Total de la venta")
    metodo_pago = models.CharField(max_length=3, choices=MedotoPago.choices, default=MedotoPago.EF, verbose_name="Metodo de Pago")

    def _str_(self):
        return str(self.id)

    class Meta:
        verbose_name= "venta"
        verbose_name_plural ='ventas'
        order_with_respect_to = 'fecha_venta'
        db_table ='Venta'

########################################################################################################################################

class Detalle_venta(models.Model):
    
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad_producto = models.PositiveIntegerField(verbose_name="Cantidad de productos")
    subtotal_venta = models.PositiveIntegerField(verbose_name="Subtotal", default="0")


    def _str_(self):
        return self.id_producto

    class Meta:
        verbose_name= "detalle_de_venta"
        verbose_name_plural ='detalles_de_ventas'
        db_table ='Detalle_venta'

########################################################################################################################################

class Detalle_venta_cuenta(models.Model):

    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)
    id_producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad_producto = models.PositiveIntegerField(verbose_name="Cantidad de productos")
    id_plato = models.ForeignKey(Plato,on_delete=models.PROTECT)
    cantidad_plato = models.PositiveIntegerField(verbose_name="Cantidad")
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    id_mesero = models.ForeignKey(Mesero, on_delete=models.PROTECT)

    def _str_(self):
        return self.id_producto

    class Meta:
        verbose_name= "detalle_venta_cuenta"
        verbose_name_plural ='detalles_venta_cuentas'
        db_table ='Detalle_venta_cuenta'

########################################################################################################################################

class Factura(models.Model):
    fecha_emision_factura = models.DateTimeField(null=False, blank=True, verbose_name="Fecha de emisión de la factura")
    id_venta = models.ForeignKey(Venta, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.fecha_emision_factura}"

    class Meta:
        verbose_name= "factura"
        verbose_name_plural ='facturas'
        db_table ='Factura'

########################################################################################################################################
