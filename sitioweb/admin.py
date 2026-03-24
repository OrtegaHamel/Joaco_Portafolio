from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline
from .models import Categoria, Proyecto, Captura, VideoProyecto, Perfil, CapturaPerfil, VideoPerfil
from django.forms import CheckboxSelectMultiple

class VideoInline(admin.TabularInline):
    model = VideoProyecto
    extra = 1

class CapturaInline(admin.TabularInline):
    model = Captura
    extra = 3 

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    inlines = [VideoInline, CapturaInline]
    save_on_top = True
    list_display = ('nombre', 'mostrar_categorias', 'sub_categoria', 'estreno_anio')
    list_filter = ('categorias', 'sub_categoria', 'estreno_anio')
    filter_horizontal = ('categorias',)
    prepopulated_fields = {'slug': ('nombre',)}

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "categorias":
            kwargs["widget"] = CheckboxSelectMultiple
        return super().formfield_for_manytomany(db_field, request, **kwargs)

    def mostrar_categorias(self, obj):
        return ", ".join([c.nombre for c in obj.categorias.all()])
    mostrar_categorias.short_description = 'Categorías'

# Categoria
@admin.register(Categoria)
class CategoriaAdmin(TranslationAdmin): # TranslationAdmin para ver los idiomas
    save_on_top = True
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)} # Esto ayuda a que el slug se escriba solo al poner el nombre

# Configuración del Perfil
class VideoPerfilInline(TranslationTabularInline):
    model = VideoPerfil
    extra = 1

class CapturaPerfilInline(admin.TabularInline):
    model = CapturaPerfil
    extra = 3

@admin.register(Perfil)
class PerfilAdmin(TranslationAdmin):
    inlines = [VideoPerfilInline, CapturaPerfilInline]
    save_on_top = True