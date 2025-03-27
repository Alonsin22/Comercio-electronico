#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Ruta donde deseas crear la carpeta (ajusta según tu estructura de proyecto)
project_dir = os.path.dirname(os.path.abspath(__file__))
upload_dir = os.path.join(project_dir, 'media/images')

# Crear la carpeta si no existe
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)
    print(f"Carpeta creada: {upload_dir}")
else:
    print(f"La carpeta ya existe: {upload_dir}")

if __name__ == '__main__':
    main()
