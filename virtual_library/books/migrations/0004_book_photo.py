# Generated by Django 2.0.4 on 2018-04-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20180430_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(null=True, upload_to='books'),
        ),
    ]