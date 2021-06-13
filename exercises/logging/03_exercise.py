#!/usr/bin/env python

import logging
from logging.handlers import RotatingFileHandler

# Create a custom log
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# sprawdź jeszcze rotację
f_handler = RotatingFileHandler('file.log', maxBytes=32, backupCount=5)
# logging.handlers.RotatingFileHandler

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the log
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')