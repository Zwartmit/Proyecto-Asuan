# Generated by Django 5.1 on 2024-08-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_alter_venta_order_with_respect_to_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle_venta',
            name='subtotal_venta',
            field=models.PositiveIntegerField(default='0', verbose_name='Subtotal'),
        ),
    ]