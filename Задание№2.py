a=int(input("Введите А"))
b=int(input("Введите В"))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
        print(i)