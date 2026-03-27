import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns 

# 1. Rutas sin prefijo
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]

# 2. Rutas con prefijo
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('sitioweb.urls')),
    prefix_default_language=False
)

# 3. Archivos estáticos
# Permite que Django sirva archivos MEDIA durante el desarrollo
if settings.DEBUG or os.getenv('SERVIR_MEDIA_LOCAL') == 'True':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)