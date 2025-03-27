from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Platillo,cordenadas
from django.contrib import messages
from django.shortcuts import redirect

@login_required

def makePlatillo(req):
    if req.method == "POST":
        nombre = req.POST.get('nombre')
        descripcion = req.POST.get('descripcion')
        foto = req.FILES.get('foto') 

        nuevo_platillo = Platillo(
            nombre=nombre,
            descripcion=descripcion,
            foto=foto
        )
        nuevo_platillo.save()
        messages.success(req, f"El platillo '{nombre}' ha sido registrado exitosamente.")
        return redirect('menu') 

    return render(req, "../templates/aplicacion/formulario.html")

def deletePlatillo(req, platillo_id):
    try:
        platillo = Platillo.objects.get(id=platillo_id)
        platillo.delete()
        messages.success(req, f"El platillo '{platillo.nombre}' ha sido eliminado exitosamente.")
    except Platillo.DoesNotExist:
        messages.error(req, "El platillo que intentas eliminar no existe.")
    return redirect('menu')


def menu(req):
    platillos = Platillo.objects.all()
    return render(req,'../templates/aplicacion/formulario.html',{'platillos':platillos})

def mapa(req):
    lat = None
    lon = None

    if req.method == "POST":
        lat = req.POST.get('lat')
        lon = req.POST.get('lon')

        if lat and lon and lat != "None" and lon != "None":
            new_cordenadas = cordenadas(
                latitud=float(lat),  
                longitud=float(lon)
            )
            new_cordenadas.save()

    if not lat or lat == "None":
        lat = 28.6506657  
    if not lon or lon == "None":
        lon = -106.0726896 

    return render(req, '../templates/aplicacion/mapa.html', {'lat': lat, 'lon': lon})
