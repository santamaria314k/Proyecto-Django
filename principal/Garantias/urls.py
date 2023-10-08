
from django.urls import path 
from Login.views import proteccion_rutas
from .import views

app_name = 'Garantias'

urlpatterns = [


 path('HomeLoc/admin/registrotipogarantia', proteccion_rutas([1])(views.Registro_Tipo_Garantia), name='registrotipogarantia'),
 path('HomeLoc/admin/guardartipogarantia', proteccion_rutas([1])(views.Guardar_Tipo_Garantia), name='guardartipogarantia'),
 path('HomeLoc/admin/listartipogarantia', proteccion_rutas([1])(views.ListarTiposGarantia), name='listartipogarantia'),

]
