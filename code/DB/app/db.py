import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='user', #your_username
        password='1234', #your_password
        database='codingon' #your_database_name
    )