fruits = ['apple','banana','cherry']
fruits.reverse()
print(fruits)

#array sort method
cars = ['fod','BMW','Volvo']
cars.sort(reverse=True)
print(cars)

#returns the length if the value short lenght of value is print frist:
def myFunc(e):
    return len(e)
cars = ['ford','mitsuvishi','BMW','VM']
cars.sort(key=myFunc)
print(cars)