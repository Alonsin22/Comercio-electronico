"""
URL configuration for proyecto project.
"""
from django.contrib import admin # Para el panel de administración de Django
from django.urls import path, include # Para definir las rutas de la aplicación
from aplicacion import views # Importamos las vistas de nuestra aplicación
from django.conf import settings # Para configuraciones del proyecto
from django.conf.urls.static import static # Para servir archivos estáticos (imágenes, etc.)
from django.contrib.auth import views as auth_views # Para las vistas de autenticación de Django

urlpatterns = [
    path('admin/', admin.site.urls), # Rutas del panel de administración de Django.
    path('accounts/', include('django.contrib.auth.urls')), # Rutas para autenticación de usuarios (login, logout, etc.).
    path('menu/', views.menu, name='menu'), # Ruta para la vista del menú de platillos.
    path('catalogo/', views.catalogo, name='catalogo'), # Ruta para la vista del catalogo de platillos.
    path('newPlatillo/', views.makePlatillo, name='newPlatillo'), # Ruta para crear un nuevo platillo.
    path('deletePlatillo/<int:producto_id>/', views.deletePlatillo, name='deletePlatillo'), # Ruta para eliminar un platillo por ID.
    path('mapa/', views.mapa, name="mapa"), # Ruta para la vista del mapa.
    path('add/<int:producto_id>', views.agregarCar, name="add"), # Ruta para agregar un producto al carrito.
    path('more/<int:producto_id>', views.aumentarCar, name="more"), # Ruta para aumentar la cantidad de un producto en el carrito.
    path('delete/<int:producto_id>', views.eliminarCar, name="delete"), # Ruta para eliminar un producto del carrito.
    path('rest/<int:producto_id>', views.RestarCar, name="rest"), # Ruta para restar la cantidad de un producto en el carrito.
    path('clean/', views.limpiarCar, name="rest"), # Ruta para limpiar el carrito.
    path('carrito/', views.carrito, name="carrito"), # Ruta para ver el carrito.
    path('buscador/', views.buscador, name="buscador"), # Ruta para la vista del buscador.
]
if settings.DEBUG: # Si estamos en modo de desarrollo...
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Servimos los archivos multimedia