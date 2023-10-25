from django.urls import path
from . import views

urlpatterns = [   
   #INDEX DE LA PAGINA 
   path('',views.index,name='index'),
   
    path('HomeLoc', views.login_view, name='login'),
    path('user', views.user, name='user'),
    path('admin', views.admin, name='admin'),
    path('employee',views.employee,name='employee'),
    path('cerrar',views.cerrar,name='cerrar'),


]
