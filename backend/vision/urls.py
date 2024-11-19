from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('scan/', views.ScanView, name='scan_image'),
    path('scan-flow/', views.ScanViewTest, name='scan_flow')
]