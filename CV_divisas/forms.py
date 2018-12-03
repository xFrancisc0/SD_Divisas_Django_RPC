from django import forms
from .models import usuario, sistema, conversion



class seleccion_listar_form(forms.Form):
    CHOICES=(('1','usuario'),('2','sistema'),('3','conversion'))
    elija_opcion = forms.ChoiceField(choices=CHOICES)

class realizar_compra_form(forms.Form):
    moneda_a_comprar = forms.ModelChoiceField(queryset=sistema.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField()
    pagara_con =forms.ModelChoiceField(queryset=usuario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))

class realizar_venta_form(forms.Form):
    moneda_a_vender = forms.ModelChoiceField(queryset=sistema.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField()
    desea_recibir =forms.ModelChoiceField(queryset=usuario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
