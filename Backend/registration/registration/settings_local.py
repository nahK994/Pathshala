from .settings import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': '0.0.0.0',
        'PORT': '5001',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200"
]