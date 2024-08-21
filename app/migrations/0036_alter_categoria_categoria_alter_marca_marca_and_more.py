# Generated by Django 5.1 on 2024-08-21 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_categoria_estado_marca_estado_presentacion_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='categoria',
            field=models.CharField(max_length=50, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='marca',
            field=models.CharField(max_length=50, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='presentacion',
            field=models.CharField(max_length=50, verbose_name='Presentación'),
        ),
    ]