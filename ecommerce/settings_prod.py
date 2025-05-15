from .settings import *

DEBUG = False

ALLOWED_HOSTS = [
    '.vercel.app',
    'tc-r787czwmb-thanzihsts-projects.vercel.app',
    'tc.vercel.app',
    'localhost',
    '127.0.0.1',
    '*',  # Temporarily allow all hosts for testing
]

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres.vmggpyepxhdgigthsree'),
        'PASSWORD': os.environ.get('DB_PASSWORD', '9sdswIIg8ykTQvhF'),
        'HOST': os.environ.get('DB_HOST', 'aws-0-us-east-1.pooler.supabase.com'),
        'PORT': os.environ.get('DB_PORT', '6543'),
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
} 