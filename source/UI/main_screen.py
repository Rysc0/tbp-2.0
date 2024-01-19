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
        self.EntryName = tk.Label(self.WorkLogLabelFrame, state="disabled", text="John Doe")
        self.EntryName.grid()

 
        self.DatumLabel = tk.Label(self.WorkLogLabelFrame, text='Datum:')
        self.DatumLabel.grid()
        self.calendar = DateEntry(self.WorkLogLabelFrame, selectmode='day', date_pattern='dd/MM/yyyy')
        self.calendar.grid()


        self.StatusLabel = tk.Label(self.WorkLogLabelFrame, text="Status:")
        self.StatusLabel.grid()
        self.statusComboBox = ttk.Combobox(self.WorkLogLabelFrame, state='readonly', values=self.populateStatus())
        self.statusComboBox.set('Odaberi')
        self.statusComboBox.grid()


        self.VoziloLabel = tk.Label(self.WorkLogLabelFrame, text="Vozilo:")
        self.VoziloLabel.grid()
        self.VehicleEntry = ttk.Combobox(self.WorkLogLabelFrame, state='readonly', values=self.populateVozilo())
        self.VehicleEntry.set('Odaberi')
        self.VehicleEntry.grid()


        self.KilometrazaLabel = tk.Label(self.WorkLogLabelFrame, text="Kilometraža:")
        self.KilometrazaLabel.grid()
        self.Distance = ttk.Spinbox(self.WorkLogLabelFrame, from_=0, to=1000, increment=1)
        self.Distance.set(0)
        self.Distance.grid()       


        self.DnevnikLabel = tk.Label(self.WorkLogLabelFrame, text='Dnevnik')
        self.DnevnikLabel.grid(row=10, column=0)
        self.Dnevnik = tk.Text(self.WorkLogLabelFrame, height=8, width=50)
        self.Dnevnik.grid(row=11, column=0)

        self.UpisiButton = tk.Button(self.WorkLogLabelFrame, text="Upisi", command=self.on_upisiButton_click, height=1, width=15)
        self.UpisiButton.grid(row=12, column=0, pady=5)

        # ---------------------------------------------------------------------#
        
        # prazno vert
        tk.Label(self.WorkLogLabelFrame).grid(column=1)

        self.TrosakFrame = tk.LabelFrame(self.WorkLogLabelFrame, border=5, relief=tk.RIDGE, text='Trošak')
        self.TrosakFrame.grid(row=0, column=2, rowspan=70)


        # spinbox
        self.IznosLabel = tk.Label(self.TrosakFrame, text="Iznos:")
        self.IznosLabel.grid(row=0)
        self.IznosSpinBox = ttk.Spinbox(self.TrosakFrame, from_=0, to=1000, increment=1)
        self.IznosSpinBox.set(0)
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
        self.vrstaComboBox = ttk.Combobox(self.TrosakFrame, state='readonly', values=self.populateVrsta())
        self.vrstaComboBox.set('Odaberi')
        self.vrstaComboBox.grid()

        
        # button - dodaj
        self.DodajTrosakButton = tk.Button(self.TrosakFrame, text="Dodaj", command=self.on_dodajButton_click, height=1, width=15)
        self.DodajTrosakButton.grid(pady=10)

        # button - ukloni
        self.UkloniTrosakButton = tk.Button(self.TrosakFrame, text="Ukloni", command=self.on_ukloniButton_click, height=1, width=15)
        self.UkloniTrosakButton.grid()

        # prazno vert
        tk.Label(self.TrosakFrame).grid(column=2)


        # listbox -> kreirani troškovi 
        self.ListaTroskovaLabel = tk.Label(self.TrosakFrame, text='Troškovi:')
        self.ListaTroskovaLabel.grid(row=0, column=3)
        self.TrosakListBox = tk.Listbox(self.TrosakFrame, width=20, height=20)
        self.TrosakListBox.grid(row=1, column=3, rowspan=10)

        # ---------------------------------------------------------------------#

        # Configure row and column weights for resizing
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        self.WorkLogLabelFrame.grid_columnconfigure(3, weight=1)

    
    def populateStatus(self):
        statuses = data.getStatuses()
        statuses = [y[1] for y in statuses]
        return statuses
    
    def populateVozilo(self):
        vozila = data.getVehicleNames()
        vozila = [y[0] for y in vozila]
        return vozila

    def populateVrsta(self):
        vrste = data.getVrstaTroska()
        vrste = [y[1] for y in vrste]
        return vrste


    
    
    def on_change_password(self):
        messagebox.showinfo("Change pass", "Change pass clicked")

    def on_carButton_click(self):
        messagebox.showinfo("Car", "Car clicked")

    def on_isplateButton_click(self):
        messagebox.showinfo("Isplate", "Isplate clicked")

    def on_djelatniciButton_click(self):
        messagebox.showinfo("Klikno si")

    def on_statusButton_click(self):
        messagebox.showinfo("Klikno si")

    def on_dodajButton_click(self):
        messagebox.showinfo("Klikno si")

    def on_ukloniButton_click(self):
        messagebox.showinfo("Klikno si")

    def on_upisiButton_click(self):
        messagebox.showinfo("Klikno si")


