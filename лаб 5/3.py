import math
x = float(input('Введіть число x: '))   # Дійсне число
eps = float(input('Введіть задану точність: '))     # Задана точінсть
s = x   # Сума
n = 1   # Натуральне число

while True:
    a = math.pow(-1, n-1) * (math.pow(x, 2 * n - 1) / math.factorial(2 * n - 1))  # Доданок
    if math.fabs(a) > eps:
        s += a
        n += 1
    else:
        break

print(f'Сума: {s}')
print(f'Синус від х: {math.sin(x)}')
if s == math.cos(x):
    print('Рівність справедлива')
else:
    print('Рівність несправедлива')
import math
x = float(input('Введіть число x: '))   # Дійсне число
eps = float(input('Введіть задану точність: '))     # Задана точінсть
s = x   # Сума
n = 1   # Натуральне число

while True:
    a = math.pow(-1, n-1) * (math.pow(x, 2 * n - 1) / math.factorial(2 * n - 1))  # Доданок
    if math.fabs(a) > eps:
        s += a
        n += 1
    else:
        break

print(f'Сума: {s}')
print(f'Синус від х: {math.sin(x)}')
if s == math.cos(x):
    print('Рівність справедлива')
else:
    print('Рівність несправедлива')