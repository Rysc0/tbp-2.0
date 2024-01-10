import tkinter as tk
from tkinter import ttk, messagebox

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Screen")

        # Create and place buttons on the left side
        self.button1 = tk.Button(root, text="Button 1", command=self.on_button1_click)
        self.button1.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.button2 = tk.Button(root, text="Button 2", command=self.on_button2_click)
        self.button2.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.button3 = tk.Button(root, text="Button 3", command=self.on_button3_click)
        self.button3.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        # Create and place a search bar on the right side
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(root, textvariable=self.search_var, width=20)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.search_button = tk.Button(root, text="Search", command=self.on_search_click)
        self.search_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Create and place an empty space for a table below the search bar
        self.tree = ttk.Treeview(root, columns=("Column 1", "Column 2"), show="headings")
        self.tree.heading("Column 1", text="Column 1")
        self.tree.heading("Column 2", text="Column 2")
        self.tree.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Configure row and column weights for resizing
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def on_button1_click(self):
        messagebox.showinfo("Button 1", "Button 1 clicked")

    def on_button2_click(self):
        messagebox.showinfo("Button 2", "Button 2 clicked")

    def on_button3_click(self):
        messagebox.showinfo("Button 3", "Button 3 clicked")

    def on_search_click(self):
        # Handle search button click
        search_text = self.search_var.get()
        print(f"Searching for: {search_text}")
