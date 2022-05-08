#find the greatest number
num = int(int)
num1 = int(input("Enter the first Number: "))
num2=  int(input("Enter the second Number: "))
num3=  int(input("Enter the second Number: "))
if(num1>=num2 and num1>=num3):
    print("{0} is greater than {1} and {2}".format(num1, num2, num3))
elif(num2>=num3 and num2>=num1):
    print("{0} is greater than {1} and {2}".format(num2, num1, num3))
else:
    print("{0} is greater than {1} and {2}".format(num3, num2, num1))