from django.db import models
from django.contrib.auth import validators
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_TYPE = (
        ('WORKER', 'WORKER'),
        ('SEEKER', 'SEEKER')
    )
    user            = models.ForeignKey(User,related_name='user', on_delete=models.CASCADE, null=True)
    fullname        = models.CharField(max_length=255, null=True)
    phone           = models.IntegerField(null=True)
    profile         = models.FileField(upload_to='static/avtar/', null=True)
    date_of_birth   = models.DateTimeField(null=True)
    accountType     = models.CharField(max_length=30,null=True,choices=USER_TYPE)

    def __str__(self):
        return self.fullname

