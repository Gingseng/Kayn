import mysql.connector

db= mysql.connector.connect(
    host="",
    user="",
    passwd=""
    database=""
)

cursor = db.cursor()

def criarbase():
    cursor.execute("CREATE DATABASE infos")

    criarbase()