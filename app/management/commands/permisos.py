from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from app.models import Venta, Factura  # Reemplaza 'app' con el nombre real de tu aplicación

class Command(BaseCommand):
    help = 'Assign permissions to the Operator group for Venta and Factura models'

    def handle(self, *args, **kwargs):
        # Obtener el grupo Operador
        operador_group = Group.objects.get(name='Operador')

        # Obtener los ContentTypes de los modelos Venta y Factura
        venta_ct = ContentType.objects.get_for_model(Venta)
        factura_ct = ContentType.objects.get_for_model(Factura)

        # Obtener los permisos para los modelos Venta y Factura
        permisos_venta = Permission.objects.filter(content_type=venta_ct)
        permisos_factura = Permission.objects.filter(content_type=factura_ct)

        # Asignar permisos al grupo Operador
        operador_group.permissions.set(permisos_venta | permisos_factura)

        self.stdout.write(self.style.SUCCESS("Permisos asignados al grupo Operador para los modelos Venta y Factura."))