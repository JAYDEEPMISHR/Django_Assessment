# Generated by Django 4.2 on 2023-05-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0013_watchman'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchman',
            name='status',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
