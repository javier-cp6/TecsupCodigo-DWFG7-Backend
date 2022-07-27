# Documentación de aplicacion

- drf-yasg (Swagger generator): https://github.com/axnsan12/drf-yasg/

# Desplegar aplicacion en Heroku

- Configurar static files para que pueda cargar Swagger
- Crear archivo Procfile
- Crear base de datos en Heroku con JawsDB
- Crear variables de entorno en Heroku con las credenciales de JawsDB
- Inicializar git en proyecto con: git init
- Hacer conexion remota con: heroku git:remote -a <nombre-de-la-aplicacion>
- Desplegar el proyecto con: git add . && git commit -m "Inicializacion" && git push heroku <nombre-de-la-rama>
- Hacer migración de la base de datos con: heroku run python manage.py migrate

# Configuración de CORS

- Url: https://pypi.org/project/django-cors-headers/
- Configurar aplicacion para que pueda ser consumida desde cualquier lugar
- Instalar el paquete cors: pip install django-cors-headers
- Añadir el paquete a la aplicacion:

```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]
```

- Añadir middlewares a la aplicacion:

```python
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]
```

- Añadir librería a requirements.txt:
