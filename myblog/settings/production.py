from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['halpi17.com', '.halpi17.com']

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('X-Forwarded-Proto', 'https')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'hrn30xup8',
    'API_KEY': '429999974535526',
    'API_SECRET': 'JszbV5cjJ0QQX7Lvnl0_FmPl2B0'
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'