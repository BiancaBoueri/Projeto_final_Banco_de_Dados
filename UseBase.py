from dbConnection import mydb, mycursor 

def insert(idUse, useName, recoveredHP, recoveredMP, attributeBonus, value):
  sql = "INSERT INTO UseBase VALUES (%s,%s,%s,%s,%s,%s)"
  vals = (idUse, useName, recoveredHP, recoveredMP, attributeBonus, value)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idUse, useName, recoveredHP, recoveredMP, attributeBonus, value):
  if(useName):
    sql = "UPDATE UseBase SET useName = %s WHERE idUse = %s"
    vals = (useName,idUse)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(recoveredHP):
    sql = "UPDATE UseBase SET recoveredHP = %s WHERE idUse = %s"
    vals = (recoveredHP,idUse)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(recoveredMP):
    sql = "UPDATE UseBase SET recoveredMP = %s WHERE idUse = %s"
    vals = (recoveredMP,idUse)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(attributeBonus):
    sql = "UPDATE UseBase SET attributeBonus = %s WHERE idUse = %s"
    vals = (attributeBonus,idUse)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(value):
    sql = "UPDATE UseBase SET value = %s WHERE idUse = %s"
    vals = (value,idUse)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM UseBase")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idUse):
  sql = "SELECT * FROM UseBase WHERE idUse = '%s'" %(idUse)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idUse):
  sql = "DELETE FROM UseBase WHERE idUse = '%s'" %(idUse)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM UseBase")
  mydb.commit()





