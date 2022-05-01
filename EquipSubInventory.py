from dbConnection import mydb, mycursor 

def insert(idEquipSubInventory, Inventory_idInventory, EquipBase_idEquip, equipQuantity, equipRarity):
  sql = "INSERT INTO EquipSubInventory VALUES (%s,%s,%s,%s,%s)"
  vals = (idEquipSubInventory, Inventory_idInventory, EquipBase_idEquip, equipQuantity, equipRarity)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idEquipSubInventory, equipID, equipQuantity, equipRarity):
  if(equipQuantity):
    sql = "UPDATE EquipSubInventory SET equipQuantity = %s WHERE idEquipSubInventory = %s AND EquipBase_idEquip = %s AND equipRarity = %s"
    vals = (equipQuantity,idEquipSubInventory,equipID,equipRarity)
    mycursor.execute(sql,vals)
    mydb.commit()
    
def selectAll():
  mycursor.execute("SELECT * FROM EquipSubInventory")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idEquipSubInventory):
  sql = "SELECT * FROM EquipSubInventory WHERE idEquipSubInventory = '%s'" %(idEquipSubInventory)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idEquipSubInventory):
  sql = "DELETE FROM EquipSubInventory WHERE idEquipSubInventory = '%s'" %(idEquipSubInventory)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM EquipSubInventory")
  mydb.commit()





