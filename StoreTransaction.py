from dbConnection import mydb, mycursor 

def createUseStoreSituationView():
  sql = "CREATE VIEW useStoreSituation AS SELECT name,idInventory,idUseSubInventory,mesos,stock,ub.value,idUse,useQuantity FROM maplestory.Character AS ch JOIN Inventory AS i JOIN UseSubInventory AS u JOIN Store AS s JOIN UseBase AS ub ON i.idInventory=ch.Inventory_idInventory AND i.idInventory=u.Inventory_idInventory AND ub.idUse = u.UseBase_idUse AND s.idItem = ub.idUse"
  mycursor.execute(sql)
  mydb.commit()

def createEtcStoreSituationView():
  sql = "CREATE VIEW etcStoreSituation AS SELECT name,idInventory,idEtcSubInventory,mesos,stock,ub.value,idEtc,etcQuantity FROM maplestory.Character AS ch JOIN Inventory AS i JOIN EtcSubInventory AS u JOIN Store AS s JOIN EtcBase AS ub ON i.idInventory=ch.Inventory_idInventory AND i.idInventory=u.Inventory_idInventory AND ub.idEtc = u.EtcBase_idEtc AND s.idItem = ub.idEtc"  
  mycursor.execute(sql)
  mydb.commit()

def createEquipStoreSituationView():
  sql = "CREATE VIEW equipStoreSituation AS SELECT name,idInventory,idEquipSubInventory,mesos,stock,ub.value,idEquip,equipQuantity,equipRarity FROM maplestory.Character AS ch JOIN Inventory AS i JOIN EquipSubInventory AS u JOIN Store AS s JOIN EquipBase AS ub ON i.idInventory=ch.Inventory_idInventory AND i.idInventory=u.Inventory_idInventory AND ub.idEquip = u.EquipBase_idEquip AND s.idItem = ub.idEquip"
  mycursor.execute(sql)
  mydb.commit()


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
  
