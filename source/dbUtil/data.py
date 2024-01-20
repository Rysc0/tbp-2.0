import psycopg2 as db



def db_connect():
    connection = db.connect(dbname="postgres", user="postgres", password="psql", host="localhost", port=5432)
    return connection


def db_close(connection):
    connection.close()
    return 

def db_executeQuery(query, fetchAll = False):
    connect = db_connect()
    cursor = connect.cursor()
    cursor.execute(query=query)

    if fetchAll:
        result = cursor.fetchall()
        result = convertToList(result)
    
    else:
        result = cursor.fetchone()
        if result == None:
            return None
        result = list(result)
 
    db_close(connect)

    return result

def db_fetch(query):
    connect = db_connect()
    cursor = connect.cursor()
    cursor.execute(query=query)

    result = list(cursor.fetchall())
    db_close(connect)

    return result



def convertToList(inputList, full = False):
    lenght = len(inputList)
    
    if full:
        new_list = list(inputList)
        return new_list

    if lenght > 1:
        new_list = []
        for item in inputList:
            item = list(item)
            new_list.append(item)
        return new_list

    else:
        new_list = list(inputList[0])
        return new_list

    

def login(user, password):
    auth = '''SELECT "Ime i prezime" FROM public."Zaposlenik"
    WHERE "Ime i prezime" = '{}' AND "Lozinka" = '{}';'''.format(user, password)
    data = db_executeQuery(auth)
    
    # validate
    if data is not None and len(data) > 0 and user in data:
        return True

    return False


def db_getAllEmployeesData():
    querry = 'SELECT * FROM public."Zaposlenik"'      
    data = db_fetch(query=querry)
    print(data)
    return data

def db_getEmployeesData(ID=-1, Name=None):
    querry = '''SELECT * FROM public."Zaposlenik"
where "ID" = {} or "Ime i prezime" LIKE '%{}%';'''.format(ID, Name)
    data = db_executeQuery(query=querry, fetchAll= True)
    print(data)
    return data

def db_getUser(username):
    querry = '''SELECT * FROM public."Zaposlenik"
where "Ime i prezime" LIKE '%{}%';'''.format(username)
    data = db_executeQuery(querry)
    return data

def getRadnoMjesto(id):
    query = '''SELECT * FROM public."Radno mjesto" 
where "ID" = {};'''.format(id)
    data = db_executeQuery(query)
    return data[1]

def getStatuses():
    status = 'SELECT * FROM public."Status";'
    data = db_executeQuery(status, True)
    return data

def getVehicles():
    query = '''SELECT * FROM public."Vozilo";'''
    data = db_executeQuery(query, True)
    return data

def getVehicleNames():
    vehicle = 'SELECT "Marka" FROM public."Vozilo";'
    data = db_executeQuery(vehicle, True)
    return data

def getVrstaTroska():
    expense = 'SELECT * FROM public."Trošak_Vrsta";'
    data = db_executeQuery(expense, True)
    return data

def getIsplataForEmployee(employeeID):
    query = '''SELECT * FROM public."Isplata"
WHERE "ZaposlenikID" = {};'''.format(employeeID)
    data = db_executeQuery(query, True)
    return data

def getPayCheck(paycheckID):
    query = '''SELECT * FROM public."Plaća"
WHERE "ID" = {};'''.format(paycheckID)
    data = db_executeQuery(query)
    return data

