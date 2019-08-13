a = 50
b =20
c = 54
d=50
if b>a:
    print("b is greater than b")
elif c>a:
    print("c is grater than a")
else:
    print("a is grater than b")

    #Short Hand if...Else
print("A") if a > b else print("B")

#print Multiple
print("A") if a< d else print("=") if a == d else print("B") 

if a>b and d>b:
    print("Both are true")

    if a<b or c>a:
        print("one is true")