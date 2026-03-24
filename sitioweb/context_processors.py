from .models import Categoria

def categorias_nav(request):
    return {
        'categorias_globales': Categoria.objects.all()
    }