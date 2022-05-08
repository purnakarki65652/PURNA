#array function append is used to add items in array function list
fruits = ["apple","Banana","cherry"]
fruits.append("orange")
print(fruits)


# fruits clears
fruits =["apple","banana","cherry"]
fruits.clear()
print(fruits)

#list .copy value
fruits = ["apple","banana", "cherry"]
x = fruits.copy()
print (x)

#list count method
fruits = ["apple","banana","cherry"]
x = fruits.count("banana")
print(x)
y=len(fruits) #count total lenth
print(f"Total length of fruits array is {y}")


# write a program to ask the numbers of user
# add the names by user input
# ask the user to search any names
#if found give result "serch{realname} Found"

number = int(input("How many user name we want to enter :"))
names = []
for i in range(number):
    name = input("enter the Name:")
    names.append(name)
    print(names)
    search = input("enter the name for search:")
    count = names.count(search)
    if count>=1:
        print(f"search {search} Found")
    else:
        print(f"serch {search} Not Found")




