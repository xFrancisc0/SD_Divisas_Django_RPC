from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url('index/', views.index, name='index'),
    url('comprar/', views.comprar, name='comprar'),
	url('realizar_compra/',views.realizar_compra, name='realizar_compra'),
    url('listardivisas/', views.listardivisas, name='listardivisas')
]
