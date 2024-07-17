# Generated by Django 5.0.6 on 2024-06-24 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_cliente_numero_documento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numero_documento',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cliente'),
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='id_mesero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mesero'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='id_metodo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.metodo_pago'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='id_venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.venta'),
        ),
        migrations.AlterField(
            model_name='mesero',
            name='numero_documento',
            field=models.PositiveIntegerField(unique=True, verbose_name='Número de documento'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.administrador'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_cuenta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cuenta'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='id_operador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.operador'),
        ),
    ]