n = int(input("Введите число n"))
k = int(input("Введите число k"))
a=1
b=1
for i in range(1, n + 1):
    if i>=k:
        b += a
    a +=i
print(b)