import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuraciones básicas
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-t@85mpa7f*y!9lg*y9k+ukcetjc*_*eqvthk2hfo#0n$4o%wcw')
DEBUG = False  # ¡Desactiva DEBUG en producción!
ALLOWED_HOSTS = ['soporte.ana-hn.org', 'www.soporte.ana-hn.org']

# Seguridad HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Aplicaciones instaladas
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

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de rutas y WSGI
ROOT_URLCONF = 'techcare.urls'
WSGI_APPLICATION = 'techcare.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'techcare_db'),
        'USER': os.getenv('DB_USER', 'admin3'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'Test-12345'),
        'HOST': os.getenv('DB_HOST', '192.168.10.6'),
        'PORT': os.getenv('DB_PORT', '3306'),
    }
}

# Configuración de archivos estáticos y de medios
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Configuración de Templates en settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # Ruta donde estarán tus plantillas personalizadas
        ],
        'APP_DIRS': True,  # Esto permite que Django busque automáticamente plantillas en los directorios de las aplicaciones
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Necesario para el admin
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Configuración de correo
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'techcare.app2024@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'dvex nxbf quaj nxtc')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Logs de errores
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django_error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Campo por defecto de auto incrementación
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
