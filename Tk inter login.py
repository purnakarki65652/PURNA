import tkinter as tk
from tkinter import ttk
#root window
root = tk.Tk()
root.geometry("240x100")
root.title('Login')

# configure the grid

#username
username_label = ttk.Label(root, text="Username:")
username_label.grid(column=0, row=1, padx=5, pady=5)

username_entry = ttk.Entry(root)
username_entry.grid(column=1, row=1, padx=5, pady=5)

#password
password_label = ttk.Label(root, text="Password:")
password_label.grid(column=0, row=2, padx=5,pady=5)

#password Enter
password_entry = ttk.Entry(root)
password_entry.grid(column=1, row=2, padx=5,pady=5)

#login Button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1, row=3, padx=5, pady=5)

root.mainloop()