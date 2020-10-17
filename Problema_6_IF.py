a=int(input("Prima nota:"))
b=int(input("A doua nota:"))
c=int(input("A treia nota:"))
if (a>10) or (a<1) or (b>10) or (b<1) or (c>10) or (c<1):
    print("Eroare la introducerea notelor")
    'break'
elif c>=8:
    print(a,b,c)
else:
    if a>b:
        print(a)
    if a<b:
        print(b)
    if a==b:
        print(a)