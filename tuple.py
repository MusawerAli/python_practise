# Tuple
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

thistuple = ('Banana','Apple','Grapes')
print(thistuple)

print(thistuple[1])

#access tuple with for loop
for x in thistuple:
    print(x)

#check if exist
if "Apple" in thistuple:
    print("Yes apple are exist")
else:
    print("no found")

#find length

print(len(thistuple))

this = tuple(('bnana','apple','cherry'))
print(this)