# Generated by Django 4.2 on 2023-05-19 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0009_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
