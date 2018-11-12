from modernrpc.core import rpc_method
from .models import sistema, usuario, conversion


@rpc_method
def listdiv():
    lista_ob =list(sistema.objects.all())


    return lista_ob
