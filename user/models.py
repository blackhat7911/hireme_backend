from django.db import models
from django.contrib.auth import validators
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Coordinates(models.Model):
    lat     = models.FloatField()
    lang    = models.FloatField()

class Location(models.Model):
    city        = models.CharField(max_length=255, null=True)
    zipCode     = models.IntegerField(null=True)
    Coordinates = models.ForeignKey(Coordinates, on_delete=models.DO_NOTHING, null=True)

class Profile(models.Model):
    USER_TYPE = (
        ('WORKER', 'WORKER'),
        ('SEEKER', 'SEEKER')
    )
    user            = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE, null=True)
    fullname        = models.CharField(max_length=255, null=True)
    phone           = models.CharField(max_length=16, null=True)
    profile         = models.FileField(upload_to='static/avtar/', null=True)
    date_of_birth   = models.DateField(null=True)
    accountType     = models.CharField(max_length=30,null=True,choices=USER_TYPE, blank=True)
    location        = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

