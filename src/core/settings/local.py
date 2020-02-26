# pylint: skip-file
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '83107a3e-57ee-4af4-9caa-a1e312e29793'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': ''
    }
}

ALLOWED_HOSTS = ['*']
