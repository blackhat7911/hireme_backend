# Generated by Django 3.0.5 on 2021-09-12 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210913_0530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='oordinates',
            new_name='coordinates',
        ),
    ]