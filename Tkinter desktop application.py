from tkinter import *
window = Tk()
window.title("Welcome to Nepal Airlines")
window.geometry("600x400") #size of windwos
window.minsize(300,100)#minimize the windows
#window.maxsize(1200,900)#maxmize the windows
window.wm_iconbitmap("favicon.ico")#for window icon
lbl = Label(text="Welcome to Nepal Airlines Corporation")
lbl.grid(column=0, row=0)#
lbl.pack()
window.mainloop()
