import datetime
#get current date and time
datetime_object = datetime.datetime.now()
print(datetime_object)

#Get current date
datetime_object = datetime.date.today()
print(datetime_object)

print(dir(datetime))#module information
# current date and time format
now = datetime.datetime.now()
t=now.strftime("%H:%M:%S")
print("current time",t)

