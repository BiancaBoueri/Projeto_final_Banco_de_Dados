from dbConnection import mydb, mycursor 

def insert(idEquip, equipName, classCanUse, attackPower, magicPower, attribute, attributeBonus, value):
  sql = "INSERT INTO EquipBase VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
  vals = (idEquip, equipName, classCanUse, attackPower, magicPower, attribute, attributeBonus, value)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(idEquip, equipName, classCanUse, attackPower, magicPower, attribute, attributeBonus, value):
  if(equipName):
    sql = "UPDATE EquipBase SET equipName = %s WHERE idEquip = %s"
    vals = (equipName,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(classCanUse):
    sql = "UPDATE EquipBase SET classCanUse = %s WHERE idEquip = %s"
    vals = (classCanUse,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()
  
  if(attackPower):
    sql = "UPDATE EquipBase SET attackPower = %s WHERE idEquip = %s"
    vals = (attackPower,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(magicPower):
    sql = "UPDATE EquipBase SET magicPower = %s WHERE idEquip = %s"
    vals = (magicPower,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(attribute):
    sql = "UPDATE EquipBase SET attribute = %s WHERE idEquip = %s"
    vals = (attribute,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(attributeBonus):
    sql = "UPDATE EquipBase SET attributeBonus = %s WHERE idEquip = %s"
    vals = (attributeBonus,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()
  
  if(value):
    sql = "UPDATE EquipBase SET value = %s WHERE idEquip = %s"
    vals = (value,idEquip)
    mycursor.execute(sql,vals)
    mydb.commit()

def selectAll():
  mycursor.execute("SELECT * FROM EquipBase")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(idEquip):
  sql = "SELECT * FROM EquipBase WHERE idEquip = '%s'" %(idEquip)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(idEquip):
  sql = "DELETE FROM EquipBase WHERE idEquip = '%s'" %(idEquip)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM EquipBase")
  mydb.commit()





