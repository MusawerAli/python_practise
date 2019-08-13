thisdict = {
    "name":"ali",
    "class":"bscs",
    "city":"bahawalpur"
}

print(thisdict['name'])
x=thisdict.get('name')
print(x)

#change value
thisdict["name"] = "Ali Raza"
print(thisdict)

#loop in dict

for x in thisdict:
    print(x)

#for accesss
for y in thisdict:
    print(thisdict[y])

#values() same method

for z in thisdict.values():
    print(z)

#print both key and values
    for a,b in thisdict.items():
        print(a,b)

#check if exist
if "ali" in thisdict:
    print("ali exist")
else:
    print("not exist")

    #find length
    print(len(thisdict))

#adding items
thisdict['color']="red"
print(thisdict)

#remove item specific item
thisdict.pop("color")
print(thisdict)

#copy dict
copydict = thisdict.copy()
print(copydict)

#dist
