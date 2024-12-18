# Generated by Django 5.0.6 on 2024-06-24 17:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_cliente_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='mesero',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='operador',
            name='email',
            field=models.EmailField(max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='Email'),
        ),
    ]