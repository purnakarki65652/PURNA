from tkinter import *
from tkinter import Menu

from tkinter import  messagebox #import message called
def openNewWindow():
    #Toplevel object which will be treated as a new window
    NewWindow = Toplevel(window)
#sets the title of the toplovel widget
    NewWindow.title("new window")
#sets the geomtry of toplovel
    NewWindow.geometry("200x200")
# A label widget to show in toplevel
    Label(NewWindow, text="This is a new window").pack()

def save(): #function
    messagebox.showinfo("Saved")

window = Tk()
window.title("Welcome to Dashboard")

menu = Menu(window)
new_item = Menu(menu, tearoff=0)# tearoff remove the ---- line
new_item.add_command(label='New' , command=openNewWindow)
new_item.add_separator()
new_item.add_command(label='Print')
new_item.add_separator()
new_item.add_command(label='copy')
new_item.add_command(label='paste')
new_item.add_separator()
new_item.add_command(label='Save',command=save) #save commadn
new_item.add_command(label='Save as')
new_item.add_command(label='Exit',command=exit)
menu.add_cascade(label='File',menu=new_item)
window.config(menu=menu)
window.mainloop()