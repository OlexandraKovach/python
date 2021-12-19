import random
n = int(input("Введіть розмірність матриці : "))
A = [[float(random.randint(-10, 10)) for j in range(n)] for i in range (n)]
print(*A, sep="\n")
sum = 0
for i in range(n):
    for j in range (n):
        if A[i][j]<0:
            if (j+i)%2==0:
                sum += A[i][j]
print(f"sum = {sum}")


