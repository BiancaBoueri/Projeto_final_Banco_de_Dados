import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",password="password",database="maplestory")
mycursor = mydb.cursor(buffered=True)

if mydb is not None:
    print('Connected Successfully')
else:
    print('Connection Failed')
