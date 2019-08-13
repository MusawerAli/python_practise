# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.

set1 = {"Banana","apple","grapes"}

print(set1)

for x in set1:
    print(x)
#check if exist Boolean Return
print("Banana" in set1)

# Add Items
# To add one item to a set use the add() method.
# To add more than one item to a set use the update() method.

set1.add("cherry")

print(set1)
set1.update(["mango",'carger'])

print(set1)