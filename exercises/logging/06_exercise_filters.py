#!/usr/bin/env python

# https://docs.python.org/3/howto/logging-cookbook.html

import logging
from random import choice
import uuid


class ContextFilter(logging.Filter):
    """
    This is a filter which injects contextual information into the log.

    Rather than use actual contextual information, we just use random
    data in this demo.
    """

    USERS = ['jim', 'fred', 'sheila']
    IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

    def filter(self, record):
        """
        jeżeli chcecie "puścić" rekord zwracacie True, przy False nic dalej nie będzie robione

        dodatkowo co mniej oczywiste można dodać własne informacje do recordu, po prostu dopisując do obiektu:
        """
        record.ip = choice(ContextFilter.IPS)
        record.user = choice(ContextFilter.USERS)
        record.ruid = str(uuid.uuid4())
        return True


if __name__ == '__main__':
    levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)-15s %(name)-5s %(levelname)-8s IP: %(ip)-15s ruid: %(ruid)-20s User: %(user)-8s %(message)s')
    a1 = logging.getLogger('a.b.c')
    a2 = logging.getLogger('d.e.f')

    f = ContextFilter()
    a1.addFilter(f)
    a2.addFilter(f)
    a1.debug('A debug message')
    a1.info('An info message with %s', 'some parameters')
    for x in range(10):
        lvl = choice(levels)
        lvl_name = logging.getLevelName(lvl)
        a2.log(lvl, 'A message at %s level with %d %s', lvl_name, 2, 'parameters')
