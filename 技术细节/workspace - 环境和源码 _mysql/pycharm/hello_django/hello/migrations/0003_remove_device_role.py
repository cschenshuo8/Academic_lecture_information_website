# Generated by Django 4.2.2 on 2023-06-14 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_device_terminfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='role',
        ),
    ]
