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

"""
Funcion de compras: Es utilzada por realizar_compra
-recibe la request
-retorna el render de comprar.html
"""
def comprar(request):

    client = ServerProxy('http://localhost:8000/rpc/')
    resulta = client.listdiv(1)
    return render(request,'comprar.html',{'resulta':resulta})
"""
Funcion realizar_compra: funcion principal para la realizacion de compras
-recibe la request
-retorna un redirect a la funcion compra en caso de que la request recibido sea POST o un render de realizar_compra.html en caso contrario
"""
def realizar_compra(request):
    #si el metodo de la request es un POST
    if request.method == "POST":
        #creamos un form con los datos entregados en realizar_compra.html
        form = realizar_compra_form(request.POST)
        #si es valido continuamos con la operacion
        if form.is_valid():
            #limpiamos los datos recibbidos del html
            m_comprar = form.cleaned_data['moneda_a_comprar']
            cantidad = form.cleaned_data['cantidad']
            m_pagar = form.cleaned_data['pagara_con']
            #realizamos la conexion con el servidor rpc
            client = ServerProxy('http://localhost:8000/rpc/')
            #realizamos la conversion de los datos a los tipos que necesitamos enviar
            str_m_comprar = str(m_comprar)
            int_cantidad = int(cantidad)
            str_m_pagar = str(m_pagar)
            print(str_m_comprar,int_cantidad,str_m_pagar)
            #enviamos los datos al metodo RPC div.buy en rpc_methods.py
            resulta = client.div_buy(str_m_comprar,int_cantidad,str_m_pagar)
            return redirect('comprar')
    else:
        form = realizar_compra_form()
    context = {'form': form}
    return render(request, 'realizar_compra.html', context)
"""
Funcion de ventas: Es utilzada por realizar_venta
-recibe la request
-retorna el render de vender.html
"""
def vender(request):
    client = ServerProxy('http://localhost:8000/rpc/')
    resulta = client.listdiv(1)
    return render(request,'vender.html',{'resulta':resulta})
"""
Funcion realizar_venta: funcion principal para la realizacion de ventas
-recibe la request
-retorna un redirect a la funcion venta en caso de que la request recibido sea POST o un render de realizar_venta.html en caso contrario
"""
def realizar_venta(request):
#si el metodo de la request es un POST
    if request.method == "POST":
        form = realizar_venta_form(request.POST)
        #creamos un form con los datos entregados en realizar_venta.html
        if form.is_valid():
            #limpiamos los datos recibbidos del html
            m_venta = form.cleaned_data['moneda_a_vender']
            cantidad = form.cleaned_data['cantidad']
            m_recibir = form.cleaned_data['desea_recibir']
            #realizamos la conexion con el servidor rpc
            client = ServerProxy('http://localhost:8000/rpc/')
            #realizamos la conversion de los datos a los tipos que necesitamos enviar
            str_m_vender = str(m_venta)
            int_cantidad = int(cantidad)
            str_m_recibir = str(m_recibir)
            print(str_m_vender,int_cantidad,str_m_recibir)
            #enviamos los datos al metodo RPC div.buy en rpc_methods.py
            resulta = client.div_sell(str_m_vender,int_cantidad,str_m_recibir)
            return redirect('vender')
    else:
        form = realizar_venta_form()
    context = {'form': form}
    return render(request, 'realizar_venta.html', context)
"""
Metodo para listar las diferentes divisas ya sea la del cliente, la del sistema o las converiones de las monedas
-Recibe la request
-Retorna el render de listardivisas.html con los datos de la opcion seleccionada.
"""
def listardivisas(request):
    #se establece el metodo de respuesta
    if request.method == 'POST':
        #se crea un objeto de seleccion_listar_form
        form = seleccion_listar_form(request.POST)
        #se verifica que el formulario sea valido
        if form.is_valid():
            #obtiene los datos ingresados por el formulario
            lista = form.cleaned_data['elija_opcion']

            #Transforma los datos a
            opcion=int(lista)

            #Crea un objeto remoto
            client = ServerProxy('http://localhost:8000/rpc/')
            #obtiene el resultado de llamar al metodo listdiv
            resulta = client.listdiv(opcion)
            return render(request,'listardivisas.html',{'form':form,'result':resulta,'opcion':opcion })
    else:

            form = seleccion_listar_form()
    arg={'form':form,'opcion':2}
    return render(request,'listardivisas.html',arg)

"""
Metodo para listar la informacion de forma detallada de las distintas divisas
-Recibe la request
-Retorna el render de listardivisasparticular.html.html con los datos de la opcion seleccionada.
"""
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
            #obtiene el resultado de llamar al metodo listdivparticular
            resulta = client.listdivparticular(opcion)
            return render(request,'listardivisasparticular.html',{'form':form,'result':resulta,'opcion':opcion })
    else:

            form = seleccion_listarparticular_form()
    arg={'form':form,'opcion':2}
    return render(request,'listardivisasparticular.html',arg)
