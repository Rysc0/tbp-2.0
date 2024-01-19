import tkinter as tk
from tkinter import messagebox
from dbUtil.data import login

class LoginScreen:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.title("Login Screen")
        self.on_login_success = on_login_success

        # Create and place login widgets
        self.label_username = tk.Label(root, text="Username:")
        self.label_username.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_username = tk.Entry(root)
        self.entry_username.grid(row=0, column=1, padx=10, pady=10)

        self.label_password = tk.Label(root, text="Password:")
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_password = tk.Entry(root, show="*")
        self.entry_password.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(root, text="Login", command=self.on_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def on_login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        
        # You can implement your own authentication logic here
        if login(username, password):
            self.on_login_success(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
