from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    seeker                = models.ForeignKey(User, on_delete=models.CASCADE, related_name="req_seeker", null=True)
    worker                = models.ForeignKey(User, on_delete=models.CASCADE, related_name="req_worker", null=True)
    title                 = models.CharField(max_length=200)
    description           = models.TextField()
    location              = models.CharField(max_length=200)
    request_date          = models.DateTimeField(auto_now_add=True)
    is_accepted           = models.BooleanField(default=False)
    is_cancelled          = models.BooleanField(default=False)
    request_accepted_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

    def isAccepted(self):
        return self.request_status

class Work(models.Model):
    request       = models.ForeignKey(Request, on_delete=models.CASCADE, related_name="work_request") 
    isCompleted   = models.BooleanField(default=False)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.request.title)