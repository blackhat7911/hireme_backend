from django.db import models
from django.contrib.auth import validators
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Coordinates(models.Model):
    lat         = models.FloatField()
    lang        = models.FloatField()

    def __str__(self):
        return str(self.lat) + ", " + str(self.lang)
class Location(models.Model):
    user        = models.OneToOneField(User,related_name='user_location', on_delete=models.CASCADE, null=True)
    city        = models.CharField(max_length=255, null=True)
    zipCode     = models.IntegerField(null=True)
    coordinates    = models.OneToOneField(Coordinates,related_name='location_coordinates', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return str(self.city)



class Profile(models.Model):
    USER_TYPE = (
        ('WORKER', 'WORKER'),
        ('SEEKER', 'SEEKER')
    )
    user            = models.OneToOneField(User,related_name='user', on_delete=models.CASCADE, null=True)
    fullname        = models.CharField(max_length=255, null=True)
    phone           = models.CharField(max_length=16, null=True)
    profile         = models.FileField(upload_to='static/avtar/', null=True)
    date_of_birth   = models.DateField(null=True)
    accountType     = models.CharField(max_length=30,null=True,choices=USER_TYPE, blank=True)
    work            = models.CharField(max_length=255, null=True, blank=True)
    location        = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username)

