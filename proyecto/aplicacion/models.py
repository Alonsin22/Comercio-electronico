from django.db import models
from PIL import Image
import re
import os
import uuid
from django.utils.text import slugify



def clean_filename(filename):
    name, ext = os.path.splitext(filename)
    name = slugify(name) 
    name = re.sub(r'[^a-z0-9]', '', name)  
    unique_id = uuid.uuid4().hex[:8] 
    return f"{name}_{unique_id}.jpg"

class administrador(models.Model):
    nombre = models.CharField(max_length = 60)
    correo = models.EmailField(max_length = 60)
    contraseña = models.CharField(max_length = 128)

class cordenadas(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return ( {'latitud':self.latitud, 'lon':self.longitud})

class Platillo(models.Model):
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    foto = models.ImageField(
        upload_to='images/', 
        height_field='imagen_altura', 
        width_field='imagen_anchura',
        blank=True,
        null=True
    )
    imagen_altura = models.PositiveIntegerField(blank=True, null=True)
    imagen_anchura = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Limpiar el nombre del archivo de la foto antes de guardarlo
        if self.foto:
            cleaned_filename = clean_filename(self.foto.name)
            self.foto.name = cleaned_filename

        super().save(*args, **kwargs)

        img = Image.open(self.foto.path)

        # Convertir la imagen a JPEG y redimensionarla si es necesario
        if img.mode != 'RGB' or img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            
            # Convertir la imagen a formato RGB antes de guardarla como JPEG
            img = img.convert('RGB')
            img.save(self.foto.path, 'JPEG')

            # Actualizar la extensión del archivo en el modelo
            self.foto.name = os.path.splitext(self.foto.name)[0] + '.jpg'
            super().save(*args, **kwargs)