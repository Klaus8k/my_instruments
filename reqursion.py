from my_logger import logger_timer

logger = logger_timer

import sys
sys.setrecursionlimit(20000)

# Декоратор с логерром для измерения времени
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

# logger.warning('start')
# fuctor(2000)
# logger.warning('end====================')



def fuc(l):
    res = 1
    x = 1
    while x <= l:
        res *= x
        x += 1

    return res


def fib(a):
    if a == 1 or a == 0:
        return a
    else:
        return fib(a-1) + fib(a-2)

# logger.warning('start')
# print(fib(20))
# logger.warning('end')

def fib_while(x):
    count = 1
    a = 0
    b = 1
    res = 0
    while count != x:
        res = a + b
        a,b = b, res
        count += 1
    print(res)
    return res

# @timer
def aaa(x, a=1):
    print(a)
    if a == x:
        return a
    else:
        return aaa(x, a+1)

aaa(10)