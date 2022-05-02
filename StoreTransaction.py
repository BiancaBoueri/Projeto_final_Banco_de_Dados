import mysql.connector
from dbConnection import mydb, mycursor

def callLastTransactionEquipView(charName,idItem,itemRarity):
  mycursor.execute("SELECT * FROM lasttransactionresultequip WHERE name = '%s' AND idItem = '%s' AND equipRarity = '%s'" %(charName,idItem,itemRarity))
  for i in mycursor:
    return i

def callLastTransactionUseView(charName,idItem):
  mycursor.execute("SELECT * FROM lasttransactionresultuse WHERE name = '%s' AND idItem = '%s'" %(charName,idItem))
  for i in mycursor:
    return i

def callLastTransactionEtcView(charName,idItem):
  mycursor.execute("SELECT * FROM lasttransactionresultetc WHERE name = '%s' AND idItem = '%s'" %(charName,idItem))
  for i in mycursor:
    return i

def callBuyProcedure(charName,typeOfItem,idItem,itemQuantity,itemRarity):
  if (typeOfItem == "Equip"):
    mycursor.execute("CALL buyFromStore('%s','Equip','%s',%s,@output);" %(charName,idItem,itemQuantity))
    mycursor.execute("SELECT @output")
    mydb.commit()

    tempList = []
    for i in mycursor:
      tempList.append(i[0])

    if (tempList[0] is not None):
      return tempList[0]

    return callLastTransactionEquipView(charName,idItem,itemRarity)

  elif (typeOfItem == "Use"):
    mycursor.execute("CALL buyFromStore('%s','Use','%s',%s,@output);" %(charName,idItem,itemQuantity))
    mycursor.execute("SELECT @output")
    mydb.commit()

    tempList = []
    for i in mycursor:
      tempList.append(i[0])

    if (tempList[0] is not None):
      return tempList[0]

    return callLastTransactionUseView(charName,idItem)

  elif (typeOfItem == "Etc"):
    mycursor.execute("CALL buyFromStore('%s','Etc','%s',%s,@output);" %(charName,idItem,itemQuantity))
    mycursor.execute("SELECT @output")
    mydb.commit()

    tempList = []
    for i in mycursor:
      tempList.append(i[0])

    if (tempList[0] is not None):
      return tempList[0]

    return callLastTransactionEtcView(charName,idItem)

def callSellProcedure(charName,typeOfItem,idItem,itemQuantity,itemRarity):
  if (typeOfItem == "Equip"):
    mycursor.execute("CALL sellOnStore('%s','Equip','%s',%s,'Rare',@output);" %(charName,idItem,itemQuantity))
    mycursor.execute("SELECT @output")
    mydb.commit()

    tempList = []
    for i in mycursor:
      tempList.append(i[0])

    if (tempList[0] is not None):
      return tempList[0]

    return callLastTransactionEquipView(charName,idItem,itemRarity)

  elif (typeOfItem == "Use"):
    mycursor.execute("CALL sellOnStore('%s','Use','%s',%s,'Rare',@output);" %(charName,idItem,itemQuantity))
    mycursor.execute("SELECT @output")
    mydb.commit()

    tempList = []
    for i in mycursor:
      tempList.append(i[0])

    if (tempList[0] is not None):
      return tempList[0]

    return callLastTransactionUseView(charName,idItem)

  elif (typeOfItem == "Etc"):
    mycursor.execute("CALL sellOnStore('%s','Etc','%s',%s,'Rare',@output);" %(charName,idItem,itemQuantity))
    mycursor.execute("SELECT @output")
    mydb.commit()

    tempList = []
    for i in mycursor:
      tempList.append(i[0])

    if (tempList[0] is not None):
      return tempList[0]

    return callLastTransactionEtcView(charName,idItem)


    

















