from .base import BASE_DIR


DEBUG_LOG_DIR = BASE_DIR + "opt/python/log/django_logs.log"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # How to format the output
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    # Log handlers (where to go)
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'log_file': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': DEBUG_LOG_DIR,
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter': 'standard',
        },
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'formatter': 'standard'
        }
    },
    # Loggers (where does the log come from)
    'loggers': {
        'repackager': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django': {
            'handlers':['console'],
            'propagate': True,
            'level':'WARN',
        },
        'django.db.backends': {
            'handlers': ['console', 'log_file'],
            'level': 'WARN',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
        }
    }
}