def createSellProcedure(list): 
  characterName = list[0]
  itemType = list[1] 
  itemID = list[2]
  quantity = list[3]
  rarity = list[4]

  if(itemType == "Use"):

    vals = (characterName, itemID, quantity)

    sql = """DELIMITER $$
    CREATE PROCEDURE sellUseItem(
    IN %s VARCHAR(20),
    IN %s CHAR(8),
    IN %s TINYINT,
    OUT sellReturn VARCHAR(50)
    )
    BEGIN
      SET @useSubInventoryID = (SELECT idUseSubInventory FROM maplestory.Character AS ch JOIN UseSubInventory AS u ON ch.Inventory_idInventory=u.Inventory_idInventory WHERE name = characterName);
      SET @itemQuantity = (SELECT useQuantity FROM UseSubInventory WHERE UseBase_idUse = itemID AND idUseSubInventory = @useSubInventoryID); 
        IF @itemQuantity < quantity THEN
        SET sellreturn = "Character doesn't have enough itens";
      ELSE 
            SET @inventory = (SELECT Inventory_idInventory FROM maplestory.Character WHERE name = characterName);
            SET @value = (SELECT value FROM UseBase WHERE idUse = itemID);
            UPDATE Inventory SET mesos = mesos + (@value * quantity) WHERE idInventory = @inventory;
        UPDATE UseSubInventory SET useQuantity = useQuantity - quantity WHERE UseBase_idUse = itemID AND idUseSubInventory = @useSubInventoryID;
        INSERT INTO Store VALUES (itemID,@value,quantity) ON DUPLICATE KEY UPDATE stock=stock + quantity;        
        SET sellReturn = "Success";
      END IF;
    END $$ 
    DELIMITER ;"""

  elif(itemType == "Etc"):
    
    vals = (characterName, itemID, quantity)

    sql = """DELIMITER $$
    CREATE PROCEDURE sellEtcItem(
    IN %s VARCHAR(20),
    IN %s CHAR(8),
    IN %s TINYINT,
    OUT sellReturn VARCHAR(50)
    )
    BEGIN
      SET @etcSubInventoryID = (SELECT idEtcSubInventory FROM maplestory.Character AS ch JOIN EtcSubInventory AS u ON ch.Inventory_idInventory=u.Inventory_idInventory WHERE name = characterName);
      SET @itemQuantity = (SELECT etcQuantity FROM EtcSubInventory WHERE EtcBase_idEtc = itemID AND idEtcSubInventory = @etcSubInventoryID); 
        IF @itemQuantity < quantity THEN
        SET sellreturn = "Character doesn't have enough itens";
      ELSE 
            SET @inventory = (SELECT Inventory_idInventory FROM maplestory.Character WHERE name = characterName);
            SET @value = (SELECT value FROM EtcBase WHERE idEtc = itemID);
            UPDATE Inventory SET mesos = mesos + (@value * quantity) WHERE idInventory = @inventory;
        UPDATE EtcSubInventory SET etcQuantity = etcQuantity - quantity WHERE EtcBase_idEtc = itemID AND idEtcSubInventory = @etcSubInventoryID;
        INSERT INTO Store VALUES (itemID,@value,quantity) ON DUPLICATE KEY UPDATE stock=stock + quantity;        
        SET sellReturn = "Success";
      END IF;
    END $$ 
    DELIMITER ;"""
  
  else:

    vals = (characterName, itemID, quantity, rarity)

    sql = """DELIMITER $$
    CREATE PROCEDURE sellEquipItem(
    IN %s VARCHAR(20),
    IN %s CHAR(8),
    IN %s TINYINT,
    IN %s VARCHAR(9),
    OUT sellReturn VARCHAR(50)
    )
    BEGIN 
      SET @equipSubInventoryID = (SELECT idEquipSubInventory FROM maplestory.Character AS ch JOIN EquipSubInventory AS u ON ch.Inventory_idInventory=u.Inventory_idInventory WHERE name = characterName);
        SET @itemQuantity = (SELECT equipQuantity FROM EquipSubInventory WHERE EquipBase_idEquip = itemID AND idEquipSubInventory = @equipSubInventoryID AND equipRarity = rarity);
        IF @itemQuantity < quantity THEN
        SET sellreturn = "Character doesn't have enough itens";
      ELSE 
            SET @inventory = (SELECT Inventory_idInventory FROM maplestory.Character WHERE name = characterName);
            SET @value = (SELECT value FROM EquipBase WHERE idEquip = itemID);
            UPDATE Inventory SET mesos = mesos + (@value * quantity) WHERE idInventory = @inventory;
        UPDATE EquipSubInventory SET equipQuantity = equipQuantity - quantity WHERE EquipBase_idEquip = itemID AND idEquipSubInventory = @equipSubInventoryID AND equipRarity = rarity;
        INSERT INTO Store VALUES (itemID,@value,quantity) ON DUPLICATE KEY UPDATE stock=stock + quantity;        
        SET sellReturn = "Success";
      END IF;
    END $$ 
    DELIMITER ;"""

  
  mycursor.execute(sql,vals)
  mydb.commit()

