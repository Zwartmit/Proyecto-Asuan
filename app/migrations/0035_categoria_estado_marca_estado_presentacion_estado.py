# Generated by Django 5.1 on 2024-08-21 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_alter_presentacion_unidad_medida'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='marca',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='presentacion',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
