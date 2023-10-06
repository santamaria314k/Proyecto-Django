from django.http import HttpRequest
from django.shortcuts import render,redirect
from .forms import ValoracionForm
from .models import Diagnostico
from django.contrib import messages
# Create your views here.

#===========================================================
#===========================================================
#===========================================================
#===========================================================
# ADMINISTRADOR ==================================

def RegistroValoracion(request): 
    registrovalor=ValoracionForm()
    return render(request,'registro_valoracion.html',{'form':registrovalor})
#---------------------------------------------------------------------
def Guardar_Valoracion(request):
    if request.method == 'POST':
        registrovalor = ValoracionForm(request.POST)
        if registrovalor.is_valid():
            # Guardar el diagnóstico en la base de datos
            diagnostico_text = registrovalor.cleaned_data['diagnostico']
            diagnostico = Diagnostico(diagnostico=diagnostico_text)
            diagnostico.save()
    return render(request,'registro_valoracion.html',{'form':registrovalor,"mensaje":'valoracion-registrada'},)



#===========================================================
def ListarValoracion(request):
    listadoDiagnosticos=Diagnostico.objects.all()
    return render ( request,'listar_valoracion.html',{'listadoDiagnosticos':listadoDiagnosticos})



#===========================================================


def editar_valoracion(request, id_val):
    valoracion=Diagnostico.objects.get(id_val=id_val)
    
    if request.method == 'POST':
        editavaloracion = ValoracionForm(data=request.POST, instance=valoracion)
        if editavaloracion.is_valid():
            editavaloracion.save()
            return redirect('Valoracion:listarvaloracion')
        else:
            return redirect('Valoracion:editarvaloracion')

    registrovalor = ValoracionForm(instance=valoracion)
    return render(request, 'editar_valoracion.html', {'form': registrovalor})

#===========================================================

def eliminar_valoracion(request,id_val):
    valoraciondelete=Diagnostico.objects.get(id_val=id_val)
    valoraciondelete.delete()
    return render(request,'listar_valoracion.html')






#===========================================================
#===========================================================
#===========================================================
#===========================================================
# TRABAJADOR ===============================================

def RegistroValoracionemplo(request): 
    registrovalor=ValoracionForm()
    return render(request,'registro_valoracionemplo.html',{'form':registrovalor})

def Guardar_Valoracionemplo(request):
    if request.method == 'POST':
        registrovalor = ValoracionForm(request.POST)
        if registrovalor.is_valid():
            # Guardar el diagnóstico en la base de datos
            diagnostico_text = registrovalor.cleaned_data['diagnostico']
            diagnostico = Diagnostico(diagnostico=diagnostico_text)
            diagnostico.save()
    return render(request,'registro_valoracionemplo.html',{'form':registrovalor,"mensaje":'valoracion-registrada'},)

#===========================================================


#===========================================================
def ListarValoracionemplo(request):
    listadoDiagnosticos=Diagnostico.objects.all()
    return render ( request,'listar_valoracionemplo.html',{'listadoDiagnosticos':listadoDiagnosticos})




#===========================================================


def editar_valoracionemplo(request, id_val):
    valoracionemplo=Diagnostico.objects.get(id_val=id_val)
    
    if request.method == 'POST':
        editavaloracionemplo = ValoracionForm(data=request.POST, instance=valoracionemplo)
        if editavaloracionemplo.is_valid():
            editavaloracionemplo.save()
            return redirect('Valoracion:listarvaloracionemplo')
        else:
            return redirect('Valoracion:editarvaloracionemplo')

    registrovaloremplo = ValoracionForm(instance=valoracionemplo)
    return render(request, 'editar_valoracionemplo.html', {'form': registrovaloremplo})

#===========================================================



def eliminar_valoracion(request,id_val):
    valoraciondeleteemplo=Diagnostico.objects.get(id_val=id_val)
    valoraciondeleteemplo.delete()
    return render(request,'listar_valoracionemplo.html')
