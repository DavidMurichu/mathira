# Generated by Django 3.2.20 on 2023-09-27 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_appointmentapproved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='agenda',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='appointmentapproved',
            name='agenda',
            field=models.CharField(max_length=500),
        ),
    ]