a = 10
b = 2
c = 10

if a > b:
    print("A is Greater than B")

if b > a:
    print("B is greater than a")
else:
        print("B is less than a")

if a < b:
    print("B is grater is A")
elif a == c:
    print("A & B are equal")
else:
    print("A is grearter")

    #short hand if

print("A is grearter") if a > b else print("Print B")

d = 100
e = 200
c = 100

print("D is Less") if d < e else print("e is grater") if e > d else print("d and c are qequal") 
print("e is lesss") if e < d else print("d is grater") if(d > e) else print("both d and c are equal") 