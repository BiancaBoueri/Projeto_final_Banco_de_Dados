from dbConnection import mydb, mycursor 

def insert():
  mycursor.execute("INSERT INTO Map VALUES (11,'Mirror',2)")
  mydb.commit()

def select():
  mycursor.execute("select * from Map")
