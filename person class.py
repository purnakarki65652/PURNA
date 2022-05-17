class Person: #init method or constructor
    def __init__(self, na):
        self.name = na
      #sample method
    def say_hi(self):
        print('Hello my name is', self.name)
p = Person('Purna')
p.say_hi("")