# Generated by Django 4.2.6 on 2023-10-13 16:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_rename_busary_images_busary_images_busary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ongoing_project_images',
            name='project_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='ongoing_project_images',
            name='project_location',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ongoing_project_images',
            name='project_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='past_project_images',
            name='project_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='past_project_images',
            name='project_location',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='past_project_images',
            name='project_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upcoming_project_images',
            name='project_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='upcoming_project_images',
            name='project_location',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upcoming_project_images',
            name='project_name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
