#basic function example
def greet(name): #name means paramater #greet means user define function
    """
    This function greets to
    the program pased in as    
    a parameter
    """ # docstring
    print("Hello," + name +". Good morning!") #function statement
name = input("ente your name?")
greet("purna") #function call




#print absolute value
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >=0:
        return num #return means print required address
    else:
        return -num
    print(absolute_value(2))
    print(absolute_value(-4))