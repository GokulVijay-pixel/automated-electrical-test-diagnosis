import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def create_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="engineering_test_db"
    )

    return connection