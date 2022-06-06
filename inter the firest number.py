from tkinter import *
window = Tk()#object and function
window.title("welcome to nepal airlines")#title text and content
lbl = Label(window, text="Enter the First number",font=("Arial Bold",20))#Text and font
lbl.grid(column=0,row=0)#lable column and row size
lbl1 = Label(window,text="Enter the second number",font=("Arial Bold",20))
lbl1.grid(column=0,row=2)
txt = Entry(window,width=10,)
txt.grid(column=1,row=1)

window.mainloop()