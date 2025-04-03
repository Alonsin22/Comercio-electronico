class Carrito:
    def __init__(self, req):
        self.req = req  # Guardamos la petición para usar la sesión
        self.session = req.session  # Obtenemos la sesión del usuario
        carrito = self.session["carrito"]  # Intentamos obtener el carrito de la sesión
        if not carrito:  # Si no hay carrito en la sesión...
            self.session["carrito"] = {}  # Creamos un carrito vacío
            self.carrito = self.session["carrito"]  # Lo asignamos a self.carrito
        else:
            self.carrito = carrito  # Si ya hay carrito, lo usamos

    def add(self, producto):
        id = str(producto.id)  # Obtenemos el ID del producto como cadena
        if id not in self.carrito.keys():  # Si el producto no está en el carrito...
            self.carrito[id] = {  # Creamos una entrada para el producto
                "id": producto.id,
                "nombre": producto.nombre,
                "total": str(producto.precio),  # Guardamos el precio como cadena
                "cantidad": 1,  # Cantidad inicial: 1
            }
        else:  # Si el producto ya está en el carrito...
            self.carrito[id]["cantidad"] += 1  # Aumentamos la cantidad
            self.carrito[id]["total"] = str(float(self.carrito[id]["total"]) + float(producto.precio))  # Actualizamos el total
        self.guardar_carrito()  # Guardamos los cambios en la sesión

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito  # Actualizamos el carrito en la sesión
        self.session.modified = True  # Marcamos la sesión como modificada

    def eliminar_producto(self, producto):
        id = str(producto.id)  # Obtenemos el ID del producto como cadena
        if id in self.carrito.keys():  # Si el producto está en el carrito...
            del self.carrito[id]  # Lo eliminamos
            self.guardar_carrito()  # Guardamos los cambios

    def limpiar_carrito(self, producto):
        id = str(producto.id)  # Obtenemos el ID del producto como cadena
        if id in self.carrito.keys():  # Si el producto está en el carrito...
            self.carrito[id]["cantidad"] -= 1  # Disminuimos la cantidad
            self.carrito[id]["total"] = str(float(self.carrito[id]["total"]) - float(producto.precio))  # Actualizamos el total
        if self.carrito[id]["cantidad"] <= 0:  # Si la cantidad llega a cero...
            del self.carrito[id]  # Eliminamos el producto del carrito
        self.guardar_carrito()  # Guardamos los cambios

    def limpiar(self):
        self.session["carrito"] = {}  # Vaciamos el carrito
        self.session.modified = True  # Guardamos los cambios