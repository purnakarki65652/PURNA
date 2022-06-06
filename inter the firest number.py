from tkinter import *
window = Tk()#object and function
window.title("welcome to nepal airlines")#title text and content

lbl = Label(window, text="Enter First number",font=("Arial Bold",10))#Text and font
lbl.grid(column=0,row=0)#lable column and row size

txt = Entry(window,width=5)
txt.grid(column=0,row=1)

lbl1 = Label(window,text="Enter second number",font=("Arial Bold",10))
lbl1.grid(column=0,row=2)

txt1 = Entry(window,width=5)
txt1.grid(column=0,row=3)

window.mainloop()