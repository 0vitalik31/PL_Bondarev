a=int(input("Введите А"))
b=int(input("Введите В"))
for i in range(a,b-1,-1):
    if i%2!=0:
        print(i)