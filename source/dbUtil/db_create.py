import psycopg2
from psycopg2 import sql

# Replace these values with your PostgreSQL connection details
db_name = "postgres"
user = "postgres"
password = "psql"
host = "localhost"  
port = "5432"  


# Establish a connection to PostgreSQL
try:
    connection = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
     # Set autocommit mode
    connection.autocommit = True

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Replace "your_new_database" with the name you want for your new database
    new_db_name = "baza"

    # Create a new database
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))

    # Commit the changes
    connection.commit()

    print(f"Database '{new_db_name}' created successfully.")


except psycopg2.Error as e:
    print("Error: Unable to connect to the database.")
    print(e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
