from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Categoria, Proyecto, Captura, VideoProyecto, Perfil, CapturaPerfil, VideoPerfil

class VideoInline(admin.TabularInline):
    model = VideoProyecto
    extra = 1

class CapturaInline(admin.TabularInline):
    model = Captura
    extra = 3 # Te mostrará 3 espacios vacíos para subir fotos de una vez

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    inlines = [VideoInline,CapturaInline]
    list_display = ('nombre', 'categoria')
    list_filter = ('categoria',)

admin.site.register(Categoria)


# El Inline ahora permite campos traducidos
class VideoPerfilInline(TranslationTabularInline):
    model = VideoPerfil
    extra = 1

class CapturaPerfilInline(admin.TabularInline):
    model = CapturaPerfil
    extra = 3

@admin.register(Perfil)
class PerfilAdmin(TranslationAdmin):
    inlines = [VideoPerfilInline, CapturaPerfilInline]