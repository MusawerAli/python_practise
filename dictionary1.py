# Simplyprint

thisdict = {
    "model": "2015",
    "name": "Honda",
    "City": "LA" 
}

print(thisdict)

#printspecific key value

print(thisdict['model'])
print(thisdict['name'])
print(thisdict['City'])


#get values with get mehod

print(thisdict.get('mdoel'))
print(thisdict.get('name'))
print(thisdict.get('City'))


#Change value

thisdict['model'] = 2014
thisdict['name'] = 'Toyota'
print(thisdict['model'])
print(thisdict.get('name'))
print(thisdict)

#Removing itesm
thisdict["color"] = "red"
thisdict.popitem()

#Loop in thisdist
print("__________--for Loop--________")
for x in thisdict:
    print(x)
    print(thisdict[x])

    #with value method

    print('--WIth value method--')
    for x in thisdict.values():
        print(x)

        #with their key and value

        print('--items--')
        for x, y in thisdict.items():
            print(x, y)

            #check key is exist

            if "model" in thisdict:
                print("model is exist in thisdist")

            
                #print length of dict
                print("__________print length of dict")
                print(len(thisdict))

                # add new item in dict
    del.thisdict
print(thisdict)
       