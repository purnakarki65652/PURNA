class Base(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self, name)
        #super().__init__(self, name)
        self.age = age
    def getAge(self):
        return self.age
class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address
        #To get address
    def getAddress(self):
        return self.address
    #Drive  code
g = GrandChild("Geek1", 23, "Noida")
print(g.getName(), g.getAge(), g.getAddress())
