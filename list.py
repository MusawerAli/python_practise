thislist = ["apple","banana","cherrry"]
print(thislist)

tihslist1 = ["apple","banana","cherry"]
print(tihslist1[1])

tihslist1[1] = "Orange"
print(tihslist1)

#For loop in py
for x in tihslist1:
    print(x)
else:
    #check condition

    if "apple" in tihslist1:
        print("yes apple heew")
    else: 
       print("not found")
       
    
print(len(thislist))


#append
tihslist1.append("bana")
print(tihslist1)

#insert
tihslist1.insert(1,"blueberry")
print(tihslist1)

#remove
tihslist1.remove("bana")
print(tihslist1)


#del
print(thislist)
del thislist[0]
print(thislist)


#clear
list2 = ["Aircondition","LED","Charger"]
print(list2)
list2.clear()
print(list2)

#copy
copylist = tihslist1.copy()
print(copylist)

#list
copylist2 = list(tihslist1)
print(copylist2)