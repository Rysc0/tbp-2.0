import tkinter as tk
from tkinter import ttk, messagebox
from dbUtil import data as db

class IsplateScreen:
    def __init__(self, employeeID):
        self.root = tk.Tk()
        self.root.title("Isplate Screen")
        self.employeeID = employeeID

        # Create a Treeview widget
        columns = ("ID", "Ime i prezime", "Datum", "Plaća")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)  # Adjust the width as needed

        # Insert sample data into the table
        record = db.getIsplataForEmployee(self.employeeID)
        ime = db.db_getEmployeesData(ID=self.employeeID)
        for item in record:
            item[1] = ime[1]
        # record[1] = ime[1]

        # get placa
        if len(record) > 1:
            paycheck = db.getPayCheck(record[0][3])
            for item in record:
                item[3] = paycheck[1]
            data = [tuple(x) for x in record]
        else:
            paycheck = db.getPayCheck(record[3])
            record[3] = paycheck[1]

            data = [tuple(record)]

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