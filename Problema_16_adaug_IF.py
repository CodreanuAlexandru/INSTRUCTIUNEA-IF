import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
d=0-(c/a)
e=b**2-4*a*c
if a==0:
    print("x=",0-(c/b))
elif b==0:
    if d>0:
        print("x=",math.sqrt(d))
    else:
        print("x=multime vida")
elif c==0:
    print("x1=0 si x2=",0-b/a)
else:
    if e>0:
        print("x1=",0-b-math.sqrt(e)/(2*a))
        print("x1=",0-b+math.sqrt(e)/(2*a))
    if e==0:
        print("x=",0-b/(2*a))
    if e<0:
        print("x=multime vida")