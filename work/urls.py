from django.urls import path
from work.views import *

urlpatterns = [
    path('', WorkListView.as_view(), name='work_list'),
    path('<int:pk>/', WorkListView.as_view(), name='work_detail'),
    path('worker/', WorkerWorkList.as_view(), name='worker_work_list'),
    path('seeker/', SeekerWorkList.as_view(), name='seeker_work_list'),
    path('request/', RequestList.as_view(), name='request_list'),
]