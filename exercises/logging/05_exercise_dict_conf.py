#!/usr/bin/env python

import logging
from logging.config import dictConfig

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',  # dzięki temu możesz pisać już f-stringi zamiast %
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            # 'filters': ['require_debug_true'],
            # 'formatter': 'simple',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'info.log',
        },
    },
    'loggers': {
        # __name__ w tym wypadku to nazwa pliku, w django sprawdź co leci jako {module}
        __name__: {
            'handlers': ['console', ],
            'level': 'DEBUG',
            # 'propagate': False,  # sprawdź i to
        },
        '': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
dictConfig(LOGGING)
# logging.config.dictConfig(LOGGING)  # można też tak, zależy jak importujecie

# Create a custom log
logger = logging.getLogger(__name__)

logger.debug('gdzie trafi debug')
logger.info('gdzie info?')
