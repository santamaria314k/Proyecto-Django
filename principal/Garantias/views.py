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








#=======================================================
#=======================================================
#=======================================================
#=================_GARANTIAS============================

def Registro_Garantia(request):
    RegiGarantia=GarantiasForm()
    return render(request,'registrar_garantias.html',{'form':RegiGarantia})

#---------------------------------------------------------------------

def Guardar_Garantia(request):
    if request.method == 'POST':
        RegiGarantia=GarantiasForm(request.POST)
        if RegiGarantia.is_valid():
            # Guardar el diagnóstico en la base de datos
            fecha_i = RegiGarantia.cleaned_data['fechaInicio']
            fecha_f = RegiGarantia.cleaned_data['fechaFin']
            reggarantia = GarantiasForm(fechaInicio =fecha_i,fechaFin =fecha_f)
            reggarantia.save()
    return render(request,'registro_tipogarantias.html',{'form':RegiGarantia,"mensaje":'tipo de garantia -registrada'},)