"""
URL configuration for proyecto project.
"""
from django.contrib import admin
from django.urls import path, include
from aplicacion import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Rutas del panel de administración de Django.
    path('accounts/', include('django.contrib.auth.urls')), # Rutas para autenticación de usuarios (login, logout, etc.).
    path('menu/', views.menu, name='menu'), # Ruta para la vista del menú de platillos.
    path('newPlatillo/', views.makePlatillo, name='newPlatillo'), # Ruta para crear un nuevo platillo.
    path('deletePlatillo/<int:platillo_id>/', views.deletePlatillo, name='deletePlatillo'), # Ruta para eliminar un platillo por ID.
    path('mapa/', views.mapa, name="mapa"), # Ruta para la vista del mapa.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Sirve archivos multimedia durante el desarrollo.