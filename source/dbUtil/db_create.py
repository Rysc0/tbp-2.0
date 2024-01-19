import psycopg2
from psycopg2 import sql

# Replace these values with your PostgreSQL connection details
db_name = "postgres"
user = "postgres"
password = "psql"
host = "localhost"  # usually "localhost" if running on the same machine
port = "5432"  # usually 5432


path = "path_to_script"

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
    new_db_name = "your_new_database"

    # Create a new database
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_db_name)))

    # Commit the changes
    connection.commit()

    print(f"Database '{new_db_name}' created successfully.")

    # Read and execute the SQL script
    with open(path, 'r') as sql_file:
        sql_script = sql_file.read()
        cursor.execute(sql_script)
    connection.commit()

except psycopg2.Error as e:
    print("Error: Unable to connect to the database.")
    print(e)

finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
