# Generated by Django 4.2 on 2023-05-20 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('d_s', '0010_alter_events_date_alter_notice_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=50)),
                ('mobile', models.PositiveIntegerField()),
                ('purpose', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
