n = int(input("Введите число n"))
 
a = 0
for i in range(1, n + 1):
    a += i ** 3
 
print(a)