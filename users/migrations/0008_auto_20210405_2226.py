# Generated by Django 3.1.6 on 2021-04-06 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210405_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='media/images/noimage_csnmxo.png', upload_to='images/'),
        ),
    ]
