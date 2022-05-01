from dbConnection import mydb, mycursor 

def callUseStoreSituationView():
  mycursor.execute("SELECT * FROM useStoreSituation")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def callEtcStoreSituationView():
  mycursor.execute("SELECT * FROM etcStoreSituation")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def callEquipStoreSituationView():
  mycursor.execute("SELECT * FROM equipStoreSituation")
  resultList = []
  for i in mycursor:
    resultList.append(i)
  return resultList

def callBuyUseItemProcedure(list):

  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]

  vals = (characterName, itemID, quantity)
  sql = """CALL buyUseItem(%s,%s,%s,@buyReturn);
  SELECT @buyReturn;"""
  mycursor.execute(sql,vals)
  for i in mycursor:
    return i

def callBuyEtcItemProcedure(list):
  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]

  vals = (characterName, itemID, quantity)
  sql = """CALL buyEtcItem(%s,%s,%s,@buyReturn);
  SELECT @buyReturn;"""
  mycursor.execute(sql,vals)
  print(mycursor)
  for i in mycursor:
    print(i)
    return i

def callBuyEquipItemProcedure(list):
  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]

  vals = (characterName, itemID, quantity)
  sql = """CALL buyEquipItem(%s,%s,%s,@buyReturn);
  SELECT @buyReturn;"""
  mycursor.execute(sql,vals)
  for i in mycursor:
    return i

def callSellUseItemProcedure(list):
  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]

  vals = (characterName, itemID, quantity)
  sql = """CALL sellUseItem(%s,%s,%s,@sellReturn);
  SELECT @sellReturn;"""
  mycursor.execute(sql,vals)
  mydb.commit()
  for i in mycursor:
    return i

def callSellEtcItemProcedure(list):
  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]

  vals = (characterName, itemID, quantity)
  sql = """CALL sellEtcItem(%s,%s,%s,@sellReturn);
  SELECT @sellReturn;"""
  mycursor.execute(sql,vals)
  mydb.commit()
  for i in mycursor:
    return i

def callSellEquipItemProcedure(list):
  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]
  rarity = list[4]

  vals = (characterName, itemID, quantity, rarity)
  sql = """CALL sellEquipItem(%s,%s,%s,%s,@sellReturn);
  SELECT @sellReturn;"""
  mycursor.execute(sql,vals)
  mydb.commit()
  for i in mycursor:
    return i


    

















