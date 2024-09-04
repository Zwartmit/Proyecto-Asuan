# Generated by Django 5.1 on 2024-08-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_presentacion_unidad_medida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='unidad_medida',
            field=models.CharField(choices=[('litros', 'litros'), ('mililitros', 'mililitros'), ('gramos', 'gramos')], default='', max_length=12, verbose_name='Tipo de documento'),
        ),
    ]
