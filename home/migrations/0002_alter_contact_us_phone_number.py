# Generated by Django 3.2.20 on 2023-09-18 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_us',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
