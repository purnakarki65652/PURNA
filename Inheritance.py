class Person(object):
    #constructor
    def __init__(self, name):
        self.name = name
    # To get name
    def getName(self):
            return self.name
    # To check if this person is an employee
    def isEmployee(self):
            return False
    # Inherited or subclass (Note person in bracket)
class Employee(Person):
    #here we return true
    def isEmployee(self):
        return True
    # Drive code
emp = Person("Geek1") #An object  of  person
print(emp.getName(), emp.isEmployee())
emp = Employee("Geek2") #AN object of employee
print(emp.getName(),emp.isEmployee())