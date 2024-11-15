from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.ScanView, name='scan_image'),
]