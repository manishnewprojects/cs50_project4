# Generated by Django 2.2.5 on 2019-11-27 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalization_engine', '0002_auto_20191123_0949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='locality',
            new_name='zone',
        ),
    ]