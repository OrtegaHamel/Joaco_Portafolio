from django.shortcuts import render, get_object_or_404 #Bedford_or_404
from .models import Categoria, Proyecto, Perfil

def home(request):
    # Esta vista solo renderiza la ilustración inicial
    return render(request, 'sitioweb/home.html')

def categoria_detalle(request, slug):
    # Buscamos la categoría por su slug (ej: 'colorista')
    categoria = get_object_or_404(Categoria, slug=slug)
    
    # Filtramos los proyectos que pertenecen a esa categoría
    proyectos = Proyecto.objects.filter(categoria=categoria)
    
    context = {
        'categoria': categoria,
        'proyectos': proyectos,
    }
    return render(request, 'sitioweb/categoria_listado.html', context)

def proyecto_detalle(request, pk):
    # pk es el ID único del proyecto
    proyecto = get_object_or_404(Proyecto, pk=pk)
    # Obtenemos todas las capturas relacionadas a este proyecto
    capturas = proyecto.capturas.all() 
    
    return render(request, 'sitioweb/proyecto_detalle.html', {
        'proyecto': proyecto, 
        'capturas': capturas
    })

def about_me(request):
    perfil = Perfil.objects.first() # Trae el perfil de Joaco
    return render(request, 'sitioweb/about.html', {
        'perfil': perfil
    })