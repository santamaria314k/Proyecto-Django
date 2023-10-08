from django import forms
from .models import Garantias,TiposGarantia


class TiposGarantiaForm(forms.ModelForm):
    class Meta:
        model = TiposGarantia
        fields = ['nombre']






class GarantiasForm(forms.ModelForm):
    class Meta:
        model = Garantias
        fields = ['fechaInicio', 'fechaFin', 'id_serveh', 'id_tiga']


