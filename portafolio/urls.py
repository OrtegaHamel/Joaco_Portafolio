from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns #Permite configuración para los idiomas

# 1. Rutas que NO llevan prefijo de idioma (Admin e idioma interno)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')), # Esto permite que los botones de idioma funcionen
]

# 2. Rutas que SÍ llevan prefijo (/es/, /en/, /fr/)
urlpatterns += i18n_patterns(
    path('', include('sitioweb.urls')),
    # Si en el futuro agregas más apps que se traduzcan, van aquí
)

# 3. Configuración para ver las fotos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
