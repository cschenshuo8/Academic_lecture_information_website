# Generated by Django 4.2.2 on 2023-06-15 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0013_remove_device_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='intro',
        ),
    ]
