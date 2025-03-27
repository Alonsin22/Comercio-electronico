from django.contrib import admin

# Register your models here.
from .models import administrador

admin.site.register(administrador)

from .models import Platillo

admin.site.register(Platillo)