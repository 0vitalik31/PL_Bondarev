n = int(input("Введите число n"))
a = 1
b= 0
for i in range(1, n + 1):
    a =a * i
    b += a
print(b)