from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent, name='password-reset-sent'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.RegisterView, name='register'),
    path('reset-password/<str:reset_id>/', views.ResetPassword, name='reset-password'),
]