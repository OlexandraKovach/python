import random
n = int(input("Введіть n*n матриці : "))
a = [[random.randint(-10, 10) for j in range(n)] for i in range(n)]
print("Ісходна матриця : \n ")
print(*a, sep="\n")
for i in range(1, n, 2):
    a[i] = sorted(a[i], reverse=True)
print("Посортирована матриця : \n")
print(*a, sep="\n")
