class person:
    def __init__(self, fname , lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
    

class student(person):
    def __init__(self, fname, lname):
        person.__init__(self, fname, lname)

x = student("mikle", "jakson")
x.printname()


class teacher:
    def __init__(self, name, contact, address):
        self.fname = name
        self.number = contact
        self.address = address

    def printDetail(self):
        print("Name: " + self.fname)
        print("Contact: " + self.number)
        print("Address: " + self.address)


class student(teacher):
    def __init__(self, fname, lname, address,year):
        super().__init__(fname, lname, address)
        self.gradyear = year

x = student("Mike", "Ldsd", "LA",2019)
print(x.gradyear)
x.printDetail()