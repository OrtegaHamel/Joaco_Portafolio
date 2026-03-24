from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class Categoria(models.Model):
    # Realizador, Director de Foto, Colorista
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) # Para URLs amigables
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción de la categoría")

    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    categorias = models.ManyToManyField(Categoria, related_name='proyectos', verbose_name="Categorías")
    SUB_CATEGORIAS = [
        ('ficcion', _('Ficción')),
        ('documental', _('Documental')),
        ('videoclip', _('Videoclip')),
        ('experimental', _('Experimental')),
    ]
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    sub_categoria = models.CharField(
        max_length=20,
        choices=SUB_CATEGORIAS,
        default='ficcion',
        verbose_name="Sub-categoría"
    )
    tagline = models.CharField(max_length=150, blank=True, null=True, default="")
    ficha_tecnica = models.TextField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True) # Opcional
    miniatura = models.ImageField(upload_to='proyectos/miniaturas/')
    estreno_anio = models.PositiveIntegerField(
        verbose_name="Año de estreno",
        validators=[
            MinValueValidator(1900), 
            MaxValueValidator(datetime.date.today().year + 5)
        ],
        help_text="Ingrese el año en formato YYYY",
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['-estreno_anio'] # Orden por defecto: más nuevos primero

    def __str__(self):
        return self.nombre
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

class Captura(models.Model):
    # Esto permite que un Proyecto tenga "varias capturas de pantalla"
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='capturas')
    imagen = models.ImageField(upload_to='proyectos/capturas/')

    def __str__(self):
        return f"Captura de {self.proyecto.nombre}"

# MODELO PARA VIDEOS MÚLTIPLES
class VideoProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='videos', on_delete=models.CASCADE)
    url_video = models.URLField(help_text="Pega el link de YouTube o Vimeo")
    titulo_video = models.CharField(max_length=200, blank=True, null=True, help_text="Opcional: Ej. Trailer, Detrás de escena")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = "Videos"

# MODELOS PARA LA SECCIÓN "ABOUT"
class Perfil(models.Model):
    nombre = models.CharField(max_length=200, default="Joaco")
    foto_perfil = models.ImageField(upload_to='perfil/foto/', blank=True, null=True)
    bio_introduccion = models.TextField(blank=True, null=True) # Similar a ficha_tecnica
    bio_detallada = models.TextField(blank=True, null=True)     # Similar a descripcion
    email_contacto = models.EmailField(blank=True, null=True, verbose_name="Correo electrónico")
    whatsapp_numero = models.CharField(max_length=20, blank=True, null=True, verbose_name="WhatsApp")
    cv_pdf = models.FileField(upload_to='documentos/', blank=True, null=True, verbose_name="CV en PDF")
    def __str__(self):
        return self.nombre

class CapturaPerfil(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='capturas')
    imagen = models.ImageField(upload_to='perfil/capturas/')

class VideoPerfil(models.Model):
    perfil = models.ForeignKey(Perfil, related_name='videos', on_delete=models.CASCADE)
    url_video = models.URLField(help_text="Link de YouTube o Vimeo")
    titulo_video = models.CharField(max_length=200, blank=True, null=True)