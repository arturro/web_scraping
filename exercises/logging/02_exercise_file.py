#!/usr/bin/env python

import logging

logging.basicConfig(
    # datefmt='%d-%b-%y %H:%M:%S',
    level=logging.DEBUG,  # jaki poziom chcesz?
    filename='exercise.log',  # leci do pliku
    # plus pozmieniaj format

    # pozmieniajcie format na różne sposoby
    # format='%(name)s - %(levelname)s - %(message)s',
    # format='%(process)d-%(levelname)s-%(message)s',
    format='%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s'
)

logging.warning('warning...')
logging.error('warning...')

# równolegle w consoli włącz
# tail -f exercise.log


data = 'qwerty'
logging.error('data: %s', data)
logging.error(f'data: {data}')

my_dict = {
    'a': 1,
    'b': 2,
    'c': {
        'dalej': 4
    },
    'lst01': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'lst02': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'lst03': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'lst04': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'lst05': [1, 2, 3, 4, 5, 6, 7, 8, 9],
}

logging.error(f'my_dict: {my_dict}')
logging.error('my_dict: %s', my_dict)

from pprint import pformat, pprint  # pretty print

data_str = pformat(my_dict)
print(data_str)
pprint(my_dict)
logging.error(f'my_dict2: {pformat(my_dict)}')
