from modernrpc.core import rpc_method
from .models import sistema, usuario, conversion, informacion_moneda
from django.db.models import F

@rpc_method
def listdivparticular(opcion_div):
    if(opcion_div == 1):
        lista_ob =list(informacion_moneda.objects.all().filter(id_moneda=1))
    elif(opcion_div == 2):
        lista_ob =list(informacion_moneda.objects.all().filter(id_moneda=2))
    else:
        lista_ob =list(informacion_moneda.objects.all().filter(id_moneda=3))
    return lista_ob

@rpc_method
def listdiv(opcion_div):
    if(opcion_div == 1):
        lista_ob =list(usuario.objects.all())
    elif(opcion_div == 2):
        lista_ob =list(sistema.objects.all())
    else:
        lista_ob =list(conversion.objects.all())
    return lista_ob

@rpc_method
def div_buy(m_comprar, cantidad, m_pagar):
    print("rpc "+m_comprar, cantidad, m_pagar)
    conversiones = conversion.objects.get(tipo_moneda_buscada=m_comprar, tipo_moneda_encontrada=m_pagar)
    if(conversiones):
        #obtenemos el valor de la conversion
        valores=str(conversiones.valor_conversion())
        #calculamos la tasa de cambio
        tasa= float(valores)*cantidad
        print(tasa)
        #buscamos el tiṕo de moneda que se comprara del sistema
        sis_update_entrega=sistema.objects.filter(tipo_moneda=m_comprar).update(cantidad_moneda=F('cantidad_moneda')-cantidad)

        #buscamos el tipo moneda que recibe el sistema por la compra

        sis_update_recibe=sistema.objects.filter(tipo_moneda=m_pagar).update(cantidad_moneda=F('cantidad_moneda')+tasa)


        #buscamos el tiṕo de moneda que se comprara del sistema

        user_update_recibe=usuario.objects.filter(tipo_moneda=m_comprar).update(cantidad_moneda=F('cantidad_moneda')+cantidad)

        #buscamos el tipo moneda que recibe el sistema por la compra

        user_update_entrega=usuario.objects.filter(tipo_moneda=m_pagar).update(cantidad_moneda=F('cantidad_moneda')-tasa)


    else:
        print("no hay nada en la bd")
        tasa="No encontrada"
    return tasa

@rpc_method
def div_sell(m_venta, cantidad, m_recibir):

    conversiones = conversion.objects.get(tipo_moneda_buscada=m_venta, tipo_moneda_encontrada=m_recibir)
    if(conversiones):
        #obtenemos el valor de la conversion
        valores=str(conversiones.valor_conversion())
        #calculamos la tasa de cambio
        tasa= float(valores)*cantidad
        print(tasa)
        #buscamos el tiṕo de moneda que recibira  el sistema por la venta
        sis_update_recibe=sistema.objects.filter(tipo_moneda=m_venta).update(cantidad_moneda=F('cantidad_moneda')+cantidad)

        #buscamos el tipo moneda que el sistema pagara

        sis_update_entrega=sistema.objects.filter(tipo_moneda=m_recibir).update(cantidad_moneda=F('cantidad_moneda')-tasa)


        #buscamos el tiṕo de moneda que se vendera al sistema

        user_update_entrega=usuario.objects.filter(tipo_moneda=m_venta).update(cantidad_moneda=F('cantidad_moneda')-cantidad)

        #buscamos el tipo moneda que recibe el sistema por la compra

        user_update_recibe=usuario.objects.filter(tipo_moneda=m_recibir).update(cantidad_moneda=F('cantidad_moneda')+tasa)


    else:
        print("no hay nada en la bd")
        tasa="No encontrada"
    return tasa
