from django.contrib.auth.decorators import login_required # Importamos un decorador para proteger vistas
from django.shortcuts import render, redirect # Importamos funciones para renderizar plantillas y redirigir
from django.http import HttpResponse # Importamos para respuestas HTTP directas (no se usa aquí)
from .models import Producto, cordenadas # Importamos nuestros modelos
from django.contrib import messages # Importamos para mostrar mensajes al usuario
from aplicacion.carrito import Carrito # Importamos nuestra clase Carrito
from django.db.models import Q # Importamos para hacer consultas complejas

# Vista para crear un nuevo producto (requiere inicio de sesión).
@login_required # Solo usuarios logueados pueden usar esta vista
def makePlatillo(req):
    if req.method == "POST": # Si recibimos datos de un formulario...
        nombre = req.POST.get('nombre') # Obtenemos el nombre del producto
        descripcion = req.POST.get('descripcion') # Obtenemos la descripción
        foto = req.FILES.get('foto') # Obtenemos la foto (si la hay)
        precio = req.POST.get('precio') # Obtenemos el precio

        nuevo_producto = Producto(nombre=nombre, descripcion=descripcion, foto=foto, precio=precio) # Creamos un nuevo producto
        nuevo_producto.save() # Guardamos el producto en la base de datos
        messages.success(req, f"El producto '{nombre}' ha sido registrado exitosamente.") # Mensaje de éxito
        return redirect('menu') # Redirigimos al menú

    return render(req, "../templates/aplicacion/formulario.html") # Mostramos el formulario

# Vista para eliminar un producto por su ID.
def deletePlatillo(req, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id) # Buscamos el producto
        producto.delete() # Lo eliminamos
        messages.success(req, f"El producto '{producto.nombre}' ha sido eliminado exitosamente.") # Mensaje de éxito
    except Producto.DoesNotExist: # Si el producto no existe...
        messages.error(req, "El Producto que intentas eliminar no existe.") # Mensaje de error
    return redirect('menu') # Redirigimos al menú

# Vista para mostrar el menú de platillos.
def menu(req):
    productos = Producto.objects.all() # Obtenemos todos los productos
    return render(req, '../templates/aplicacion/formulario.html', {'productos': productos}) # Mostramos el menú

def catalogo(req):
    productos = Producto.objects.all() # Obtenemos todos los productos
    return render(req, '../templates/aplicacion/catalogo.html', {'productos': productos}) # Mostramos el catálogo

# Vista para mostrar un mapa y guardar coordenadas.
def mapa(req):
    lat = None # Inicializamos latitud
    lon = None # Inicializamos longitud

    if req.method == "POST": # Si recibimos coordenadas...
        lat = req.POST.get('lat') # Obtenemos latitud
        lon = req.POST.get('lon') # Obtenemos longitud

        if lat and lon and lat != "None" and lon != "None": # Si son válidas...
            new_cordenadas = cordenadas(latitud=float(lat), longitud=float(lon)) # Creamos coordenadas
            new_cordenadas.save() # Guardamos coordenadas

    # Valores predeterminados si no hay coordenadas POST o son "None".
    if not lat or lat == "None":
        lat = 28.6506657 # Latitud por defecto
    if not lon or lon == "None":
        lon = -106.0726896 # Longitud por defecto

    return render(req, '../templates/aplicacion/mapa.html', {'lat': lat, 'lon': lon}) # Mostramos el mapa

def agregarCar(req, producto_id):
    carrito = Carrito(req) # Creamos un carrito
    producto = Producto.objects.get(id=producto_id) # Buscamos el producto
    carrito.add(producto) # Lo agregamos al carrito
    carrito.guardar_carrito() # Guardamos el carrito
    print(req.session.get("carrito")) # Imprimimos el carrito (para depurar)
    return redirect('catalogo') # Redirigimos al catálogo

def aumentarCar(req, producto_id):
    carrito = Carrito(req) # Creamos un carrito
    producto = Producto.objects.get(id=producto_id) # Buscamos el producto
    carrito.add(producto) # Aumentamos la cantidad en el carrito
    carrito.guardar_carrito() # Guardamos el carrito
    print(req.session.get("carrito")) # Imprimimos el carrito (para depurar)
    return redirect('carrito') # Redirigimos al carrito

def eliminarCar(req, producto_id):
    carrito = Carrito(req) # Creamos un carrito
    producto = Producto.objects.get(id = producto_id) # Buscamos el producto
    carrito.eliminar_producto(producto) # Lo eliminamos del carrito
    return redirect('carrito') # Redirigimos al carrito

def RestarCar(req, producto_id):
    carrito = Carrito(req) # Creamos un carrito
    producto = Producto.objects.get(id = producto_id) # Buscamos el producto
    carrito.limpiar_carrito(producto) # Restamos la cantidad del producto
    return redirect('carrito') # Redirigimos al carrito

def limpiarCar(req):
    carrito = Carrito(req) # Creamos un carrito
    carrito.limpiar() # Vaciamos el carrito
    return redirect('catalogo') # Redirigimos al catálogo

def carrito(req):
    return render(req, '../templates/aplicacion/carrito.html') # Mostramos el carrito

def buscador(req):
    busqueda = req.GET.get('search', '') # Obtenemos la búsqueda
    productos = Producto.objects.filter( # Filtramos los productos
        Q(nombre__icontains=busqueda) | Q(descripcion__icontains=busqueda) # Buscamos en nombre o descripción
    )
    return render(req, '../templates/aplicacion/catalogo.html', {'productos': productos}) # Mostramos los resultados