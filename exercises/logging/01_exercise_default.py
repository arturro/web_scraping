#!/usr/bin/env python

import logging

logger = logging.getLogger(__name__)

# nie poleci bo default jest od warning
logger.debug('This is a debug message')
logger.info('This is an info message')

# to poleci
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

# minimalna konfiguracja i proszę:
logging.basicConfig(level=logging.DEBUG)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

try:
    1 / 0
except ZeroDivisionError:
    logger.error('nie dziel przez 0')
    # logger.error('nie dziel przez 0', exc_info=True)  # zadziała analogicznie jak logger.exception
    # logger.exception('nie dziel przez 0')
    # porównaj error i exception
except Exception:
    pass  # tego nie rób bo można nie wychwycić krytycznych rzeczy
