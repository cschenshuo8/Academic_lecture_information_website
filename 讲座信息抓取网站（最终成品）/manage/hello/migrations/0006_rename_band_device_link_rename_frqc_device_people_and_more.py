# Generated by Django 4.2.2 on 2023-06-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0005_rename_s_device_sn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='band',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='frqc',
            new_name='people',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='fw',
            new_name='place',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='gps',
            new_name='release_time',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='mac',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='device',
            old_name='plmn',
            new_name='university',
        ),
        migrations.RemoveField(
            model_name='device',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='device',
            name='cnm',
        ),
        migrations.RemoveField(
            model_name='device',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='device',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='device',
            name='rf',
        ),
        migrations.RemoveField(
            model_name='device',
            name='rip',
        ),
        migrations.RemoveField(
            model_name='device',
            name='sn',
        ),
        migrations.RemoveField(
            model_name='device',
            name='sync',
        ),
        migrations.RemoveField(
            model_name='device',
            name='tmp',
        ),
        migrations.AddField(
            model_name='device',
            name='content',
            field=models.CharField(default=0, max_length=2000),
        ),
        migrations.AddField(
            model_name='device',
            name='intro',
            field=models.CharField(default=0, max_length=2000),
        ),
    ]
