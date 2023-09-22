from django.urls import path

from . import views





urlpatterns = [
    path('Login/', views.login, name='login'),  
    path('Admin/', views.admin, name='Admin'), 
    path('User/', views.user, name='User'),  
]

