aa=int(input("Introduceti numarul bilelor albe mici:"))
ab=int(input("Introduceti numarul bilelor albe mari:"))
ba=int(input("Introduceti numarul bilelor rosii mici:"))
bb=int(input("Introduceti numarul bilelor rosii mari:"))
ca=int(input("Introduceti numarul bilelor verzi mici:"))
cb=int(input("Introduceti numarul bilelor verzi mari:"))
print("Totalul bilelor:",aa+ab+ba+bb+ca+cb)
if aa+ba+ca>ab+bb+cb:
    print("Mari:",ab+bb+cb,"bile")
else:
    print("Mici:",aa+ab+ca,"bile")
if (aa+ab>ba+bb) and (aa+ab>ca+cb):
    print("Albe:",aa+ab,"bile")
elif (ba+bb>aa+ab) and (ba+bb>ca+cb):
    print("Rosii:",ba+bb,"bile")
else:
    print("Verzi:",ca+cb,"bile")