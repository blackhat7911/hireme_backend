from django.urls import path
from user.views import * 

urlpatterns = [
    path('', UserView.as_view(), name="user"),
]