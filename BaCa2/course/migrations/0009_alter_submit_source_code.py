# Generated by Django 4.1.3 on 2022-12-30 12:39

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_submit_usr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='source_code',
            field=models.FileField(upload_to=pathlib.PureWindowsPath('C:/Users/48698/PycharmProjects/BaCa2/BaCa2/submits')),
        ),
    ]