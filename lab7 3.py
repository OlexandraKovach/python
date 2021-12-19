from random import randint
i = int(input('Рядки : '))
j = int(input('Стовпчики : '))
A = [[randint(-10, 10) for x in range(j)] for y in range(i)]
print('A:', *A, sep="\n")
b = [randint(-10, 10) for z in range(j)]
print(f'b:\n{b}')
for x in range(i):
    for y in range(j):
        A[x][y] *= b[y]
print('A:', *A, sep="\n")
