# Generated by Django 5.0.7 on 2024-08-06 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_detalle_venta_order_with_respect_to_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total_venta_iva',
        ),
    ]
