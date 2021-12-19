py
import random

def x(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n > 1:
        return x(n-2) + x(n-1)
n = random.randint(0, 10)
print('result = {0}'.format(x(n)))