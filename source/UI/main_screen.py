import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from dbUtil import data

class MainScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Screen")

        # TODO: Take data from login and pass it here
        employee_data = (data.db_getEmployeesData(Name='John Doe'))
        # ---------------------------------------------------------------------#
        self.EmployeeFrame = tk.Frame(self.root, border=5, relief=tk.RIDGE)
        self.EmployeeFrame.grid(row=0, column=0)
        
        self.ime_prezime = tk.Label(self.EmployeeFrame, text="Ime i prezime: \n{}".format(employee_data[1]))
        self.ime_prezime.grid(row=0, column=0)
        
        self.email = tk.Label(self.EmployeeFrame, text="Email: \n{}".format(employee_data[5]))
        self.email.grid(row=1, column=0)

        self.kontakt = tk.Label(self.EmployeeFrame, text="Kontakt: \n{}".format(employee_data[2]))
        self.kontakt.grid(row=2, column=0)

        self.radno_mjesto = tk.Label(self.EmployeeFrame, text="Radno mjesto: \n{}".format(employee_data[9]))
        self.radno_mjesto.grid(row=3, column=0)

        # TODO: Format radno vrijeme approprietly
        self.radno_vrijeme = tk.Label(self.EmployeeFrame, text="Radno vrijeme: \n{}".format(str(employee_data[6])[:-3] + ' - ' + str(employee_data[7])[:-3]))
        self.radno_vrijeme.grid(row=4, column=0)


        # Create and place buttons on the left side
        self.changePass = tk.Button(self.EmployeeFrame, text="Change Password", command=self.on_change_password, height=1, width=15)
        self.changePass.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        self.carButton = tk.Button(self.EmployeeFrame, text="Car", command=self.on_carButton_click, height=1, width=15)
        self.carButton.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        self.isplateButton = tk.Button(self.EmployeeFrame, text="Isplate", command=self.on_isplateButton_click, height=1, width=15)
        self.isplateButton.grid(row=7, column=0, padx=10, pady=5, sticky="w")

        self.djelatniciButton = tk.Button(self.EmployeeFrame, text="Djelatnici", command=self.on_djelatniciButton_click, height=1, width=15)
        self.djelatniciButton.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        # ---------------------------------------------------------------------#

        self.WorkLogLabelFrame = tk.LabelFrame(self.root, border=5, relief=tk.RIDGE, text='WorkLog')
        self.WorkLogLabelFrame.grid(row=0, column=1)


        self.NameLabel = tk.Label(self.WorkLogLabelFrame, text="Ime i prezime:")
        self.NameLabel.grid()
        self.EntryName = tk.Entry(self.WorkLogLabelFrame, state="disabled")
        self.EntryName.grid()

        # TODO: datum 
        self.TrosakLabel = tk.Label(self.WorkLogLabelFrame, text='Datum:')
        self.TrosakLabel.grid()
        self.calendar = DateEntry(self.WorkLogLabelFrame, selectmode='day', date_pattern='dd/MM/yyyy')
        self.calendar.grid()

        self.StatusLabel = tk.Label(self.WorkLogLabelFrame, text="Status:")
        self.StatusLabel.grid()
        self.statusComboBox = ttk.Combobox(self.WorkLogLabelFrame)
        self.statusComboBox.grid()


        self.VoziloLabel = tk.Label(self.WorkLogLabelFrame, text="Vozilo:")
        self.VoziloLabel.grid()
        self.VehicleEntry = tk.Entry(self.WorkLogLabelFrame)
        self.VehicleEntry.grid()


        self.KilometrazaLabel = tk.Label(self.WorkLogLabelFrame, text="Kilometraža:")
        self.KilometrazaLabel.grid()
        self.Distance = ttk.Spinbox(self.WorkLogLabelFrame, from_=0, to=1000, increment=1)
        self.Distance.grid()

        # TODO: Trošak


        self.DnevnikLabel = tk.Label(self.WorkLogLabelFrame, text='Dnevnik')
        self.DnevnikLabel.grid(row=0, column=1)
        self.Dnevnik = tk.Text(self.WorkLogLabelFrame, height=5, width=30)
        self.Dnevnik.grid(row=1, column=1)

        # ---------------------------------------------------------------------#

        self.TrosakFrame = tk.LabelFrame(self.WorkLogLabelFrame, border=5, relief=tk.RIDGE, text='Trošak')
        self.TrosakFrame.grid(row=3, column=1)


        # spinbox
        self.IznosLabel = tk.Label(self.TrosakFrame, text="Iznos:")
        self.IznosLabel.grid(row=0)
        self.IznosSpinBox = ttk.Spinbox(self.TrosakFrame, from_=0, to=1000, increment=1)
        self.IznosSpinBox.grid(row=1)


        # datum
        self.TrosakDatumLabel = tk.Label(self.TrosakFrame, text='Datum:')
        self.TrosakDatumLabel.grid()
        self.calendar = DateEntry(self.TrosakFrame, selectmode='day', date_pattern='dd/MM/yyyy')
        self.calendar.grid()


        # Text
        self.OpisLabel = tk.Label(self.TrosakFrame, text='Opis')
        self.OpisLabel.grid()
        self.OpisText = tk.Text(self.TrosakFrame, height=5, width=30)
        self.OpisText.grid()

        
        # combobox
        self.VrstaTroskaLabel = tk.Label(self.TrosakFrame, text="Vrsta:")
        self.VrstaTroskaLabel.grid()
        self.statusComboBox = ttk.Combobox(self.TrosakFrame)
        self.statusComboBox.grid()

        
        # button - dodaj
        self.DodajTrosakButton = tk.Button(self.TrosakFrame, text="Dodaj", height=1, width=15)
        self.DodajTrosakButton.grid(pady=10)

        # button - ukloni
        self.UkloniTrosakButton = tk.Button(self.TrosakFrame, text="Ukloni", height=1, width=15)
        self.UkloniTrosakButton.grid()

        # prazno vert
        tk.Label(self.TrosakFrame).grid(column=2)


        # listbox -> kreirani troškovi 
        self.ListaTroskovaLabel = tk.Label(self.TrosakFrame, text='Troškovi:')
        self.ListaTroskovaLabel.grid(row=0, column=3)
        self.TrosakListBox = tk.Listbox(self.TrosakFrame, width=20, height=10)
        self.TrosakListBox.grid(row=1, column=3, rowspan=10)

        # ---------------------------------------------------------------------#

        # Configure row and column weights for resizing
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.WorkLogLabelFrame.grid_columnconfigure(3, weight=1)

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
