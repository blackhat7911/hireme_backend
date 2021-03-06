# Generated by Django 3.0.5 on 2021-09-15 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0008_auto_20210911_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='request_status',
            new_name='is_accepted',
        ),
        migrations.RemoveField(
            model_name='work',
            name='seeker',
        ),
        migrations.RemoveField(
            model_name='work',
            name='worker',
        ),
        migrations.AddField(
            model_name='request',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
