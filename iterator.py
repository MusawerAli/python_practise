mytupples = ("Apple", "Orange", "Mango")

getiter = iter(mytupples)
print(next(getiter))
print(next(getiter))
print(next(getiter))

tupple2 = ("Apple", "Orange", "Mango")

for x in tupple2:
    print(x)
