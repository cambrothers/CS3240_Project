# Generated by Django 3.1.6 on 2021-04-19 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210419_0956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='snapchat_handle',
            new_name='linked_in',
        ),
    ]