from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('my_listings', views.my_listings, name='my_listings'),
    path('create_pdf', views.render_pdf_view, name='create_pdf'),
    path('download_pdf', views.download_pdf, name='download_pdf'),
    path('pdf', views.MyPDFView.as_view(), name='pdf'),
    path('pdf_download', views.MyPDFDownload.as_view(), name='pdf_download'),
]

