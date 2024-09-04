# Generated by Django 5.0.7 on 2024-07-31 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_alter_venta_options_alter_venta_metodo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='metodo_pago',
            field=models.CharField(choices=[('EF', 'Efectivo'), ('TF', 'Transferencia')], default='EF', max_length=3, verbose_name='Método de Pago'),
        ),
    ]
