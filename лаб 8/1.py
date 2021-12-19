import math
def f(x):
    if x > 3:
        summ = 0
        for i in range(1, 18, 2):
            summ += math.sin(x) ** i
    else:
        el = math.tan(x)
        summ = 15 + el
        for i in range(4):
            el = math.tan(el)
            summ += el

    return summ
a = int(input('a: '))
b = int(input('b: '))
u = max(f(a), f(b))
print(u)