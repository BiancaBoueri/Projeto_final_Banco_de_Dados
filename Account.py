from dbConnection import mydb, mycursor 

def insert(username, password, profilePicture, creationDate, localization, preferredLanguage, PIN):
  sql = "INSERT INTO Account VALUES (%s,%s,%s,%s,%s,%s,%s)"
  vals = (username, password, profilePicture, creationDate, localization, preferredLanguage, PIN)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(username, password, profilePicture, localization, preferredLanguage, PIN):
  if(password):
    sql = "UPDATE Account SET password = %s WHERE username = %s"
    vals = (password,username)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(profilePicture):
    sql = "UPDATE Account SET profilePicture = %s WHERE username = %s"
    vals = (profilePicture,username)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(localization):
    sql = "UPDATE Account SET localization = %s WHERE username = %s"
    vals = (localization,username)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(preferredLanguage):
    sql = "UPDATE Account SET preferredLanguage = %s WHERE username = %s"
    vals = (preferredLanguage,username)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(PIN):
    sql = "UPDATE Account SET PIN = %s WHERE username = %s"
    vals = (PIN,username)
    mycursor.execute(sql,vals)
    mydb.commit()
  
    
def selectAll():
  mycursor.execute("SELECT * FROM Account")

def select(username):
  sql = "SELECT * FROM Account WHERE username = '%s'" %(username)
  mycursor.execute(sql)

def delete(username):
  sql = "DELETE FROM Account WHERE username = '%s'" %(username)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM Account")
  mydb.commit()





