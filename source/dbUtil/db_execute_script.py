import psycopg2
from psycopg2 import sql

# Replace these values with your PostgreSQL connection details
db_name = "your_new_database"
user = "postgres"
password = "psql"
host = "localhost"  # usually "localhost" if running on the same machine
port = 5432  # usually 5432

# Path to your SQL script file
sql_script_path = "path_to_script"

# Establish a connection to PostgreSQL in autocommit mode
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

    # Read and execute the SQL script
    with open(sql_script_path, 'r') as sql_file:
        sql_script = sql_file.read()
        cursor.execute(sql_script)

    print("SQL script executed successfully.")

except psycopg2.Error as e:
    print("Error: Unable to connect to the database or execute the script.")
    print(e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
