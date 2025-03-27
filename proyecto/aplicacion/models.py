from django.db import models
from PIL import Image
import re
import os
import uuid
from django.utils.text import slugify

# Función para limpiar nombres de archivos, genera un nombre único y seguro.
def clean_filename(filename):
    name, ext = os.path.splitext(filename)
    name = slugify(name)
    name = re.sub(r'[^a-z0-9]', '', name)
    unique_id = uuid.uuid4().hex[:8]
    return f"{name}_{unique_id}.jpg"

# Modelo para administradores, almacena información básica.
class administrador(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField(max_length=60)
    contraseña = models.CharField(max_length=128) # Contraseña almacenada (debe ser hash).

# Modelo para coordenadas, almacena latitud y longitud.
class cordenadas(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return f"Lat: {self.latitud}, Lon: {self.longitud}" # Devuelve un string, no un dict.

# Modelo para platillos, almacena información del platillo y su imagen.
class Platillo(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    foto = models.ImageField(upload_to='images/', height_field='imagen_altura', width_field='imagen_anchura', blank=True, null=True)
    imagen_altura = models.PositiveIntegerField(blank=True, null=True)
    imagen_anchura = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.foto:
            self.foto.name = clean_filename(self.foto.name) # Limpia el nombre del archivo.

        super().save(*args, **kwargs)

        if self.foto:
            img = Image.open(self.foto.path)
            if img.mode != 'RGB' or img.height > 200 or img.width > 200:
                img.thumbnail((200, 200)) # Redimensiona la imagen.
                img = img.convert('RGB') # Convierte a RGB.
                img.save(self.foto.path, 'JPEG')
            self.foto.name = os.path.splitext(self.foto.name)[0] + '.jpg' # Asegura extensión .jpg.
            super().save(*args, **kwargs)