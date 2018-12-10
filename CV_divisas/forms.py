from django import forms
from .models import usuario, sistema, conversion


#formulario utlizado en listardivisas.html
class seleccion_listar_form(forms.Form):
    CHOICES=(('1','usuario'),('2','sistema'),('3','conversion'))
    elija_opcion = forms.ChoiceField(choices=CHOICES)
#formulario utilizado en realizar_compra.html
class realizar_compra_form(forms.Form):
    moneda_a_comprar = forms.ModelChoiceField(queryset=sistema.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField()
    pagara_con =forms.ModelChoiceField(queryset=usuario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
#fomulario utilzado en realizar_venta.html
class realizar_venta_form(forms.Form):
    moneda_a_vender = forms.ModelChoiceField(queryset=sistema.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField()
    desea_recibir =forms.ModelChoiceField(queryset=usuario.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
#fomulario utilzado en listardivisasparticular.html
class seleccion_listarparticular_form(forms.Form):
    CHOICES=(('1','CLP'),('2','USD'),('3','EUR'))
    elija_opcion = forms.ChoiceField(choices=CHOICES)
