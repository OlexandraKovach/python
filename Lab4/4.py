'''
число - float - x
'''
import math
x = float(input('Введіть х - '))
y = float(input('Введіть у - '))
if y<x:
    Z = y*(math.e)**x
elif y == x :
    Z = y * x
else:
    Z = x*(math.e)**y
print('Result - {0:7.2f}'.format(Z))


