import array
balance = array.array('i',[300,200,100,400,500,1,3])
print (balance [1])
for i in balance:
    print(i, end = " ")

#insert array
balance .insert(2,150)
print(balance[:])

#modifiy array element
balance[0]=100
print(balance[:])

#Array concatenation
first =array.array('b',[4,6,9,5,6,55,7])
second = array.array('b',[9,12,15])
numbers = array.array('b')
numbers = first + second
print(numbers)

#Removing items for on array
first.pop(2)
print(first)

#Delete the items
del first [1]
print(first)


#remove array items by value
numbers.remove(6)
print(numbers)
print("the length of the array is ", len(numbers))