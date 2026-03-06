import os
import sys

# Definimos la ruta de la app
path = '/home/joacofr/domains/joaco.fr/joaco_app'
if path not in sys.path:
    sys.path.append(path)

# El nombre de la carpeta donde está tu settings.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'portafolio.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
