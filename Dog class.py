class Dog: #class
#class variable
    animal ='dog'
#This init method or construtor
    def __init__(self, breed,color):
#instance variable
        self.breed = breed
        self.color = color
# objects of Dog class
Rodger = Dog("Pug","brown")
Buzo = Dog("Bulldog", "black")
print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('color:',Rodger.color)
print('\nBuzo details:')