from django.db import models
from django.contrib.auth.models import User

class Work(models.Model):
    seeker        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seeker")
    worker        = models.ForeignKey(User, on_delete=models.CASCADE, related_name="worker", null=True, blank=True)
    title         = models.CharField(max_length=200)
    description   = models.TextField()
    Location      = models.CharField(max_length=200)
    workerStatus  = models.BooleanField(default=False)
    isCompleted   = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)