# Generated by Django 3.2.20 on 2023-09-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_auto_20230926_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='customizer',
            name='image_title',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
