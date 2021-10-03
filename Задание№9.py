n = int(input("Введите число n"))
a=1
b=1
for i in range(1, n + 1):
    b += a
    a +=i
print(b)
