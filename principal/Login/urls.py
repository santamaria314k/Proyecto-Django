from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('user', views.user, name='user'),
    path('admin', views.admin, name='admin'),

    
]
