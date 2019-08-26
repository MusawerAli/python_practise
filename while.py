i = 1
while i < 6:
    print(i)
    i += 1

    #stop loop iof condition is true

x = 1
while x < 10:
    print(x)
    if x == 6:
        break
    x += 1

    #with continue ststement

z = 0
while z < 10:
    z += 1
    if z == 5:
        continue
    print(z)