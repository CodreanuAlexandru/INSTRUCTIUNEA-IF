a=int(input("Primul numar:"))
b=int(input("Al doilea numar:"))
if (a%2==0) and (b%2==0):
    if a>b:
        print(a)
    else:
        print(b)
elif (a%2!=0) and (b%2==0):
    print(b)
elif (a%2==0) and (b%2!=0):
    print(a)
else:
    print("Nu exista numere pare")