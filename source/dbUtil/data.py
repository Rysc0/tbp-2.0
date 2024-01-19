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
    
    else:
        result = cursor.fetchone()
    
    db_close(connect)
    result = convertToList(result)
    return result


def convertToList(inputList):
    lenght = len(inputList)

    if lenght > 1:
        new_list = []
        for item in inputList:
            item = list(item)
            new_list.append(item)
        return new_list

    else:
        new_list = list(inputList[0])
        return new_list


def db_getEmployeesData():
    querry = 'SELECT * FROM public."Zaposlenik"'
    data = db_executeQuery(query=querry, fetchAll= True)
    print(data)
    return data

def db_getEmployeesData(ID=-1, Name=None):
    querry = '''SELECT * FROM public."Zaposlenik"
where "ID" = {} or "Ime i prezime" LIKE '%{}%';'''.format(ID, Name)
    data = db_executeQuery(query=querry, fetchAll= True)
    print(data)
    return data

