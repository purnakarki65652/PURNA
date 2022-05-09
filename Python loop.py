##looping concept
x=0
#define a while loop
while(x<10):
    print(x)
    if x==3:
        break
    x=x+1
#CONTINUSE LOOPING
x=0
while(x<10):
 x= x+1
 if x ==3:
     continue
 print(x)

#For loop
for y in range(6):
      if y == 7: break
      print(y)
else:
      print("finished")


# For with else
for y in range(6):
    if y == 3: break
    print(y)
else:
    print("finished")
adj = ["red", "big", "testy"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)