# Generated by Django 3.0.5 on 2021-09-11 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_work_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_request', to='work.Request'),
        ),
    ]