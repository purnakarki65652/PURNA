import tkinter as tk
from tkinter import ttk
#root window
root = tk.Tk()
#root.geometry("240x100")
root.title('Login')

# configure the grid

#username
username_label = ttk.Label(root, text="Username *")
username_label.grid(column=0, row=1, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=1, padx=5, pady=5)

#password
password_label = ttk.Label(root, text="Password *")
password_label.grid(column=0, row=2, padx=5,pady=5)

#password Enter
password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=2, padx=5,pady=5)
#status
status_label = ttk.Label(root,text="Status")
status_label.grid(column=0,row=3,padx=5,pady=5)

status_entry = ttk.Entry(root)
status_entry.grid(column=1,row=3, padx=5,pady=5)

#email address
email_label =ttk.Label(root, text="Email")
email_label.grid(column=0,row=4, padx=5, pady=5)
email_entry = ttk.Entry(root)
email_entry.grid(column=1,row=4, padx=5,pady=5)

#phone number
phone_label = ttk.Label(root, text="Phone Number *")
phone_label.grid(column=0,row=5, padx=5, pady=5)
phone_entry = ttk.Entry(root)
phone_entry.grid(column=1,row=5, padx=5,pady=5)

#login Button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=8, padx=5, pady=5)

root.mainloop()