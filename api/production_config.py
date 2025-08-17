"""
Production Configuration for API
================================

This file contains production-specific configurations for the API.
Include these settings in your production settings.py file.
"""

# API Production Settings
API_PRODUCTION_SETTINGS = {
    # Security settings
    'SECURE_SSL_REDIRECT': True,
    'SECURE_BROWSER_XSS_FILTER': True,
    'SECURE_CONTENT_TYPE_NOSNIFF': True,
    'X_FRAME_OPTIONS': 'DENY',
    
    # CORS settings for production
    'CORS_ALLOWED_ORIGINS': [
        'https://yourdomain.com',
        'https://www.yourdomain.com',
        'https://api.yourdomain.com',
    ],
    'CORS_ALLOW_CREDENTIALS': True,
    
    # REST Framework settings
    'REST_FRAMEWORK': {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication',
            # 'rest_framework_simplejwt.authentication.JWTAuthentication',  # Uncomment if using JWT
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',  # Change from AllowAny for production
        ],
        'DEFAULT_THROTTLE_CLASSES': [
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ],
        'DEFAULT_THROTTLE_RATES': {
            'anon': '100/hour',
            'user': '1000/hour'
        },
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 20,
        'DEFAULT_FILTER_BACKENDS': [
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter',
            'rest_framework.filters.OrderingFilter',
        ],
    },
    
    # Caching settings
    'CACHES': {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': 'redis://127.0.0.1:6379/1',
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            }
        }
    },
    
    # Session settings
    'SESSION_ENGINE': 'django.contrib.sessions.backends.cache',
    'SESSION_CACHE_ALIAS': 'default',
    
    # Logging settings
    'LOGGING': {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
                'style': '{',
            },
            'simple': {
                'format': '{levelname} {message}',
                'style': '{',
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': '/var/log/django/api.log',
                'formatter': 'verbose',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
            },
            'api': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    },
}

# API Rate Limiting
API_RATE_LIMITING = {
    'DEFAULT_RATE_LIMIT': '100/hour',
    'ANONYMOUS_RATE_LIMIT': '50/hour',
    'USER_RATE_LIMIT': '1000/hour',
}

# API Caching
API_CACHING = {
    'DEFAULT_CACHE_TIMEOUT': 300,  # 5 minutes
    'ARTICLES_CACHE_TIMEOUT': 600,  # 10 minutes
    'PORTFOLIO_CACHE_TIMEOUT': 1800,  # 30 minutes
    'WEB_CONFIG_CACHE_TIMEOUT': 3600,  # 1 hour
}

# API Monitoring
API_MONITORING = {
    'ENABLE_METRICS': True,
    'METRICS_ENDPOINT': '/api/metrics/',
    'HEALTH_CHECK_ENDPOINT': '/api/health/',
}

# API Documentation
API_DOCUMENTATION = {
    'ENABLE_SWAGGER': True,
    'SWAGGER_SETTINGS': {
        'SECURITY_DEFINITIONS': {
            'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header'
            }
        },
        'USE_SESSION_AUTH': False,
        'JSON_EDITOR': True,
    },
    'REDOC_SETTINGS': {
        'LAZY_RENDERING': False,
    }
}

# API Security
API_SECURITY = {
    'ENABLE_HTTPS': True,
    'ENABLE_CSRF': True,
    'ENABLE_XSS_PROTECTION': True,
    'ENABLE_CONTENT_TYPE_NOSNIFF': True,
    'ENABLE_FRAME_DENY': True,
    'ALLOWED_HOSTS': [
        'yourdomain.com',
        'www.yourdomain.com',
        'api.yourdomain.com',
    ],
}

# Database optimization for API
API_DATABASE = {
    'CONN_MAX_AGE': 600,
    'OPTIONS': {
        'MAX_CONNS': 20,
        'MIN_CONNS': 5,
    },
    'READ_REPLICA': {
        'HOST': 'your-read-replica-host',
        'PORT': 5432,
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
    }
}

# CDN Configuration
API_CDN = {
    'ENABLE_CDN': True,
    'CDN_DOMAIN': 'cdn.yourdomain.com',
    'STATIC_URL': 'https://cdn.yourdomain.com/static/',
    'MEDIA_URL': 'https://cdn.yourdomain.com/media/',
}

