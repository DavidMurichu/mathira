# Generated by Django 3.2.20 on 2023-10-02 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0014_auto_20230928_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busary_images',
            name='busary_images',
            field=models.ImageField(default=1, upload_to='static/img/busary'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='corousel_images',
            name='corousel_images',
            field=models.ImageField(default=1, upload_to='static/img/corousel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ongoing_project_images',
            name='Ongoing_Project',
            field=models.ImageField(default=1, upload_to='static/img/projects/ongoing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outlook_images',
            name='outlook_images',
            field=models.ImageField(default=1, upload_to='static/img/outlook'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='past_project_images',
            name='Past_Project',
            field=models.ImageField(default=1, upload_to='static/img/projects/past'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upcoming_project_images',
            name='Upcoming_Project',
            field=models.ImageField(default=1, upload_to='static/img/projects/upcoming'),
            preserve_default=False,
        ),
    ]
