from django.urls import path
from user.views import * 
from knox import views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name="register"),
    path('login/', LoginAPI.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile_detail"),
    path('profile/location/', LocationView.as_view(), name="location"),
    path('profile/location/<int:pk>/', LocationDetailView.as_view(), name="location_detail"),
    path('profile/location/coordinates/', CoordinatesView.as_view(), name="coordinates"),
    path('profile/location/coordinates/<int:pk>/', CoordinatesDetailView.as_view(), name="coordinates_detail"),
]
