from dbConnection import mydb, mycursor
from datetime import date

def insert(Account_username, name, Class, mainAttribute, level, HP, MP, EXP, server, Map_idMap, Inventory_idInventory):
  sql = "INSERT INTO maplestory.Character VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
  vals = (name, Class, mainAttribute, level, HP, MP, EXP, server, Map_idMap, Inventory_idInventory)
  mycursor.execute(sql,vals)
  mydb.commit()

  creationDate = date.today()
  Character_name = name
  sql = "INSERT INTO AccountToCharacter VALUES (%s,%s,%s)"
  vals = (Account_username, Character_name, creationDate)
  mycursor.execute(sql,vals)
  mydb.commit()

def update(name, Class, mainAttribute, level, HP, MP, EXP, server):
  if(Class):
    sql = "UPDATE maplestory.Character SET class = %s WHERE name = %s"
    vals = (Class,name)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(mainAttribute):
    sql = "UPDATE maplestory.Character SET mainAttribute = %s WHERE name = %s"
    vals = (mainAttribute,name)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(level):
    sql = "UPDATE maplestory.Character SET level = %s WHERE name = %s"
    vals = (level,name)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(HP):
    sql = "UPDATE maplestory.Character SET HP = %s WHERE name = %s"
    vals = (HP,name)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(MP):
    sql = "UPDATE maplestory.Character SET MP = %s WHERE name = %s"
    vals = (MP,name)
    mycursor.execute(sql,vals)
    mydb.commit()
    
  if(EXP):
    sql = "UPDATE maplestory.Character SET EXP = %s WHERE name = %s"
    vals = (EXP,name)
    mycursor.execute(sql,vals)
    mydb.commit()

  if(server):
    sql = "UPDATE maplestory.Character SET server = %s WHERE name = %s"
    vals = (server,name)
    mycursor.execute(sql,vals)
    mydb.commit()

def selectAll():
  sql = "SELECT Account_username, Character_name, creationDate, class, mainAttribute, level, HP, MP, EXP, server, Map_idMap, Inventory_idInventory FROM AccountToCharacter as atc JOIN maplestory.Character as ch ON ch.name = atc.Character_name"
  mycursor.execute(sql)
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def select(name):
  sql = "SELECT Account_username, Character_name, creationDate, class, mainAttribute, level, HP, MP, EXP, server, Map_idMap, Inventory_idInventory FROM AccountToCharacter as atc JOIN maplestory.Character as ch ON ch.name = atc.Character_name WHERE name = '%s'" %(name)
  mycursor.execute(sql)
  for i in mycursor:
    return i

def delete(name):
  sql = "DELETE FROM AccountToCharacter WHERE Character_name = '%s'" %(name)
  mycursor.execute(sql)
  mydb.commit()
  sql = "DELETE FROM maplestory.Character WHERE name = '%s'" %(name)
  mycursor.execute(sql)
  mydb.commit()

def deleteAll():
  mycursor.execute("DELETE FROM AccountToCharacter")
  mydb.commit()
  mycursor.execute("DELETE FROM maplestory.Character")
  mydb.commit()





