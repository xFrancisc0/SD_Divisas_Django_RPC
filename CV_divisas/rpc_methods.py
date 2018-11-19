from modernrpc.core import rpc_method
from .models import sistema, usuario, conversion


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
def div_buy(m_comprar, cantidad,m_pagar):
    conversiones = conversion.objects.all()
    if(conversion):
        valores = conversiones.filter(tipo_moneda_buscada=m_comprar, tipo_moneda_encontrada=m_pagar)
        tasa= float(valores['cantidad_encontrada'])*float(cantidad)
    else:
        tasa="No encontrada"
    return tasa
