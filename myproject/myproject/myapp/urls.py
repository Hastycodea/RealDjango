from django.urls import path
from . import views

urlpatterns = [
    path('task_list', views.task_list, name='task_list')
]