# Generated by Django 4.2.11 on 2024-05-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencv', '0003_rename_image_uploadimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimg',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
