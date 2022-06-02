import os
#renaming the test.txt to purna.txt
if os.path.exists('test.txt'):
    os.rename('test.txt','purna1.txt') #renaming a file name

#delete the file
if os.path.exists('purna1.txt'):
    os.remove('purna1.txt')
path="admin123"
isExit = os.path.exists(path)
if not isExit:
    os.makedirs(path)
    print(path, "Directory created")
else:
    print(path,"admin directory already exits")
print(os.listdir("admin123")) #show the admin123 file in directory

print(os.listdir("D:\pythonProject1\Purna"))#to show files in dir Purna


print(os.listdir("./admin123"))

#print(os.listdirD:\pythonProject1\Purna )
for x in os.listdir("D:\pythonProject1\Purna"):
    print(x)
for x in os.listdir("D:\pythonProject1\Purna"):
    if os.path.isfile(x): print('file-',x)
    elif os.path.isdir(x): print("Directory -",x)
    else: print("---D:\pythonProject1\Purna---", x)

#creating a file
file1 = open("test.txt","w")
L = [" This is delhi \n","This is paris \n", "This is London \n"]

#Writing data to a file
file1.write("Hello \n")
file1.writelines(L)
file1.close()#to change file access modes
file1 = open("test.txt", "r+")
print("Output of Read function is ")
print(file1.read())
print()
#seek(n) takes the file handle to the nth
#bite from the beginning
file1.seek(0)
print("output of readline function is")
print(file1.readline())
print()
file1.seek(0)
#To show difference between read and readline
print("output of tad(9) function is")
print(file1.read(9))
print()
file1.seek(0)
print("output of readline(9) function is")
print(file1.readline(9))
print()
file1.seek(0)
#readline function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()