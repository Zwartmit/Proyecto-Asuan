# Generated by Django 5.1.1 on 2024-09-10 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='presentacion',
            unique_together={('presentacion', 'unidad_medida')},
        ),
    ]