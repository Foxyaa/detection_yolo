# Generated by Django 4.2.11 on 2024-05-26 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opencv', '0004_alter_uploadimg_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimg',
            name='title',
            field=models.TextField(),
        ),
    ]
