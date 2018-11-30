# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from xmlrpc.client import ServerProxy
from .models import sistema, usuario, conversion, informacion_moneda
from django import forms
from .forms import seleccion_listar_form, realizar_compra_form

# Create your views here.

def index(request):
   	return render(request,'index.html')


def comprar(request):

    client = ServerProxy('http://localhost:8000/rpc/')
    resulta = client.listdiv(1)
    return render(request,'comprar.html',{'resulta':resulta})

def realizar_compra(request):

    if request.method == "POST":
        form = realizar_compra_form(request.POST)

        if form.is_valid():
            m_comprar = form.cleaned_data['moneda_a_comprar']
            cantidad = form.cleaned_data['cantidad']
            m_pagar = form.cleaned_data['pagara_con']
            client = ServerProxy('http://localhost:8000/rpc/')
            #obtiene el resultado de llamar al metodo add
            str_m_comprar = str(m_comprar)
            int_cantidad = int(cantidad)
            str_m_pagar = str(m_pagar)
            print(str_m_comprar,int_cantidad,str_m_pagar)
            resulta = client.div_buy(str_m_comprar,int_cantidad,str_m_pagar)
            return redirect('comprar')
    else:
        form = realizar_compra_form()
    context = {'form': form}
    return render(request, 'realizar_compra.html', context)


def listardivisas(request):
    #se establece el metodo de respuesta
    if request.method == 'POST':
        #se crea un objeto de sumaForm
        form = seleccion_listar_form(request.POST)
        #se verifica que el formulario sea valido
        if form.is_valid():
            #obtiene los datos ingresados por el formulario
            lista = form.cleaned_data['elija_opcion']

            #Transforma los datos a
            opcion=int(lista)

            #{'form':form,'mydata':data1}
            #Crea un objeto remoto
            client = ServerProxy('http://localhost:8000/rpc/')
            #obtiene el resultado de llamar al metodo add
            resulta = client.listdiv(opcion)
            return render(request,'listardivisas.html',{'form':form,'result':resulta,'opcion':opcion })
    else:

            form = seleccion_listar_form()
    arg={'form':form,'opcion':2}
    return render(request,'listardivisas.html',arg)
