# Generated by Django 4.2 on 2023-04-18 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0003_rename_user_chairmans'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chairmans',
            new_name='User',
        ),
    ]