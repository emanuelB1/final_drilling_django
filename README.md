# Venta Virtual de Vehículos


## Descripción

Este proyecto implementa una tienda virtual de ventas de vehículos desarrollada en Django, con un diseño moderno y amigable utilizando Bootstrap. Los usuarios pueden explorar un catálogo de vehículos, agregar nuevos vehículos y acceder a funcionalidades exclusivas según sus roles y permisos.

## Funcionalidades Implementadas

- Creación del ambiente de desarrollo virtual con las bibliotecas necesarias.
- Estructura del proyecto con directorio `proyecto_vehiculos_django` y aplicación `vehiculo`.
- Definición del modelo de datos para vehículos, incluyendo campos como Marca, Modelo, Serial Carrocería, etc.
- Creación del superusuario con credenciales `admin/admin`.
- Registro de la aplicación en el sitio administrativo de Django.
- Diseño de la página de inicio (`index.html`) con enlace al catálogo de vehículos.
- Formulario de ingreso de vehículos en `http://localhost:8000/vehiculo/add`.
- Listado de vehículos y condiciones de precios bajo, medio y alto.
- Creación de un permiso personalizado `visualizar_catalogo` para visualizar el catálogo de vehículos.
- Asignación automática del permiso `visualizar_catalogo` a nuevos usuarios registrados.
- Implementación de menú de navegación (navbar) utilizando Bootstrap, con enlaces a la página de inicio y al formulario de ingreso de vehículos.

## Instalación y Uso

1. Clona este repositorio
2. Ve a la carpeta del proyecto: `cd proyecto-vehiculos`
3. Crea y activa un entorno virtual (opcional pero recomendado).
4. Instala las dependencias: `pip install -r requirements.txt`
5. Ejecuta las migraciones: `python manage.py migrate`
6. Crea el superusuario: `python manage.py createsuperuser`
7. Inicia el servidor de desarrollo: `python manage.py runserver`
8. Abre tu navegador y visita `http://localhost:8000` para explorar la tienda virtual de vehículos.

## Contribuciones

Contribuciones son bienvenidas. Si deseas mejorar el proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama: `git checkout -b mejora/funcionalidad`
3. Realiza tus cambios y commitea: `git commit -m "Añade una mejora"`
4. Haz push a la rama: `git push origin mejora/funcionalidad`
5. Abre un pull request en GitHub.


---

**Venta Virtual de Vehículos** - Todos los derechos reservados.

Hecho con ❤️ por [emanuelB1](https://github.com/emanuelB1)
