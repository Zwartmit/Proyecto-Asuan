# Generated by Django 5.1 on 2024-08-22 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_detalle_venta_subtotal_venta'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'ordering': ['-fecha_venta'], 'verbose_name': 'venta', 'verbose_name_plural': 'ventas'},
        ),
        migrations.AlterOrderWithRespectTo(
            name='venta',
            order_with_respect_to=None,
        ),
    ]