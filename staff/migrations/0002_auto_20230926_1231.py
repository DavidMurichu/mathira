# Generated by Django 3.2.20 on 2023-09-26 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customizer',
            name='events_images',
        ),
        migrations.RemoveField(
            model_name='customizer',
            name='projects_images',
        ),
    ]
