# Generated by Django 2.0.4 on 2018-04-30 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180430_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre_name',
            new_name='name',
        ),
    ]
