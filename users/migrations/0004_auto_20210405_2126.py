# Generated by Django 3.1.6 on 2021-04-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210405_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]