from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Platillo, cordenadas
from django.contrib import messages

# Vista para crear un nuevo platillo (requiere inicio de sesión).
@login_required
def makePlatillo(req):
    if req.method == "POST":
        nombre = req.POST.get('nombre')
        descripcion = req.POST.get('descripcion')
        foto = req.FILES.get('foto') # Obtiene el archivo de imagen.

        nuevo_platillo = Platillo(nombre=nombre, descripcion=descripcion, foto=foto)
        nuevo_platillo.save()
        messages.success(req, f"El platillo '{nombre}' ha sido registrado exitosamente.")
        return redirect('menu') # Redirige al menú después de la creación.

    return render(req, "../templates/aplicacion/formulario.html") # Muestra el formulario.

# Vista para eliminar un platillo por su ID.
def deletePlatillo(req, platillo_id):
    try:
        platillo = Platillo.objects.get(id=platillo_id)
        platillo.delete()
        messages.success(req, f"El platillo '{platillo.nombre}' ha sido eliminado exitosamente.")
    except Platillo.DoesNotExist:
        messages.error(req, "El platillo que intentas eliminar no existe.")
    return redirect('menu') # Redirige al menú después de la eliminación.

# Vista para mostrar el menú de platillos.
def menu(req):
    platillos = Platillo.objects.all() # Obtiene todos los platillos.
    return render(req, '../templates/aplicacion/formulario.html', {'platillos': platillos}) # Pasa los platillos al template.

# Vista para mostrar un mapa y guardar coordenadas.
def mapa(req):
    lat = None
    lon = None

    if req.method == "POST":
        lat = req.POST.get('lat')
        lon = req.POST.get('lon')

        if lat and lon and lat != "None" and lon != "None":
            new_cordenadas = cordenadas(latitud=float(lat), longitud=float(lon)) # Crea y guarda coordenadas.
            new_cordenadas.save()

    # Valores predeterminados si no hay coordenadas POST o son "None".
    if not lat or lat == "None":
        lat = 28.6506657
    if not lon or lon == "None":
        lon = -106.0726896

    return render(req, '../templates/aplicacion/mapa.html', {'lat': lat, 'lon': lon}) # Pasa latitud y longitud al template.