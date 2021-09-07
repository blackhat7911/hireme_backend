from django.urls import path
from user.views import * 
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile_detail"),
]
