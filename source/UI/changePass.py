import tkinter as tk
from tkinter import ttk, messagebox
from dbUtil import data

class ChangePassScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Change Password")


        # Entry for old password
        self.label_old_password = tk.Label(self.root, text="Old Password:")
        self.label_old_password.pack(pady=5)
        self.entry_old_password = tk.Entry(self.root, show="*")
        self.entry_old_password.pack(pady=5)

        # Entry for new password
        self.label_new_password = tk.Label(self.root, text="New Password:")
        self.label_new_password.pack(pady=5)
        self.entry_new_password = tk.Entry(self.root, show="*")
        self.entry_new_password.pack(pady=5)

        # Submit and Cancel buttons
        btn_submit = tk.Button(self.root, text="Submit", command=self.change_password)
        btn_submit.pack(side=tk.LEFT, padx=10)
        btn_cancel = tk.Button(self.root, text="Cancel", command=self.cancel_password_change)
        btn_cancel.pack(side=tk.RIGHT, padx=10)

    def change_password(self):
        old_password = self.entry_old_password.get()
        new_password = self.entry_new_password.get()

        # Perform password change logic here
        # For demonstration, simply print the old and new passwords
        # print(f"Old Password: {old_password}")
        # print(f"New Password: {new_password}")

        # You can add your password change logic here, such as updating a database

        # Show a message box indicating successful password change
        messagebox.showinfo("Password Change", "Password changed successfully!")
        self.root.destroy()

    def cancel_password_change(self):
        self.root.destroy()