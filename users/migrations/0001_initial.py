# Generated by Django 3.1.6 on 2021-03-20 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('bio', models.CharField(max_length=500)),
                ('pronouns', models.CharField(max_length=400)),
                ('age', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('dorm_pref', models.CharField(choices=[('No preference.', 'None'), ('Hall-Style', 'Hall'), ('Suite-Style', 'Suite')], default='No preference.', max_length=100)),
                ('school', models.CharField(choices=[('default', 'Default'), ('College and Graduate School of Arts and Sciences', 'College'), ('School of Engineering and Applied Science', 'Eng'), ('School of Architecture', 'Arch'), ('McIntire School of Commerce', 'Comm'), ('School of Nursing', 'Nurse'), ('School of Medicine', 'Med'), ('School of Law', 'Law'), ('School of Education and Human Development', 'Edu'), ('School of Data Science', 'Ds'), ('School of Continuing & Professional Studies', 'Prof'), ('Frank Batten School of Leadership and Public Policy', 'Lead'), ('Darden School of Business', 'Busi')], default='default', max_length=500)),
                ('roomates', models.PositiveIntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
