from django.shortcuts import render
from .forms import GarantiasForm,TiposGarantiaForm
from .models import TiposGarantia
# Create your views here.


#=======================================================
#=======================================================
#=======================================================
#=================TIPOS_DE_GARANTIA======================
def Registro_Tipo_Garantia(request): 
    RegiTipoGarantia=TiposGarantiaForm()
    return render(request,'registro_tipogarantias.html',{'form':RegiTipoGarantia})

#---------------------------------------------------------------------
def Guardar_Tipo_Garantia(request):
    if request.method == 'POST':
        RegiTipoGarantia = TiposGarantiaForm(request.POST)
        if RegiTipoGarantia.is_valid():
            # Guardar el diagnóstico en la base de datos
            nombre_text = RegiTipoGarantia.cleaned_data['nombre']
            tipgarantia = TiposGarantia(nombre=nombre_text)
            tipgarantia.save()
    return render(request,'registro_tipogarantias.html',{'form':RegiTipoGarantia,"mensaje":'tipo de garantia -registrada'},)

#---------------------------------------------------------------------

def ListarTiposGarantia(request):
    listadoTipoGarantia=TiposGarantia.objects.all()
    return render ( request,'listar_tipogarantias.html',{'listadoTipoGarantia':listadoTipoGarantia})

