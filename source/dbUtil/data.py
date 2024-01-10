import psycopg2 as db



def db_connect():
    connection = db.connect(dbname="postgres", user="postgres", password="psql", host="localhost", port=5432)
    return connection


def db_close(connection):
    connection.close()
    return 


