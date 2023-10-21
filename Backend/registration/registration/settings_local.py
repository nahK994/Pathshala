from .settings import *
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'user_db'),
        'USER': os.getenv('POSTGRES_USER', 'skhan'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'haha'),
        'HOST': '0.0.0.0',
        'PORT': '5001',
    }
}

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200"
]