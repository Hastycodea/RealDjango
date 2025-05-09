from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload', views.upload_excel, name='upload'),
    path('map', views.map_headers, name='map_headers'),
]