def createBuyProcedure(list):

  characterName = list[0] 
  itemType = list[1] 
  itemID = list[2] 
  quantity = list[3] 

  vals = (characterName, itemID, quantity)

  if(itemType == "Use"):

    sql = """DELIMITER $$
    CREATE PROCEDURE buyUseItem( 
    IN %s VARCHAR(20),
    IN %s CHAR(8),
    IN %s TINYINT,
    OUT buyReturn VARCHAR(50)
    )
    BEGIN
      SET @useSubInventoryID = (SELECT idUseSubInventory FROM maplestory.Character AS ch JOIN UseSubInventory AS u ON ch.Inventory_idInventory=u.Inventory_idInventory WHERE name = characterName);
        SET @inventory = (SELECT Inventory_idInventory FROM maplestory.Character WHERE name = characterName);
        SET @characterMesos = (SELECT mesos from Inventory where idInventory = @inventory);    
        SET @storeStock = (SELECT stock FROM Store WHERE idItem = itemID);
        SET @itemExists = (SELECT EXISTS(SELECT idItem FROM Store WHERE idItem = itemID));
        IF @itemExists = 0 THEN
        SET buyReturn = "Store doesn't have this item in stock";
        ELSEIF quantity > @storeStock THEN
        SET buyReturn = "Store doesn't have enough items in stock";
        ELSE 
        SET @value = (SELECT value FROM Store WHERE idItem = itemID);        
        IF @value > @characterMesos THEN
          SET buyReturn = "Character doesn't have enough money";
        ELSE 
          UPDATE Inventory SET mesos = mesos - (@value * quantity) WHERE idInventory = @inventory;
          INSERT INTO UseSubInventory VALUES (@useSubInventoryID,@inventory,itemID,quantity) ON DUPLICATE KEY UPDATE useQuantity=useQuantity + quantity;
          INSERT INTO Store VALUES (itemID,@value,"1") ON DUPLICATE KEY UPDATE stock=stock - quantity;
          SET buyReturn = "Success";
        END IF;
      END IF;
    END $$ 
    DELIMITER ;"""

  
  elif(itemType == "Etc"):

    sql = """DELIMITER $$
    CREATE PROCEDURE buyEtcItem( 
    IN %s VARCHAR(20),
    IN %s CHAR(8),
    IN %s TINYINT,
    OUT buyReturn VARCHAR(50)
    )
    BEGIN
      SET @etcSubInventoryID = (SELECT idEtcSubInventory FROM maplestory.Character AS ch JOIN EtcSubInventory AS u ON ch.Inventory_idInventory=u.Inventory_idInventory WHERE name = characterName);
        SET @inventory = (SELECT Inventory_idInventory FROM maplestory.Character WHERE name = characterName);
        SET @characterMesos = (SELECT mesos from Inventory where idInventory = @inventory);    
        SET @storeStock = (SELECT stock FROM Store WHERE idItem = itemID);
        SET @itemExists = (SELECT EXISTS(SELECT idItem FROM Store WHERE idItem = itemID));
        IF @itemExists = 0 THEN
        SET buyReturn = "Store doesn't have this item in stock";
        ELSEIF quantity > @storeStock THEN
        SET buyReturn = "Store doesn't have enough items in stock";
        ELSE 
        SET @value = (SELECT value FROM Store WHERE idItem = itemID);        
        IF @value > @characterMesos THEN
          SET buyReturn = "Character doesn't have enough money";
        ELSE 
          UPDATE Inventory SET mesos = mesos - (@value * quantity) WHERE idInventory = @inventory;
          INSERT INTO EtcSubInventory VALUES (@etcSubInventoryID,@inventory,itemID,quantity) ON DUPLICATE KEY UPDATE etcQuantity=etcQuantity + quantity;
          INSERT INTO Store VALUES (itemID,@value,"1") ON DUPLICATE KEY UPDATE stock=stock - quantity;
          SET buyReturn = "Success";
        END IF;
      END IF;
    END $$ 
    DELIMITER ;"""

  else:
  
    sql = """
    DELIMITER $$
    CREATE PROCEDURE buyEquipItem( 
    IN %s VARCHAR(20),
    IN %s CHAR(8),
    IN %s TINYINT,
    OUT buyReturn VARCHAR(50)
    )
    BEGIN
      SET @equipSubInventoryID = (SELECT idEquipSubInventory FROM maplestory.Character AS ch JOIN EquipSubInventory AS u ON ch.Inventory_idInventory=u.Inventory_idInventory WHERE name = characterName);
        SET @inventory = (SELECT Inventory_idInventory FROM maplestory.Character WHERE name = characterName);
        SET @characterMesos = (SELECT mesos from Inventory where idInventory = @inventory);    
        SET @storeStock = (SELECT stock FROM Store WHERE idItem = itemID);
        SET @itemExists = (SELECT EXISTS(SELECT idItem FROM Store WHERE idItem = itemID));
        IF @itemExists = 0 THEN
        SET buyReturn = "Store doesn't have this item in stock";
        ELSEIF quantity > @storeStock THEN
        SET buyReturn = "Store doesn't have enough items in stock";
        ELSE 
        SET @value = (SELECT value FROM Store WHERE idItem = itemID);        
        IF @value > @characterMesos THEN
          SET buyReturn = "Character doesn't have enough money";
        ELSE 
          UPDATE Inventory SET mesos = mesos - (@value * quantity) WHERE idInventory = @inventory;
                INSERT INTO EquipSubInventory VALUES (@equipSubInventoryID,@inventory,itemID,quantity,"Rare") ON DUPLICATE KEY UPDATE equipQuantity=equipQuantity + quantity;
          INSERT INTO Store VALUES (itemID,@value,"1") ON DUPLICATE KEY UPDATE stock=stock - quantity;
          SET buyReturn = "Success";
        END IF;
      END IF;
    END $$ 
    DELIMITER ;"""

    
  mycursor.execute(sql,vals)
  mydb.commit()


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
  for i in mycursor:
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
  for i in mycursor:
    return i


    

















