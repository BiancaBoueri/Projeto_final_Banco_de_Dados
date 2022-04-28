from dbConnection import mydb, mycursor 

def insert(idEtcSubInventory, Inventory_idInventory, EtcBase_idEtc, etcQuantity):
  sql = "INSERT INTO EtcSubInventory VALUES (%s,%s,%s,%s)"
  vals = (idEtcSubInventory, Inventory_idInventory, EtcBase_idEtc, etcQuantity)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idEtcSubInventory, etcQuantity):
  if(etcQuantity):
    sql = "UPDATE EtcSubInventory SET etcQuantity = %s WHERE idEtcSubInventory = %s"
    vals = (etcQuantity,idEtcSubInventory)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM EtcSubInventory")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idEtcSubInventory):
  sql = "SELECT * FROM EtcSubInventory WHERE idEtcSubInventory = '%s'" %(idEtcSubInventory)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idEtcSubInventory):
  sql = "DELETE FROM EtcSubInventory WHERE idEtcSubInventory = '%s'" %(idEtcSubInventory)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM EtcSubInventory")
  mydb.commit()





