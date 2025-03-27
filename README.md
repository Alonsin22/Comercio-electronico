# Proyecto E-commerce de Platillos con Geolocalización

Este proyecto es una aplicación web de Django que permite gestionar un e-commerce de platillos, incluyendo la creación, eliminación y visualización de platillos, así como la funcionalidad de geolocalización para mostrar la ubicación de los platillos en un mapa.

## Funcionalidades Principales

* **Gestión de Platillos (CRUD):**
    * Creación de nuevos platillos con nombre, descripción e imagen.
    * Visualización de la lista de platillos disponibles.
    * Eliminación de platillos existentes.
* **Geolocalización:**
    * Registro de coordenadas (latitud y longitud) para cada platillo.
    * Visualización de la ubicación de los platillos en un mapa.
* **Autenticación de Usuarios:**
    * Protección de la creación de platillos, requiriendo inicio de sesión de administrador.
    * Manejo de rutas de inicio y cierre de sesión.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

* **`aplicacion/`:**
    * Contiene los modelos (`models.py`), vistas (`views.py`) y plantillas HTML para la aplicación.
    * `models.py`: Define los modelos `Platillo`, `administrador` y `cordenadas` para la base de datos.
    * `views.py`: Implementa las vistas para la creación, eliminación y visualización de platillos, así como la funcionalidad del mapa.
    * `templates/aplicacion/`: Almacena las plantillas HTML para la interfaz de usuario.
* **`proyecto/`:**
    * Contiene la configuración general del proyecto (`settings.py`, `urls.py`).
    * `urls.py`: Define las URLs del proyecto, incluyendo las rutas para la aplicación y la autenticación de usuarios.
* **`static/` y `media/`:**
    * `media/`: Almacena los archivos de imágenes cargados por los usuarios.
    * `static/`: Almacena los archivos estáticos (CSS, JavaScript, etc.).

## Configuración e Instalación

1.  **Requisitos previos:**
    * Python 3.x
    * Django
    * Pillow (PIL)
2.  **Instalación de dependencias:**
    * `pip install django pillow`
3.  **Configuración de la base de datos:**
    * Configura la base de datos en el archivo `proyecto/settings.py`.
4.  **Migraciones:**
    * Ejecuta `python manage.py migrate` para crear las tablas de la base de datos.
5.  **Ejecución del servidor:**
    * Ejecuta `python manage.py runserver` para iniciar el servidor de desarrollo.

## Rutas Principales

* `/admin/`: Panel de administración de Django.
* `/accounts/`: Rutas de autenticación de usuarios (inicio y cierre de sesión).
* `/menu/`: Lista de platillos disponibles.
* `/newPlatillo/`: Formulario para crear un nuevo platillo (requiere inicio de sesión).
* `/deletePlatillo/<int:platillo_id>/`: Eliminación de un platillo por su ID.
* `/mapa/`: Visualización del mapa y registro de coordenadas.

## Consideraciones

* Las contraseñas de administrador deben almacenarse de forma segura utilizando hashing.
* Se recomienda implementar validaciones adicionales para la entrada de datos.
* Se debe de considerar la correcta configuración de las plantillas de autenticación.

Este README proporciona una visión general del proyecto y su funcionalidad.
