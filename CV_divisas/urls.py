from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url('index/', views.index, name='index'),
    url('comprar/', views.comprar, name='comprar'),
	url('vender/',views.vender,name='vender'),
	url('realizar_compra/',views.realizar_compra, name='realizar_compra'),
	url('realizar_venta/',views.realizar_venta, name='realizar_venta'),
    url('listardivisas/', views.listardivisas, name='listardivisas'),
    url('listardivisasparticular/', views.listardivisasparticular, name='listardivisasparticular')
]
