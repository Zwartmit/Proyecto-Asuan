# Generated by Django 5.0.6 on 2024-06-23 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_administrador_numero_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='numero_documento',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='administrador',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=50, unique=True, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='numero_documento',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_emision_factura',
            field=models.DateTimeField(blank=True, verbose_name='Fecha de emisión de la factura'),
        ),
        migrations.AlterField(
            model_name='mesero',
            name='numero_documento',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='mesero',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='metodo_pago',
            name='metodo',
            field=models.CharField(choices=[('EF', 'Efectivo'), ('TF', 'Transferencia')], default='EF', max_length=2, verbose_name='Método'),
        ),
        migrations.AlterField(
            model_name='operador',
            name='numero_documento',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='operador',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='descripcion',
            field=models.CharField(max_length=300, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='nombre_plato',
            field=models.CharField(max_length=50, verbose_name='Nombre del plato'),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='presentacion',
            field=models.CharField(max_length=50, unique=True, verbose_name='Presentación'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='cantidad_producto',
            field=models.PositiveIntegerField(verbose_name='Cantidad de productos'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(blank=True, verbose_name='Fecha de venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total de la venta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_venta_iva',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total de la venta con iva'),
        ),
    ]
