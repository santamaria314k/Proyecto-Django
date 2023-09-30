from django.urls import path
from . import views


app_name = 'Valoracion'



urlpatterns = [
    path('HomeLoc/admin/registrarvaloracion/', views.RegistroValoracion, name='registrarvaloracion'),
    path('HomeLoc/admin/guardarvaloracion/', views.Guardar_Valoracion, name='guardarvaloracion'),


]
