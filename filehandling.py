# A file name "test", will be opened with the reading mode.
file = open('test.txt' , 'r')
# This will print every line one by one in the file
for each in file:
    print(each)
#Reading content from different location
file2 = open(r"D:\reading\help.txt" ,"r")
#for hlp in file2:
   # print(hlp)
    #or
#print(file2.read()) #read method is used to read or print the content

#print(file2.read(5)) # reads five character only
#print(file2.read()) # read all the files content


#python code to crate a file and overwrite
#file = open('test.txt', 'w')
#file.write("This is the write command \n")
#file.write("It allows us to write in a particular file")
#file.close()

#python code to crate a A+
file = open('test.txt', 'a+')
file.write("This is the write command \n")
file.write("It allows us to write in a particular file")
file.close()

#python code to illustrate split()function
with open("test.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

