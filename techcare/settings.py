import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

# Cargar las variables del archivo .env
load_dotenv()

# ---------------------------------------------------------------------------
# 🗂️ CONFIGURACIÓN BASE DEL PROYECTO
# ---------------------------------------------------------------------------

# BASE_DIR: La ruta base del proyecto Django
BASE_DIR = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# 🔐 CONFIGURACIÓN DE SEGURIDAD
# ---------------------------------------------------------------------------

# SECRET_KEY: Clave secreta para proteger la aplicación Django
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-t@85mpa7f*y!9lg*y9k+ukcetjc*_eqvthk2hfo#0n$4o%wcw')

# DEBUG: Modo depuración (True en desarrollo, False en producción)
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

# ALLOWED_HOSTS: Lista de dominios permitidos para acceder a la aplicación
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# ---------------------------------------------------------------------------
# 🖥️ APLICACIONES INSTALADAS
# ---------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'helpdesk',
    'inventory',
    'maintenance',
    'accounts',
]


# ---------------------------------------------------------------------------
# ⚙️ MIDDLEWARE
# ---------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ---------------------------------------------------------------------------
# 🔗 CONFIGURACIÓN DE RUTAS PRINCIPALES
# ---------------------------------------------------------------------------

ROOT_URLCONF = 'techcare.urls'

# ---------------------------------------------------------------------------
# 📝 CONFIGURACIÓN DE TEMPLATES
# ---------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
            BASE_DIR / 'helpdesk/templates',
            BASE_DIR / 'inventory/templates',
            BASE_DIR / 'maintenance/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ---------------------------------------------------------------------------
# 🌐 CONFIGURACIÓN WSGI
# ---------------------------------------------------------------------------

WSGI_APPLICATION = 'techcare.wsgi.application'

# ---------------------------------------------------------------------------
# 🗄️ CONFIGURACIÓN DE BASE DE DATOS
# ---------------------------------------------------------------------------

DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Ejemplo de `DATABASE_URL` en el archivo .env:
# DATABASE_URL=postgresql://techcare_db_user:DNVqE7QP6R4N0oWare28OCc3jG8xFfb4@dpg-cthe6ctumphs73fnbjfg-a/techcare_db

# ---------------------------------------------------------------------------
# 🔐 CONFIGURACIÓN DE AUTENTICACIÓN
# ---------------------------------------------------------------------------

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/accounts/menu/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# ---------------------------------------------------------------------------
# 📧 CONFIGURACIÓN DE CORREO ELECTRÓNICO
# ---------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'techcare.app2024@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'dvex nxbf quaj nxtc')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ---------------------------------------------------------------------------
# 📂 CONFIGURACIÓN DE ARCHIVOS ESTÁTICOS
# ---------------------------------------------------------------------------

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
    BASE_DIR / 'helpdesk/static',
]

# Carpeta donde se recopilarán los archivos estáticos en producción
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ---------------------------------------------------------------------------
# 🖼️ CONFIGURACIÓN DE IMÁGENES Y MULTIMEDIA
# ---------------------------------------------------------------------------

# Ruta para la imagen de los tickets
TICKET_IMAGE_PATH = os.getenv('TICKET_IMAGE_PATH', 'techcare/helpdesk/static/helpdesk/img/ana-transformed.png')

# ---------------------------------------------------------------------------
# 🔍 CONFIGURACIÓN DE ID AUTOMÁTICO POR DEFECTO
# ---------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
