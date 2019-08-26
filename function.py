def printData():
    print("THis is from printData")

printData()
    
#passing parameters


def my_function(fname):
    print(fname + "! Have a nice day")

my_function("Ali")
my_function("Musawer")
my_function("K2")


#Default Parameter value

def function_deft_value(country="Pakistan"):
    print("I am from: " + country)

function_deft_value("UK")
function_deft_value()

#intro function


def intro(name, country="pakistan"):
    print("My Name is: " + name)
    print("I'm Orignally From: " + country)

intro("musawer")
intro("K2", "Norway")

fruits = ["banana", "Mango", "cherry", "Orange", "Strw"]


def fruit_fun(fr_name, breakf):
    for x in fr_name:
        if x == breakf:
            break
        print(x)


fruit_fun(fruits, "Mango")

# Return value to function


def fun_return(x, y):
    return x*y

print(fun_return(4, 5))


def key_fun(child1, child2, child3):
    print("Father of " + child1 + " is "+child3)

key_fun(child1="ALi", child2="Ghazanfar", child3="Musawer")

#function arbitarty


def fun_arbitary(*students):
    print("Studnts names are: " + students[2])

fun_arbitary("ALi", "Musawer", "K2")