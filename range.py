for x in range(6):
    print(x)

print("Break")
for z in range(8, 10):
    print(z)

print("-----------")

for y in range(2, 30, 3):
    print(y)

print('else in forloop')

for x in range(9):
    print(x)
else:
    print("finally stop")

fruits = ["Banana", "Apple", "mANGO", "cHERRY"]
price = [32, 43, 12, 55]

for x in fruits:
    for y in price:
        print(x, y)