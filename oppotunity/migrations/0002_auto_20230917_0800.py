# Generated by Django 3.2.20 on 2023-09-17 08:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oppotunity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oppotunities',
            name='id_number',
            field=models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='Phone number must be at least 10 digits.'), django.core.validators.MaxLengthValidator(limit_value=10, message='Phone number can have at most 10 digits.'), django.core.validators.RegexValidator(message='Phone number must contain only digits.', regex='^[0-9]{10}$')]),
        ),
        migrations.AlterField(
            model_name='oppotunities',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(limit_value=10, message='Phone number must be at least 10 digits.'), django.core.validators.MaxLengthValidator(limit_value=10, message='Phone number can have at most 10 digits.'), django.core.validators.RegexValidator(message='Phone number must contain only digits.', regex='^[0-9]{10}$')]),
        ),
    ]
