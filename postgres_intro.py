import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

# Environment variables
POSTGRESQL_PASSWORD=os.getenv("POSTGRESQL_PASSWORD")
# print(POSTGRESQL_PASSWORD)

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="admin",
    password=POSTGRESQL_PASSWORD)

conn.autocommit = True

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Preparing query to create a database
sql = '''CREATE DATABASE ksprojects''';

# Creating a database
cursor.execute(sql)
print("Database created successfully........")

# Closing the connection
conn.close()