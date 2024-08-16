# Generated by Django 5.1 on 2024-08-15 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_alter_venta_metodo_pago'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='venta',
            order_with_respect_to='fecha_venta',
        ),
        migrations.AlterField(
            model_name='venta',
            name='fecha_venta',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Detalle_venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.PositiveIntegerField(verbose_name='Cantidad de productos')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.venta')),
            ],
            options={
                'verbose_name': 'detalle_de_venta',
                'verbose_name_plural': 'detalles_de_ventas',
                'db_table': 'Detalle_venta',
            },
        ),
        migrations.CreateModel(
            name='Detalle_venta_cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_producto', models.PositiveIntegerField(verbose_name='Cantidad de productos')),
                ('cantidad_plato', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.cliente')),
                ('id_mesero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.mesero')),
                ('id_plato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.plato')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.producto')),
                ('id_venta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.venta')),
            ],
            options={
                'verbose_name': 'detalle_venta_cuenta',
                'verbose_name_plural': 'detalles_venta_cuentas',
                'db_table': 'Detalle_venta_cuenta',
            },
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cantidad_producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_admin',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_cuenta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_operador',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='id_producto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='total_venta_iva',
        ),
        migrations.DeleteModel(
            name='Cuenta',
        ),
    ]
