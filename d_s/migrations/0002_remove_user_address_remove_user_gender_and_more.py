# Generated by Django 4.2 on 2023-04-18 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_pic',
        ),
    ]
