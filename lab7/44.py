import random
sum = 0
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовбців матриці : "))
a = [[random.randint(-4, 10) for j in range(m)] for i in range(n)]
print("Ісходна матриця : \n ")
print(*a, sep="\n")

for j in range(m):
    for i in range(n):
        if a[i][j]<0:
            for y in range(n):
                sum += a[y][j]
            break
print(sum)