# Generated by Django 3.0.5 on 2021-09-11 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20210911_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinates',
            name='user',
        ),
        migrations.RemoveField(
            model_name='location',
            name='Coordinates',
        ),
        migrations.AddField(
            model_name='coordinates',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_coordinates', to='user.Location'),
        ),
    ]
