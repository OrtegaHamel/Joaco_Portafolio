from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre-mi/', views.about_me, name='about_me'),
    path('categoria/<slug:slug>/', views.categoria_detalle, name='categoria_detalle'),
    path('proyecto/<slug:slug>/', views.proyecto_detalle, name='proyecto_detalle'),
]