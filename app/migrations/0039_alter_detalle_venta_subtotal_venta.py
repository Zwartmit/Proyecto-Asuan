# Generated by Django 5.1 on 2024-08-22 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0038_venta_fecha_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_venta',
            name='subtotal_venta',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=8, verbose_name='Subtotal'),
        ),
    ]
