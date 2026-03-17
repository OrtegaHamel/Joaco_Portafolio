from django.shortcuts import render, get_object_or_404
from .models import Categoria, Proyecto, Perfil
from django.utils.translation import gettext_lazy as _
from django.utils import translation

def home(request):
    return render(request, 'sitioweb/home.html')

def categoria_detalle(request, slug):
    # 1. Obtenemos la categoría base por su slug
    categoria = get_object_or_404(Categoria, slug=slug)
    
    # 2. FILTRO CORREGIDO: Usamos 'categorias' (plural) que es el nuevo campo en el modelo
    proyectos = Proyecto.objects.filter(categorias=categoria)
    
    # 3. FILTRADO POR SUB-CATEGORÍA
    sub_cat = request.GET.get('sub_cat')
    valid_sub_cats = [choice[0] for choice in Proyecto.SUB_CATEGORIAS]
    
    if sub_cat in valid_sub_cats:
        proyectos = proyectos.filter(sub_categoria=sub_cat)
    
    # 4. ORDENAMIENTO
    orden = request.GET.get('orden')
    if orden == 'alfabetico':
        proyectos = proyectos.order_by('nombre')
    else:
        # Orden por defecto: los más nuevos primero
        proyectos = proyectos.order_by('-estreno_anio')

    sub_cats_traducidas = [
        (valor, _(etiqueta)) for valor, etiqueta in Proyecto.SUB_CATEGORIAS
    ]
    
    context = {
        'categoria': categoria,
        'proyectos': proyectos,
        'sub_cat_actual': sub_cat,
        'orden_actual': orden,
        'sub_categorias': sub_cats_traducidas,
    }
    return render(request, 'sitioweb/categoria_listado.html', context)

def proyecto_detalle(request, slug): # CAMBIO: Ahora recibe 'slug' en lugar de 'pk'
    # Buscamos por slug para tener URLs bonitas
    proyecto = get_object_or_404(Proyecto, slug=slug)
    capturas = proyecto.capturas.all() 
    
    return render(request, 'sitioweb/proyecto_detalle.html', {
        'proyecto': proyecto, 
        'capturas': capturas
    })

def about_me(request):
    perfil = Perfil.objects.first()
    return render(request, 'sitioweb/about.html', {
        'perfil': perfil
    })