from django.db import models # Para definir modelos de datos
from PIL import Image # Para manipular imágenes
import re # Para expresiones regulares (limpiar nombres de archivos)
import os # Para operaciones con el sistema de archivos
import uuid # Para generar IDs únicos
from django.utils.text import slugify # Para generar slugs (nombres amigables para URLs)

# Función para limpiar nombres de archivos, genera un nombre único y seguro.
def clean_filename(filename):
    name, ext = os.path.splitext(filename) # Separa el nombre y la extensión
    name = slugify(name) # Convierte el nombre a un slug
    name = re.sub(r'[^a-z0-9]', '', name) # Elimina caracteres no alfanuméricos
    unique_id = uuid.uuid4().hex[:8] # Genera un ID único corto
    return f"{name}_{unique_id}.jpg" # Devuelve el nombre limpio con extensión .jpg

# Modelo para coordenadas, almacena latitud y longitud.
class cordenadas(models.Model):
    latitud = models.FloatField() # Campo para la latitud
    longitud = models.FloatField() # Campo para la longitud

    def __str__(self):
        return f"Lat: {self.latitud}, Lon: {self.longitud}" # Devuelve una representación en cadena

# Modelo para platillos, almacena información del platillo y su imagen.
class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=True) # Campo para el nombre del platillo
    descripcion = models.CharField(max_length=500, null=True) # Campo para la descripción
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True) # Campo para el precio
    foto = models.ImageField(upload_to='images/', height_field='imagen_altura', width_field='imagen_anchura', blank=True, null=True) # Campo para la imagen
    imagen_altura = models.PositiveIntegerField(blank=True, null=True) # Campo para la altura de la imagen
    imagen_anchura = models.PositiveIntegerField(blank=True, null=True) # Campo para el ancho de la imagen

    def save(self, *args, **kwargs):
        if self.foto:
            self.foto.name = clean_filename(self.foto.name) # Limpia el nombre del archivo de la imagen

        super().save(*args, **kwargs) # Guarda el modelo

        if self.foto:
            img = Image.open(self.foto.path) # Abre la imagen
            if img.mode != 'RGB' or img.height > 200 or img.width > 200: # Si no es RGB o es muy grande...
                img.thumbnail((200, 200)) # Redimensiona la imagen
                img = img.convert('RGB') # Convierte a RGB
                img.save(self.foto.path, 'JPEG') # Guarda la imagen redimensionada
            self.foto.name = os.path.splitext(self.foto.name)[0] + '.jpg' # Asegura la extensión .jpg
            super().save(*args, **kwargs) # Guarda el modelo de nuevo