import polib
import os

# Rutas a tus archivos manuales
files = [
    'locale/en/LC_MESSAGES/django.po',
    'locale/fr/LC_MESSAGES/django.po'
]

for f in files:
    if os.path.exists(f):
        po = polib.pofile(f)
        po.save_as_mofile(f.replace('.po', '.mo'))
        print(f"Éxito: Se ha creado el archivo binario para {f}")
    else:
        print(f"Error: No se encontró el archivo en {f}")