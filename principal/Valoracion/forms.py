from django import forms
from .models import Diagnostico

class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Diagnostico  
        fields = ['diagnostico']  

    diagnostico = forms.CharField(label='Diagnóstico del vehículo') 
