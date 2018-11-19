# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class sistema(models.Model):
	id_sistema = models.IntegerField(primary_key=True)
	tipo_moneda = models.CharField(max_length=3, blank=False, null=False, db_column='tipo_moneda', verbose_name ='tipo_moneda')
	cantidad_moneda = models.IntegerField(db_column='cantidad_moneda', verbose_name ='cantidad_moneda')
	def __str__(self):
		return str(self.tipo_moneda)
class usuario(models.Model):
	id_usuario = models.IntegerField(primary_key=True)
	tipo_moneda = models.CharField(max_length=3, blank=False, null=False, db_column='tipo_moneda', verbose_name ='tipo_moneda')
	cantidad_moneda = models.IntegerField(db_column='cantidad_moneda', verbose_name ='cantidad_moneda')
	def __str__(self):
		return str(self.tipo_moneda) 
class conversion(models.Model):
	id_conversion = models.IntegerField(primary_key=True)
	tipo_moneda_buscada = models.CharField(max_length=3, blank=False, null=False, db_column='tipo_moneda_buscada', verbose_name ='tipo_moneda_buscada')
	tipo_moneda_encontrada = models.CharField(max_length=3, blank=False, null=False, db_column='tipo_moneda_encontrada', verbose_name ='tipo_moneda_encontrada')
	cantidad_encontrada = models.IntegerField(db_column='cantidad_encontrada', verbose_name ='cantidad_encontrada')

class informacion_moneda(models.Model):
	id_moneda = models.IntegerField(primary_key=True)
	tipo_moneda = models.CharField(max_length=3, blank=False, null=False, db_column='tipo_moneda', verbose_name ='tipo_moneda')
	nombre = models.CharField(max_length=20, blank=False, null=False, db_column='nombre', verbose_name ='nombre')
	pais = models.IntegerField(db_column='pais', verbose_name ='pais')
	anio_creacion = models.IntegerField(db_column='anio_creacion', verbose_name ='anio_creacion')
