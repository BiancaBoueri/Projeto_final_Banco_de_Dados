from dbConnection import mydb, mycursor 

def insert(idUseSubInventory, Inventory_idInventory, UseBase_idUse, useQuantity):
  sql = "INSERT INTO UseSubInventory VALUES (%s,%s,%s,%s)"
  vals = (idUseSubInventory, Inventory_idInventory, UseBase_idUse, useQuantity)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idUseSubInventory, useQuantity):
  if(useQuantity):
    sql = "UPDATE UseSubInventory SET useQuantity = %s WHERE idUseSubInventory = %s"
    vals = (useQuantity,idUseSubInventory)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM UseSubInventory")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idUseSubInventory):
  sql = "SELECT * FROM UseSubInventory WHERE idUseSubInventory = '%s'" %(idUseSubInventory)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idUseSubInventory):
  sql = "DELETE FROM UseSubInventory WHERE idUseSubInventory = '%s'" %(idUseSubInventory)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM UseSubInventory")
  mydb.commit()





