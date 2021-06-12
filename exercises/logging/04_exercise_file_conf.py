#!/usr/bin/env python

import logging.config

# konfiguracja z zewnętrznego pliku
logging.config.fileConfig(fname='04_file.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
logger.debug('Debug ')

