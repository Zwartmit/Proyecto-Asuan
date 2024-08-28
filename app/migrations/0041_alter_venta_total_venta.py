# Generated by Django 5.1 on 2024-08-26 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0040_alter_venta_total_venta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total de la venta'),
        ),
    ]
