from django.shortcuts import render, get_object_or_404 #Bedford_or_404
from .models import Categoria, Proyecto, Perfil
from django.utils.translation import gettext_lazy as _

def home(request):
    # Esta vista solo renderiza la ilustración inicial
    return render(request, 'sitioweb/home.html')

def categoria_detalle(request, slug):
    # 1. Obtenemos la categoría base
    categoria = get_object_or_404(Categoria, slug=slug)
    
    # 2. Filtramos los proyectos que pertenecen a esa categoría
    proyectos = Proyecto.objects.filter(categoria=categoria)
    
    # 3. FILTRADO POR SUB-CATEGORÍA
    # Capturamos el parámetro 'sub_cat' de la URL (ej: ?sub_cat=ficcion)
    sub_cat = request.GET.get('sub_cat')
    valid_sub_cats = [choice[0] for choice in Proyecto.SUB_CATEGORIAS] # ['ficcion', 'documental', etc.]
    
    if sub_cat in valid_sub_cats:
        proyectos = proyectos.filter(sub_categoria=sub_cat)
    
    # 4. ORDENAMIENTO
    # Capturamos el parámetro 'orden' de la URL (ej: ?orden=alfabetico)
    orden = request.GET.get('orden')
    
    if orden == 'alfabetico':
        proyectos = proyectos.order_by('nombre')
    elif orden == 'fecha':
        proyectos = proyectos.order_by('-estreno_anio')
    else:
        # Orden por defecto: los más nuevos primero
        proyectos = proyectos.order_by('-estreno_anio')
    
    # 5. CONTEXTO
    context = {
        'categoria': categoria,
        'proyectos': proyectos,
        'sub_cat_actual': sub_cat,
        'orden_actual': orden,
        'sub_categorias': Proyecto.SUB_CATEGORIAS, # Para armar el menú en el HTML
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