# Generated by Django 4.2 on 2023-05-21 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0015_alter_watchman_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='house',
            field=models.CharField(default='A-101', max_length=20),
        ),
    ]