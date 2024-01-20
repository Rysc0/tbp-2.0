import tkinter as tk
from tkinter import ttk, messagebox
from dbUtil import data as db

class DjelatniciScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Djelatnici Screen")

        # Create a Treeview widget
        columns = ("ID", "Ime i prezime", "Kontakt", "Plaća", 
                   "Lozinka", "Email", "Radno vrijeme P", "Radno vrijeme K", 
                   "Vozilo", "Radno mjesto", "Zaposlen")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  # Adjust the width as needed

        # Insert sample data into the table
        data = db.db_getAllEmployeesData()

        for item in data:
            self.tree.insert("", "end", values=item)

        # Bind the on_select function to the treeview selection event
        self.tree.bind("<ButtonRelease-1>", self.on_select)

        # Pack the treeview widget
        self.tree.pack(expand=True, fill="both")

        # # Run the Tkinter event loop
        # root.mainloop()


    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_values = self.tree.item(selected_item)['values']
            print(f"Selected: {item_values}")