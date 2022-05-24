text = "    wlcome to Guru99    " #remove white spaces from lest and right
print(text.strip())


text="madam" # remove left and right m character
print(text.strip("m"))

text="madam"
print(text.strip("ma")) # remove ma left and side


text="madam"
print(text.strip("a")) # not remove a left and right sied bqz strip function remove first and last character


#count function
url ="https://www.yahoo.com"
url1 ="https://www.facebook.com"
url2 ="https://www.nepaltracking.com"
Inventry ="Table sdfjkldsjf Table Table"
print(url.count("o"))
print(url.count("w", 9))
print("found",Inventry.count("Table"),"Table")


#format function is put the value in carly bracket
print("welcome to {} ".format("Laba"))
print("welcome to Guru {} .".format("99"))
print("welcome to {name}{num}.".format(name="guru", num="99"))
print("welcome to {0}{1} .".format("Guru","99"))
print("{} is {} new kind of {} exprience!".format("Guru99", "totally","learning"))

print("The binary to decimal value is : {:d}".format(0b11)) #Binary to decimal conversion
print("The decimal to binary is : {:b}".format(16)) #Decimal to binary conversion
print("the value is : {:.3f}".format(40.2452525222)) # Remove number after dot (3 chareacter)
print("The value is : {:.0%}".format(0.80))# persentage
print("The value is : {:_}".format(1000000))# seprated -
print("The value is : {:,}".format(1000000))#seprated ,
print("The value is : {:10}".format(40)) #10 space in before 10
print("The value is : {:-}".format(-40))
print("The value is : {:+}".format(40))
print("The value is : {:=}".format(-40))


print("I have {:5} dogs and {:5} cat".format(2,1)) # I have (5space) 2 dogs and (5space) 1 cat

str1 = "welcome to laba training center"
print("The length of the string is :",len(str1))


#string
center ="laba"
print("we are learning at %s ."%(center))