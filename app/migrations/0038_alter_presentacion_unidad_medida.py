# Generated by Django 5.1 on 2024-08-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_categoria_categoria_alter_marca_marca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='unidad_medida',
            field=models.CharField(choices=[('litro(s)', 'litro(s)'), ('mililitro(s)', 'mililitro(s)'), ('gramo(s)', 'gramo(s)')], default='', max_length=12, verbose_name='Unidad de medida'),
        ),
    ]
