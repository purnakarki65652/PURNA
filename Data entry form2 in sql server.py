import tkinter as tk
from tkinter import ttk

from tkinter import messagebox  #import message box

#check information
def checklogin():
    username = username_entry.get()
    password = password_entry.get()
    if username=="admin" and password=="Password":
        messagebox.showinfo("login","Success")
    else:
        messagebox.showerror("login", "Plese try again")

#root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')
root.resizable(0,0)
# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
#username
username_label = ttk.Label(root,text="Username:")
username_label.grid(column=0,row=0,sticky=tk.W,padx=5,pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=0,row=1, sticky=tk.E,padx=5,pady=5)

#password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=2, sticky=tk.W,padx=5,pady=5)

#password Enter
password_entry = ttk.Entry(root, show="*")
password_entry.grid(column=0, row=1, sticky=tk.E,padx=5,pady=5)

email_label = ttk.Label(root,text="purnakarki100@gmail.com:")
email_label.grid(column=0,row=2,sticky=tk.w,padx=5,pady=5)

email_entry = ttk.Entry(root,show"*")
email_entry.grid(column=0,raw=3,sticky=tk.E,padx=5,pady=5)
#login Button
login_button = ttk.Button(root, text="Login", command=checklogin)
login_button.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

root.mainloop()