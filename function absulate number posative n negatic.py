#print absolute value
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >=0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))

#variable scope
def my_func():
    x = 10 #local scope
    print("value inside function:",x)
x = 20 #globle scope
my_func()
print("value outside function:",x)

# default argument
def sum1(num1=10,num2=30):
    sum = num1+num2
    return sum
total =sum1()
print(f"The total number is {total}")

#python arbitrary arguments
def greet(*names):
    """This function greets all the person in the names tuple."""
    #Names is a tuple with arguments
    for name in names:
        print("Hello",name)
greet("monica","luke","steve","john")

#create a nonlocal variable
#This mesans tha the variable can be neither in the local nor the globle scope.
def outer():
    x = "local"
    def inner():
        #nonlocal x
        x = "nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)
outer()

#Changing global variable from inside a function
c = 1
def add():
    global c
    c = c + 2 # increment by 2
    print("inside add():",c)
add()
print("in main:", c)
