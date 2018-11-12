# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from xmlrpc.client import ServerProxy
from .models import sistema, usuario, conversion, informacion_moneda

# Create your views here.

def index(request):
   	return render(request,'index.html')


def comprar(request):
	return render(request,'comprar.html')

def listardivisas(request):
    client = ServerProxy('http://localhost:8000/rpc/')
    result = client.listdiv()
    return  render(request,'listardivisas.html',{'result':result})
