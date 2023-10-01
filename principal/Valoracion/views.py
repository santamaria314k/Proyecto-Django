from django.http import HttpRequest
from django.shortcuts import render
from .forms import ValoracionForm
from .models import Diagnostico

# Create your views here.


#CREAR EL DIAGNOTICO DE UN VEHICULO___________________________________________

def RegistroValoracion(request): 
    registrovalor=ValoracionForm()
    return render(request,'registro_valoracion.html',{'form':registrovalor})

def Guardar_Valoracion(request):
    if request.method == 'POST':
        registrovalor = ValoracionForm(request.POST)
        if registrovalor.is_valid():
            # Guardar el diagnóstico en la base de datos
            diagnostico_text = registrovalor.cleaned_data['diagnostico']
            diagnostico = Diagnostico(diagnostico=diagnostico_text)
            diagnostico.save()
    return render(request,'registro_valoracion.html',{'form':registrovalor,"mensaje":'valoracion-registrada'},)



#MOSTRAR LOSDIAGNOSTICOS_____________________________________________
def ListarValoracion(request):
    listadoDiagnosticos=Diagnostico.objects.all()
    return render ( request,'listar_valoracion.html',{'listadoDiagnosticos':listadoDiagnosticos})