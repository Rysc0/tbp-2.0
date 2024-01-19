import tkinter as tk
from tkinter import ttk, messagebox
from dbUtil import data

class MainScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Screen")

        # TODO: Take data from login and pass it here
        employee_data = (data.db_getEmployeesData(Name='John Doe'))
        
        self.ime_prezime = tk.Label(self.root, text="Ime i prezime: \n{}".format(employee_data[1]))
        self.ime_prezime.grid(row=0, column=0)
        
        self.email = tk.Label(self.root, text="Email: \n{}".format(employee_data[5]))
        self.email.grid(row=1, column=0)

        self.kontakt = tk.Label(self.root, text="Kontakt: \n{}".format(employee_data[2]))
        self.kontakt.grid(row=2, column=0)

        self.radno_mjesto = tk.Label(self.root, text="Radno mjesto: \n{}".format(employee_data[9]))
        self.radno_mjesto.grid(row=3, column=0)

        # TODO: Format radno vrijeme approprietly
        self.radno_vrijeme = tk.Label(self.root, text="Radno vrijeme: \n{}".format(str(employee_data[6])[:-3] + ' - ' + str(employee_data[7])[:-3]))
        self.radno_vrijeme.grid(row=4, column=0)




        # Create and place buttons on the left side
        self.changePass = tk.Button(self.root, text="Change Password", command=self.on_change_password, height=1, width=15)
        self.changePass.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.carButton = tk.Button(self.root, text="Car", command=self.on_carButton_click, height=1, width=15)
        self.carButton.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.isplateButton = tk.Button(self.root, text="Isplate", command=self.on_isplateButton_click, height=1, width=15)
        self.isplateButton.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.djelatniciButton = tk.Button(self.root, text="Djelatnici", command=self.on_djelatniciButton_click, height=1, width=15)
        self.djelatniciButton.grid(row=8, column=0, padx=10, pady=5, sticky="w")

        # Create and place a search bar on the right side
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(self.root, textvariable=self.search_var, width=20)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.search_button = tk.Button(self.root, text="Search", command=self.on_search_click)
        self.search_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # # Create and place an empty space for a table below the search bar
        # self.tree = ttk.Treeview(self.root, columns=("Column 1", "Column 2"), show="headings")
        # self.tree.heading("Column 1", text="Column 1")
        # self.tree.heading("Column 2", text="Column 2")
        # self.tree.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Configure row and column weights for resizing
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def on_change_password(self):
        messagebox.showinfo("Change pass", "Change pass clicked")

    def on_carButton_click(self):
        messagebox.showinfo("Car", "Car clicked")

    def on_isplateButton_click(self):
        messagebox.showinfo("Isplate", "Isplate clicked")

    def on_djelatniciButton_click(self):
        messagebox.showinfo("Klikno si")

    def on_search_click(self):
        # Handle search button click
        search_text = self.search_var.get()
        print(f"Searching for: {search_text}")
