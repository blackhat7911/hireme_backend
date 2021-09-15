from django.urls import path
from work.views import *

urlpatterns = [
    path('', WorkListView.as_view(), name='work_list'),
    path('<int:pk>/', WorkListView.as_view(), name='work_detail'),
    path('request/', RequestList.as_view(), name='request_list'),
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
]