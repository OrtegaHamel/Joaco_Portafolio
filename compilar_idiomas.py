import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

try:
    call_command('compilemessages')
    print("Traducciones compiladas con éxito.")
except Exception as e:
    print(f"Error al compilar: {e}")