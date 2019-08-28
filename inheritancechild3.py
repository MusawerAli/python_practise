class person:
    def __init__(self, fname, address, cnic):
        self.fullname = fname
        self.paddress = address
        self.pcnic = cnic   

    def printDetail(self):
        print("Full Name: " + self.fullname)
        print("address: " + self.paddress)
        print("Full Name: " + self.pcnic)


class student(person):
    def __init__(self,fname, address, cnic, admYear):
        super().__init__(fname, address, cnic)
        self.admissionYear = admYear

    def printStdDetail(self):
        print("Admissoin Year: " + self.admissionYear)

        
x = person("Musawer","Bahawalput","3232323434")
y = student("musawer","ali",'dfasd','432432')
x.printDetail()
y.printStdDetail()