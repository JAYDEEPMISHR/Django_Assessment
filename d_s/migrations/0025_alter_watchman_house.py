# Generated by Django 4.2 on 2023-05-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0024_alter_watchman_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchman',
            name='house',
            field=models.CharField(max_length=50),
        ),
    ]