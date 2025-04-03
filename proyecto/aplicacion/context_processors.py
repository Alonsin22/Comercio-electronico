def total_carrito(req):
    total = 0  # Empezamos con un total de cero
    carrito = req.session.get("carrito")  # Intentamos obtener el carrito de la sesión del usuario
    if carrito:  # Si el carrito existe...
        for key, value in carrito.items():  # Recorremos los productos en el carrito
            try:
                total += float(value.get("total", 0))  # Sumamos el precio de cada producto al total
            except ValueError:
                print(f"Error: Valor 'total' inválido para el producto {key}")  # Si el precio no es un número, mostramos un error
            except Exception as e:
                print(f"Error inesperado: {e}")  # Si ocurre otro error, lo mostramos
    return {"total_carrito": total}  # Devolvemos el total del carrito

def inicializar_carrito(req):
    if 'carrito' not in req.session:  # Si el carrito no existe en la sesión...
        req.session['carrito'] = {}  # Creamos un carrito vacío
    return {}  # Devolvemos un diccionario vacío (no necesitamos devolver nada en realidad)