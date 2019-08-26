class myclass:
    x = 5

p1 = myclass()
print(p1.x)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is: " + self.name)


p1 = person("Musaer", 43)

print(p1.name)
print(p1.age)
p1.myfunc()