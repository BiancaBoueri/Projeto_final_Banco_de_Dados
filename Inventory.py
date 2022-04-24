from dbConnection import mydb, mycursor 

def insert(idInventory, mesos, nx):
  sql = "INSERT INTO Inventory VALUES (%s,%s,%s)"
  vals = (idInventory, mesos, nx)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idInventory, mesos, nx):
  if(mesos):
    sql = "UPDATE Inventory SET mesos = %s WHERE idInventory = %s"
    vals = (mesos,idInventory)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(nx):
    sql = "UPDATE Inventory SET nx = %s WHERE idInventory = %s"
    vals = (nx,idInventory)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM Inventory")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idInventory):
  sql = "SELECT * FROM Inventory WHERE idInventory = '%s'" %(idInventory)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idInventory):
  sql = "DELETE FROM Inventory WHERE idInventory = '%s'" %(idInventory)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM Inventory")
  mydb.commit()





