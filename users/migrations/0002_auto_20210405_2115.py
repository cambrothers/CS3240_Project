# Generated by Django 3.1.6 on 2021-04-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='schedule_image',
            field=models.ImageField(blank=True, default='', upload_to='images/'),
        ),
    ]
