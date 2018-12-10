from modernrpc.core import rpc_method
from .models import sistema, usuario, conversion, informacion_moneda
from django.db.models import F

#metodo rpc que segun la opcion dada selecciona devuelve la lista correspondiente
#recibe la opcion_div que corresponde a la opcion que se desea listar
#retona la lista que selecciono
@rpc_method
def listdivparticular(opcion_div):
    if(opcion_div == 1):
        lista_ob =list(informacion_moneda.objects.all().filter(id_moneda=1))
    elif(opcion_div == 2):
        lista_ob =list(informacion_moneda.objects.all().filter(id_moneda=2))
    else:
        lista_ob =list(informacion_moneda.objects.all().filter(id_moneda=3))
    return lista_ob

#metodo rpc que segun la opcion dada selecciona devuelve la lista correspondiente
#recibe la opcion_div que corresponde a la opcion que se desea listar
#retona la lista que selecciono
@rpc_method
def listdiv(opcion_div):
    #si la opcion es 1 se retornara la lista de los datos del usuario
    if(opcion_div == 1):
        lista_ob =list(usuario.objects.all())
    #si la opcion es 2 se retornara los datos del sistema
    elif(opcion_div == 2):
        lista_ob =list(sistema.objects.all())
    #si la opcion es otra se retornara la tasas de converiones
    else:
        lista_ob =list(conversion.objects.all())
    #retonamos la lista seleccionda
    return lista_ob

#metodo rpc que realiza las compras de divisas
#recibe: m_comprar que es la moneda a comprar, cantidad que es la cantidad que se comprara, y m_pagar que el tipo de moneda con el que sea pagara
#retorna si es que se realizo la compra con exito o no
@rpc_method
def div_buy(m_comprar, cantidad, m_pagar):
    print("rpc "+m_comprar, cantidad, m_pagar)
    #buscamos con m_compra y m_pagar la tasa de conversion entre estos tipos de moneda
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
#metodo rpc que realiza las ventas de divisas
#recibe: m_venta que corresponde a la moneda que se vendera, cantidad que corresponde a la cantidad que se vendera, y m_recibir que corresponde a el tipo de moneda que se desea recibir por la venta
#retorna si es que la venta se ha realizado con exito
@rpc_method
def div_sell(m_venta, cantidad, m_recibir):
    #buscamos en la base de datos la tasa de conversion con m_venta y m_recibir
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
