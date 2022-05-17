class Dog:#simple class
    #attribute
    attr1 = "mammal"
    attr2 = "dog"
    def fun (self): #simple method
        print("I am a", self.attr1)
        print("I am a", self.attr2)

Rodger = Dog()# Object instantiation

print(Rodger.attr1)#accessing class attributes
Rodger.fun()# method through objects