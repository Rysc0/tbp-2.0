import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from dbUtil import data
from UI.car_screen import CarScreen
from UI.djelatnici_screen import DjelatniciScreen
from UI.isplate_screen import IsplateScreen
from UI.evidencija_screen import EvidencijaScreen
from UI.changePass import ChangePassScreen

class MainScreen:
    def __init__(self, username):
        self.root = tk.Tk()
        self.root.title("Main Screen")

        self.username = username


        # TODO: Take data from login and pass it here
        self.employee_data = (data.db_getUser(self.username))
        # ---------------------------------------------------------------------#
        self.EmployeeFrame = tk.Frame(self.root, border=5, relief=tk.RIDGE)
        self.EmployeeFrame.grid(row=0, column=0)
        
        self.ime_prezime = tk.Label(self.EmployeeFrame, text="Ime i prezime: \n{}".format(self.employee_data[1]))
        self.ime_prezime.grid(row=0, column=0)
        
        self.email = tk.Label(self.EmployeeFrame, text="Email: \n{}".format(self.employee_data[5]))
        self.email.grid(row=1, column=0)

        self.kontakt = tk.Label(self.EmployeeFrame, text="Kontakt: \n{}".format(self.employee_data[2]))
        self.kontakt.grid(row=2, column=0)

        self.radno_mjesto = tk.Label(self.EmployeeFrame, text="Radno mjesto: \n{}".format(data.getRadnoMjesto(self.employee_data[9]), extract=True))
        self.radno_mjesto.grid(row=3, column=0)

        # TODO: Format radno vrijeme approprietly
        self.radno_vrijeme = tk.Label(self.EmployeeFrame, text="Radno vrijeme: \n{}".format(str(self.employee_data[6])[:-3] + ' - ' + str(self.employee_data[7])[:-3]))
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

        self.IsplatiButton = tk.Button(self.EmployeeFrame, text="Isplati", command=self.on_isplatiButton_click, height=1, width=15)
        self.IsplatiButton.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        # ---------------------------------------------------------------------#

        self.WorkLogLabelFrame = tk.LabelFrame(self.root, border=5, relief=tk.RIDGE, text='WorkLog')
        self.WorkLogLabelFrame.grid(row=0, column=1)


        self.NameLabel = tk.Label(self.WorkLogLabelFrame, text="Ime i prezime:")
        self.NameLabel.grid()
        self.EntryName = tk.Label(self.WorkLogLabelFrame, state="disabled", text=self.username)
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

        self.EvidencijaButton = tk.Button(self.WorkLogLabelFrame, text="Evidencija", command=self.on_evidencijaButton_click, height=1, width=15)
        self.EvidencijaButton.grid()

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
        self.Trcalendar = DateEntry(self.TrosakFrame, selectmode='day', date_pattern='dd/MM/yyyy')
        self.Trcalendar.grid()


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
        self.TrosakListBox.bind("<<ListboxSelect>>", self.on_select_listbox)

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
        changePass = ChangePassScreen()
        changePass.root.mainloop()
        # messagebox.showinfo("Change pass", "Change pass clicked")

    def on_carButton_click(self):
        car_screen = CarScreen()
        car_screen.root.mainloop()
        # messagebox.showinfo("Car", "Car clicked")

    def on_isplateButton_click(self):
        isplate_screen = IsplateScreen(employeeID=self.employee_data[0])
        isplate_screen.root.mainloop()
        # messagebox.showinfo("Isplate", "Isplate clicked")

    def on_djelatniciButton_click(self):
        djelatnici_screen = DjelatniciScreen()
        djelatnici_screen.root.mainloop()


    def on_isplatiButton_click(self):
        data.createIsplata(employeeID=self.employee_data[0])
        messagebox.showinfo("Isplaćeno")




    def on_dodajButton_click(self):
        
        trosak = []
        # iznos
        iznos = self.IznosSpinBox.get()
        
        # datum
        datum = self.Trcalendar.get_date()
    
        # opis
        opis = self.OpisText.get('1.0','end-1c')
        # vrsta
        selected_vrsta = self.vrstaComboBox.get()
        vrsta_id = data.getVrstaTroskaID(selected_vrsta)

        trosak.append([iznos, datum, opis, vrsta_id])
        
        for item in trosak:
            self.TrosakListBox.insert(self.TrosakListBox.size()+1, item)


    def on_select_listbox(self, event):
        selection = event.widget.curselection()

        if selection:
            index = selection[0]
            data = event.widget.get(index)
        
        
        print(index, data, self.createTrosak())


        return index, data
        
   

    def on_ukloniButton_click(self):
        selected_trosak = self.TrosakListBox.curselection()
        index = selected_trosak[0]
        self.TrosakListBox.delete(index, index)


    def createTrosak(self, worklogID):
        items = self.TrosakListBox.get(first=0, last=self.TrosakListBox.size())
        print("items: ", items)
        for item in items:
            id = data.db_insertTrosak(item, worklogID)
            print("inserter trosak id: ", id)



    def on_upisiButton_click(self):
        # employeeID
        
        # ime i prezime

        # datum
        selected_date = self.calendar.get_date()
        # status
        selected_status = self.statusComboBox.get()
        statusID = data.getStatusID(selected_status)
        # vozilo
        selected_vehicle = self.VehicleEntry.get()
        vehicleID = data.getVehicleID(selected_vehicle)
        # kilometraža
        try:
            selected_distance = self.Distance.get()
        except:
            selected_distance = None
        # Dnevnik
        journal = self.Dnevnik.get('1.0','end-1c')
        # Trošak

        
        # troškovi
        # TODO: Kreiranje troškova i worklog-a
        created_worklog_id = data.createWorkLog(employeeID=self.employee_data[0],
                           date=selected_date, status=statusID, vehicle=vehicleID,
                           kilometraza=selected_distance, dnevnik=journal)
       
        self.createTrosak(created_worklog_id)

        messagebox.showinfo("Upisano")

        # Obriši inpute nakon unosa
        self.Distance.set(0)
        self.Dnevnik.delete('1.0', 'end-1c')
        self.statusComboBox.set('Odaberi')
        self.VehicleEntry.set('Odaberi')

        self.IznosSpinBox.set(0)
        self.OpisText.delete('1.0','end-1c')
        self.vrstaComboBox.set('Odaberi')
        self.TrosakListBox.delete(0, self.TrosakListBox.size())
        return

    def on_evidencijaButton_click(self):
        evidencija_screen = EvidencijaScreen(self.employee_data[0])
        evidencija_screen.root.mainloop()
        


