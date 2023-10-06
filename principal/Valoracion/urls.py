from django.urls import path
from Login.views import proteccion_rutas

from . import views

app_name = 'Valoracion'



urlpatterns = [
    
    

    path('HomeLoc/admin/registrarvaloracion/', proteccion_rutas([1])(views.RegistroValoracion), name='registrarvaloracion'),
    path('HomeLoc/admin/guardarvaloracion/', proteccion_rutas([1])(views.Guardar_Valoracion), name='guardarvaloracion'),
    path('HomeLoc/admin/listarvaloracion/',proteccion_rutas([1])(views.ListarValoracion),name='listarvaloracion') ,
    path('HomeLoc/admin/editarvaloracion/<id_val>/',proteccion_rutas([1])(views.editar_valoracion),name='editarvaloracion') ,
    path('HomeLoc/admin/listarvaloracion/eliminarvaloracion/<id_val>/',proteccion_rutas([1])(views.eliminar_valoracion),name='eliminarvaloracion') ,


    path('HomeLoc/employee/registrarvaloracionemplo/', proteccion_rutas([3])(views.RegistroValoracionemplo), name='registrarvaloracionemplo'),
    path('HomeLoc/employee/guardarvaloracionemplo/', proteccion_rutas([3])(views.Guardar_Valoracionemplo), name='guardarvaloracionemplo'),
    path('HomeLoc/employee/listarvaloracionemplo/',proteccion_rutas([3])(views.ListarValoracionemplo),name='listarvaloracionemplo') ,
    path('HomeLoc/employee/editarvaloracionemplo/<id_val>/',proteccion_rutas([3])(views.editar_valoracionemplo),name='editarvaloracionemplo') ,
    path('HomeLoc/employee/listarvaloracionemplo/eliminarvaloracionemplo/<id_val>/',proteccion_rutas([3])(views.eliminar_valoracion),name='eliminarvaloracionemplo') ,

]


