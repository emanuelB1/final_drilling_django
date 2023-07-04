from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add', views.vehiculo_create, name='vehiculo_add'),
    path('listar/', views.vehiculo_list, name='listar'),
    path('registro/', views.registro_view, name="registro"),
    path('login/', views.login_view, name="login"),
    path('logot/', views.logout_view, name="logout")
]
