# Generated by Django 5.1.1 on 2024-09-11 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_presentacion_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentacion',
            name='presentacion',
            field=models.CharField(max_length=50, verbose_name='Presentación'),
        ),
    ]