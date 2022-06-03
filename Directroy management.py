import os
import shutil
if not os.path.isdir("helpme"):
    os.makdir("helpme")
path = os.chdir("D:\pythonProject1\Purna\helpme")
file = open('helpme.txt', 'w') #read directory
print(path)
print(os.listdir("D:\pythonProject1\Purna\helpme")) # it show file of directory

# python code to crate a file and override
file = open('helpme.txt','w') #open file
file.write("This is the write command")# file content
file.write("It allows us to write in a particular file") # helpme file name content
file.close() # close helpme.txt dir
os.chdir("D:\pythonProject1\Purna") #exit from helpme dir to Purna dir
print(os.getcwd())# print current working dir
shutil.rmtree("helpme") #delete tree dir and content
