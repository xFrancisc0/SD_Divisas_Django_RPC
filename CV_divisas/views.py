# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from xmlrpc.client import ServerProxy
from .models import sistema, usuario, conversion, informacion_moneda
from django import forms
from .forms import seleccion_listar_form, seleccion_listarparticular_form, realizar_compra_form, realizar_venta_form
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

def vender(request):
    client = ServerProxy('http://localhost:8000/rpc/')
    resulta = client.listdiv(1)
    return render(request,'vender.html',{'resulta':resulta})

def realizar_venta(request):

    if request.method == "POST":
        form = realizar_venta_form(request.POST)

        if form.is_valid():
            m_venta = form.cleaned_data['moneda_a_vender']
            cantidad = form.cleaned_data['cantidad']
            m_recibir = form.cleaned_data['desea_recibir']
            client = ServerProxy('http://localhost:8000/rpc/')
            #obtiene el resultado de llamar al metodo add
            str_m_vender = str(m_venta)
            int_cantidad = int(cantidad)
            str_m_recibir = str(m_recibir)
            print(str_m_vender,int_cantidad,str_m_recibir)
            resulta = client.div_sell(str_m_vender,int_cantidad,str_m_recibir)
            return redirect('vender')
    else:
        form = realizar_venta_form()
    context = {'form': form}
    return render(request, 'realizar_venta.html', context)

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

def listardivisasparticular(request):
    #se establece el metodo de respuesta
    if request.method == 'POST':
        #se crea un objeto de sumaForm
        form = seleccion_listarparticular_form(request.POST)
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
            resulta = client.listdivparticular(opcion)
            return render(request,'listardivisasparticular.html',{'form':form,'result':resulta,'opcion':opcion })
    else:

            form = seleccion_listarparticular_form()
    arg={'form':form,'opcion':2}
    return render(request,'listardivisasparticular.html',arg)