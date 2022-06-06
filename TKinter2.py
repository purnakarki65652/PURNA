from tkinter import *#default function
def clicked():
    lbl.configure(text="Button was clicked !!")
    res = "welcome to" + txt.get()
    lbl.configure(text=res)
window = Tk()#object and function
window.title("welcome to nepal airlines")#title text and content
lbl = Label(window, text="Hello",font=("Arial Bold",50))#Text and font
lbl.grid(column=0,row=0)#lable column and row size
lbl1= Label(window, text="world",font=("Arial Bold",50))
lbl1.grid(column=3,row=1)#column and row size
#TextBox entry
txt = Entry(window,width=30)
txt.grid(column=5, row=5)

btn = Button(window, text="Click here",bg="green", fg="red",command=clicked)#adding button
btn.grid(column=7,row=3)
window.mainloop()
