# Generated by Django 5.0.6 on 2024-06-28 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_venta_metodo_pago_alter_venta_id_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='conf_contraseña',
            field=models.CharField(default='', max_length=50, verbose_name='Confirme su contraseña'),
        ),
    ]
