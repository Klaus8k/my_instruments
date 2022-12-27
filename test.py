import logging

logger = logging.getLogger('timer')
exit_handler = logging.StreamHandler()
format_formatter = logging.Formatter('%(asctime)s --- %(message)s')
exit_handler.setFormatter(format_formatter)
logger.addHandler(exit_handler)

import sys
sys.setrecursionlimit(20000)

def timer(fn):
    def wrap(*args, **kwargs):
        logger.warning('start')
        fn(*args, **kwargs)
        logger.warning('end')
    return wrap

def fuctor(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fuctor(x-1)

logger.warning('start')
fuctor(2000)
logger.warning('end====================')


@timer
def fuc(l):
    res = 1
    x = 1
    while x <= l:
        res *= x
        x += 1

    return res

print(fuc(2000))
