# Generated by Django 3.0.5 on 2021-09-04 08:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210904_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lang', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='accountType',
            field=models.CharField(blank=True, choices=[('WORKER', 'WORKER'), ('SEEKER', 'SEEKER')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255, null=True)),
                ('zipCode', models.IntegerField(null=True)),
                ('Coordinates', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Coordinates')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Location'),
        ),
    ]
