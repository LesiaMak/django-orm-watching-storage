import os
from environs import Env

env = Env()
env.read_env() 

DATABASES = {
    'default': {
        'DB_ENGINE': env.str('ENGINE'),
        'DB_HOST': env.str('HOST'),
        'DB_PORT': env.str('PORT'),
        'DB_NAME': env.str('NAME'),
        'DB_USER': env.str('USER'),
        'DB_PASSWORD': env.str('PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SECRET_KEY')

DEBUG  = env.bool("DEBUG", default = False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
