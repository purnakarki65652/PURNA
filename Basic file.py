#multiple statement on a single line
import sys
x= 'foo'
sys.stdout.write(x+'\n')
import sys; x ='foo'; sys.stdout.write(x +'\n')



#variable declaration
counter =100 #an integer number
miles =1000.00 # A floating point
Name = "John" # A string
print (counter); print(miles)
print (Name)


counter =100 #an integer number
miles =1000.00 # A floating point
Name = "John" # A string
print (counter," Integer",miles," floating point",Name,"Name")

#Multiple Assignment
a=b=c=1;
name,address,gener ="dharma", "Kathmand" ,",mail"
print(1)


str = 'purna karki'
print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])    # Prints characters starting from 3rd to 5th
print (str[2:])     # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string




#Python list

list = ['i am purna karki',456,2.4,'purna',40.2]
tinylist =[123,'purna']
print (list)   #prints complete list
print (list [0]) # print first element of the list
print (list[1:3]) #prints elements starting from 2nd till 3rd
print (list[2:]) # print elements startin from 3rd element
print (tinylist * 2) #print list two time
print (list+ tinylist) #prints concatenated lists

#printing all list items by using for loop
for x  in range(len(list)):
    print (list[x])

# or
print(*list,sep=" , ")
#printig the list in new line


#Python tuple

tuple = ('purnakarki',456,2.4,'purna',40.2)
tuplelist =(123,'purna')
print(tuple)   #prints complete tuple
print(tuple[0]) # print first element of the list
print(tuple[1:3] )#prints elements starting from 2nd till 3rd
print(tuple[2:] ) # print elements starting from 3rd element
print(tinytuple * 2) #print tuple two time
print(tuple+ tinytuple) #prints concatenated lists

print("length of the tuple is:")
print(len(tuple))

#printing all tuples items by using for loop
for x in range(len(tuple)):
    print (tuple[x])
