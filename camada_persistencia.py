import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",password="password",database="maplestory")

mycursor = mydb.cursor()

mycursor.execute("INSERT INTO Map VALUES (4,'Mirror',2)")
mydb.commit()

mycursor.execute("select * from Map")

for i in mycursor: 
  print (i)
