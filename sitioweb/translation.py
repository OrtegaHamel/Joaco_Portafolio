from modeltranslation.translator import register, TranslationOptions
from .models import Categoria, Proyecto, Perfil, VideoPerfil

@register(Categoria)
class CategoriaTranslationOptions(TranslationOptions):
    fields = ('nombre',) # El slug no suele traducirse para no romper links

@register(Proyecto)
class ProyectoTranslationOptions(TranslationOptions):
    fields = ('nombre', 'tagline', 'descripcion', 'ficha_tecnica') # La URL de video y la imagen son iguales para todos los idiomas
    
@register(Perfil)
class PerfilTranslationOptions(TranslationOptions):
    fields = ('nombre', 'bio_introduccion', 'bio_detallada')

@register(VideoPerfil)
class VideoPerfilTranslationOptions(TranslationOptions):
    fields = ('titulo_video',)