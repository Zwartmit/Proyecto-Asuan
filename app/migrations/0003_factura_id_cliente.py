# Generated by Django 5.1.1 on 2024-10-03 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_factura_fecha_emision_factura'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='id_cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.cliente'),
        ),
    ]
