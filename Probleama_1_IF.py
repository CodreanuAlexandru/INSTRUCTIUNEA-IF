n1=int(input("Introduceti numarul copilului:"))
p1=int(input("Introduceti punctajul corespunzator:"))
n2=int(input("Introduceti numarul copilului:"))
p2=int(input("Introduceti punctajul corespunzator:"))
n3=int(input("Introduceti numarul copilului:"))
p3=int(input("Introduceti punctajul corespunzator:"))
if (p1>p2) and (p1>p3) :
    print("Cel mai mare punctaj il are copilul cu numarul",n1)
elif (p2>p1) and (p2>p3) :
    print("Cel mai mare punctaj il are copilul cu numarul",n2)
else :
    print("Cel mai mare punctaj il are copilul cu numarul",n3)