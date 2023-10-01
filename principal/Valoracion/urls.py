from django.urls import path
from . import views
from Login.views import proteccion_rutas


app_name = 'Valoracion'


urlpatterns = [
    path('HomeLoc/admin/registrarvaloracion/', proteccion_rutas([1])(views.RegistroValoracion), name='registrarvaloracion'),
    path('HomeLoc/admin/guardarvaloracion/', proteccion_rutas([1])(views.Guardar_Valoracion), name='guardarvaloracion'),
    path('HomeLoc/admin/listarvaloracion/',proteccion_rutas([1])(views.ListarValoracion),name='listarvaloracion') 
]