# Email configuration for API notifications
API_EMAIL = {
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_HOST': 'smtp.yourdomain.com',
    'EMAIL_PORT': 587,
    'EMAIL_USE_TLS': True,
    'EMAIL_HOST_USER': 'api@yourdomain.com',
    'EMAIL_HOST_PASSWORD': 'your_email_password',
    'DEFAULT_FROM_EMAIL': 'API <api@yourdomain.com>',
}

# Monitoring and Analytics
API_ANALYTICS = {
    'ENABLE_ANALYTICS': True,
    'ANALYTICS_PROVIDER': 'google_analytics',  # or 'mixpanel', 'amplitude'
    'TRACK_API_CALLS': True,
    'TRACK_ERRORS': True,
    'TRACK_PERFORMANCE': True,
}

# Backup and Recovery
API_BACKUP = {
    'ENABLE_AUTO_BACKUP': True,
    'BACKUP_SCHEDULE': '0 2 * * *',  # Daily at 2 AM
    'BACKUP_RETENTION_DAYS': 30,
    'BACKUP_STORAGE': 's3',  # or 'local', 'gcs'
    'BACKUP_BUCKET': 'your-backup-bucket',
}

# Performance Optimization
API_PERFORMANCE = {
    'ENABLE_COMPRESSION': True,
    'COMPRESSION_LEVEL': 6,
    'ENABLE_GZIP': True,
    'ENABLE_BROTLI': True,
    'MIN_COMPRESS_SIZE': 200,
    'CACHE_HEADERS': True,
    'CACHE_TIMEOUT': 300,
}

# Error Handling
API_ERROR_HANDLING = {
    'ENABLE_DETAILED_ERRORS': False,  # Set to False in production
    'LOG_ERRORS': True,
    'NOTIFY_ON_ERROR': True,
    'ERROR_NOTIFICATION_EMAIL': 'admin@yourdomain.com',
    'CUSTOM_ERROR_PAGES': True,
}

# API Versioning
API_VERSIONING = {
    'ENABLE_VERSIONING': True,
    'DEFAULT_VERSION': 'v1',
    'ALLOWED_VERSIONS': ['v1', 'v2'],
    'VERSION_PARAM': 'version',
    'VERSION_HEADER': 'X-API-Version',
}

# Testing Configuration
API_TESTING = {
    'ENABLE_API_TESTS': True,
    'TEST_DATABASE': 'test_db',
    'TEST_CACHE': 'test_cache',
    'COVERAGE_THRESHOLD': 80,
    'ENABLE_PERFORMANCE_TESTS': True,
}

# Deployment Configuration
API_DEPLOYMENT = {
    'ENVIRONMENT': 'production',
    'DEBUG': False,
    'ALLOWED_HOSTS': ['yourdomain.com', 'www.yourdomain.com'],
    'STATIC_ROOT': '/var/www/static/',
    'MEDIA_ROOT': '/var/www/media/',
    'WSGI_APPLICATION': 'backend.wsgi.application',
    'ASGI_APPLICATION': 'backend.asgi.application',
}

# Load Balancer Configuration
API_LOAD_BALANCER = {
    'ENABLE_LOAD_BALANCER': True,
    'HEALTH_CHECK_PATH': '/api/health/',
    'HEALTH_CHECK_INTERVAL': 30,
    'HEALTH_CHECK_TIMEOUT': 5,
    'HEALTH_CHECK_THRESHOLD': 3,
}

# SSL/TLS Configuration
API_SSL = {
    'ENABLE_SSL': True,
    'SSL_CERTIFICATE': '/path/to/ssl/certificate.crt',
    'SSL_PRIVATE_KEY': '/path/to/ssl/private.key',
    'SSL_CHAIN': '/path/to/ssl/chain.crt',
    'SSL_PROTOCOLS': ['TLSv1.2', 'TLSv1.3'],
    'SSL_CIPHERS': 'ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES128-GCM-SHA256',
}

# Example usage in settings.py:
"""
# In your production settings.py, include these settings:

from api.production_config import API_PRODUCTION_SETTINGS

# Apply production settings
for key, value in API_PRODUCTION_SETTINGS.items():
    globals()[key] = value

# Or apply specific settings:
REST_FRAMEWORK = API_PRODUCTION_SETTINGS['REST_FRAMEWORK']
CORS_ALLOWED_ORIGINS = API_PRODUCTION_SETTINGS['CORS_ALLOWED_ORIGINS']
CACHES = API_PRODUCTION_SETTINGS['CACHES']
LOGGING = API_PRODUCTION_SETTINGS['LOGGING']
""" 