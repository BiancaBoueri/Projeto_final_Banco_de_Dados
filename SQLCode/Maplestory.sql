-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
SET @@global.sql_mode= '';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS maplestory DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema detran_database
-- -----------------------------------------------------
USE maplestory ;

-- -----------------------------------------------------
-- Table maplestory.`Account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`Account` (
  `username` VARCHAR(40) NOT NULL,
  `password` VARCHAR(30) NOT NULL,
  `profilePicture` BLOB NULL,
  `creationDate` DATE NOT NULL,
  `localization` CHAR(2) NOT NULL,
  `preferredLanguage` VARCHAR(25) NOT NULL,
  `PIN` DECIMAL(4,0) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`Map`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`Map` (
  `idMap` DECIMAL(6,0) UNSIGNED NOT NULL,
  `mapName` VARCHAR(45) NOT NULL,
  `spawnPosition` DECIMAL(1,0) NOT NULL,
  PRIMARY KEY (`idMap`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`Inventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`Inventory` (
  `idInventory` CHAR(8) NOT NULL,
  `mesos` DECIMAL(11,0) UNSIGNED ZEROFILL,
  `nx` DECIMAL(9,0) UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`idInventory`),
  UNIQUE INDEX `idInventory_UNIQUE` (`idInventory` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`Character`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`Character` (
  `name` VARCHAR(20) NOT NULL,
  `class` VARCHAR(7) NOT NULL,
  `mainAttribute` CHAR(3) NOT NULL,
  `level` TINYINT UNSIGNED NOT NULL,
  `HP` INT UNSIGNED NOT NULL,
  `MP` INT UNSIGNED NOT NULL,
  `EXP` DOUBLE UNSIGNED NOT NULL,
  `server` VARCHAR(8) NOT NULL,
  `Map_idMap` DECIMAL(6,0) UNSIGNED,
  `Inventory_idInventory` CHAR(8),
  PRIMARY KEY (`name`),
  UNIQUE INDEX `characterName_UNIQUE` (`name` ASC) VISIBLE,
  INDEX `fk_Character_Map1_idx` (`Map_idMap` ASC) VISIBLE,
  INDEX `fk_Character_Inventory1_idx` (`Inventory_idInventory` ASC) VISIBLE,
  CONSTRAINT `fk_Character_Map1`
    FOREIGN KEY (`Map_idMap`)
    REFERENCES maplestory.`Map` (`idMap`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Character_Inventory1`
    FOREIGN KEY (`Inventory_idInventory`)
    REFERENCES maplestory.`Inventory` (`idInventory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`EquipBase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`EquipBase` (
  `idEquip` CHAR(8) NOT NULL,
  `equipName` VARCHAR(60) NOT NULL,
  `classCanUse` VARCHAR(7) NOT NULL,
  `attackPower` TINYINT UNSIGNED NOT NULL,
  `magicPower` TINYINT UNSIGNED NOT NULL,
  `attribute` CHAR(3) NOT NULL,
  `attributeBonus` TINYINT UNSIGNED NOT NULL,
  `value` DECIMAL(11,0) ZEROFILL UNSIGNED NOT NULL,
  PRIMARY KEY (`idEquip`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`EquipSubInventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`EquipSubInventory` (
  `idEquipSubInventory` INT UNSIGNED NOT NULL,
  `Inventory_idInventory` CHAR(8) NOT NULL,
  `EquipBase_idEquip` CHAR(8) NOT NULL,
  `equipQuantity` TINYINT UNSIGNED NOT NULL,
  `equipRarity` VARCHAR(9) NOT NULL,
  PRIMARY KEY (`idEquipSubInventory`,`EquipBase_idEquip`,`equipRarity`),
  INDEX `fk_EquipSubInventory_EquipBase1_idx` (`EquipBase_idEquip` ASC) VISIBLE,
  INDEX `fk_EquipSubInventory_Inventory1_idx` (`Inventory_idInventory` ASC) VISIBLE,
  CONSTRAINT `fk_EquipSubInventory_EquipBase1`
    FOREIGN KEY (`EquipBase_idEquip`)
    REFERENCES maplestory.`EquipBase` (`idEquip`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_EquipSubInventory_Inventory1`
    FOREIGN KEY (`Inventory_idInventory`)
    REFERENCES maplestory.`Inventory` (`idInventory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`UseBase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`UseBase` (
  `idUse` CHAR(8) NOT NULL,
  `useName` VARCHAR(60) NOT NULL,
  `recoveredHP` INT NOT NULL,
  `recoveredMP` INT NOT NULL,
  `attributeBonus` TINYINT NOT NULL,
  `value` DECIMAL(11,0) UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`idUse`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`UseSubInventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`UseSubInventory` (
  `idUseSubInventory` INT NOT NULL,
  `Inventory_idInventory` CHAR(8) NOT NULL,
  `UseBase_idUse` CHAR(8) NOT NULL,
  `useQuantity` TINYINT UNSIGNED NOT NULL,
  INDEX `fk_UseSubInventory_UseBase1_idx` (`UseBase_idUse` ASC) VISIBLE,
  PRIMARY KEY (`idUseSubInventory`,`UseBase_idUse`),
  INDEX `fk_UseSubInventory_Inventory1_idx` (`Inventory_idInventory` ASC) VISIBLE,
  CONSTRAINT `fk_UseSubInventory_UseBase1`
    FOREIGN KEY (`UseBase_idUse`)
    REFERENCES maplestory.`UseBase` (`idUse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UseSubInventory_Inventory1`
    FOREIGN KEY (`Inventory_idInventory`)
    REFERENCES maplestory.`Inventory` (`idInventory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`EtcBase`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`EtcBase` (
  `idEtc` CHAR(8) NOT NULL,
  `etcName` VARCHAR(60) NOT NULL,
  `value` DECIMAL(11,0) UNSIGNED ZEROFILL NOT NULL,
  PRIMARY KEY (`idEtc`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`EtcSubInventory`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`EtcSubInventory` (
  `idEtcSubInventory` INT NOT NULL,
  `Inventory_idInventory` CHAR(8) NOT NULL,
  `EtcBase_idEtc` CHAR(8) NOT NULL,
  `etcQuantity` TINYINT UNSIGNED NOT NULL,
  PRIMARY KEY (`idEtcSubInventory`,`EtcBase_idEtc`),
  INDEX `fk_EtcSubInventory_EtcBase1_idx` (`EtcBase_idEtc` ASC) VISIBLE,
  INDEX `fk_EtcSubInventory_Inventory1_idx` (`Inventory_idInventory` ASC) VISIBLE,
  CONSTRAINT `fk_EtcSubInventory_EtcBase1`
    FOREIGN KEY (`EtcBase_idEtc`)
    REFERENCES maplestory.`EtcBase` (`idEtc`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_EtcSubInventory_Inventory1`
    FOREIGN KEY (`Inventory_idInventory`)
    REFERENCES maplestory.`Inventory` (`idInventory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`Store`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`Store` (
  `idItem` CHAR(8) NOT NULL,
  `value` DECIMAL(11,0) ZEROFILL UNSIGNED NOT NULL,
  `stock` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`idItem`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table maplestory.`AccountToCharacter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS maplestory.`AccountToCharacter` (
  `Account_username` VARCHAR(40) NOT NULL,
  `Character_name` VARCHAR(20) NOT NULL,
  `creationDate` DATE NOT NULL,
  PRIMARY KEY (`Account_username`, `Character_name`),
  INDEX `fk_AccountToCharacter_Account_idx` (`Account_username` ASC) VISIBLE,
  INDEX `fk_AccountToCharacter_Character1_idx` (`Character_name` ASC) VISIBLE,
  CONSTRAINT `fk_AccountToCharacter_Account`
    FOREIGN KEY (`Account_username`)
    REFERENCES maplestory.`Account` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AccountToCharacter_Character1`
    FOREIGN KEY (`Character_name`)
    REFERENCES maplestory.`Character` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

CREATE VIEW lastTransactionResultEquip AS
	SELECT name,idInventory,mesos,idEquipSubInventory,idItem,equipName,equipQuantity,stock,equipRarity
    FROM maplestory.Character AS ch JOIN Inventory AS inv JOIN EquipSubInventory as subInv JOIN EquipBase as base JOIN Store as store
    ON ch.Inventory_idInventory = inv.idInventory AND subInv.Inventory_idInventory = inv.idInventory AND base.idEquip = store.idItem AND store.idItem = subInv.EquipBase_idEquip;
    
CREATE VIEW lastTransactionResultUse AS
	SELECT name,idInventory,mesos,idUseSubInventory,idItem,useName,useQuantity,stock
    FROM maplestory.Character AS ch JOIN Inventory AS inv JOIN UseSubInventory as subInv JOIN UseBase as base JOIN Store as store
    ON ch.Inventory_idInventory = inv.idInventory AND subInv.Inventory_idInventory = inv.idInventory AND base.idUse = store.idItem AND store.idItem = subInv.UseBase_idUse;

CREATE VIEW lastTransactionResultEtc AS
	SELECT name,idInventory,mesos,idEtcSubInventory,idItem,etcName,etcQuantity,stock
    FROM maplestory.Character AS ch JOIN Inventory AS inv JOIN EtcSubInventory as subInv JOIN EtcBase as base JOIN Store as store
    ON ch.Inventory_idInventory = inv.idInventory AND subInv.Inventory_idInventory = inv.idInventory AND base.idEtc = store.idItem AND store.idItem = subInv.EtcBase_idEtc;

DELIMITER $$
    CREATE PROCEDURE findMapWhereCharactersAre( 
    IN username VARCHAR(40),
    IN compareFlag TINYINT,
    IN compareCondition TINYINT
    )
    BEGIN
		IF compareFlag > compareCondition THEN
			SELECT username, name, acctochar.creationDate, idMap, mapName
			FROM maplestory.account AS acc JOIN maplestory.accounttocharacter AS acctochar JOIN maplestory.character AS ch JOIN maplestory.map AS map
			ON acc.username = acctochar.Account_username AND acctochar.Character_name = ch.name AND ch.Map_idMap = map.idMap
			WHERE acc.username = username;
		ELSE
			SELECT idMap, mapName
			FROM maplestory.account AS acc JOIN maplestory.accounttocharacter AS acctochar JOIN maplestory.character AS ch JOIN maplestory.map AS map
			ON acc.username = acctochar.Account_username AND acctochar.Character_name = ch.name AND ch.Map_idMap = map.idMap
			WHERE acc.username = username;
		END IF;
    END $$ 
DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE buyFromStore( 
    IN charName VARCHAR(20),
    IN typeOfItem VARCHAR(5),
    IN boughtItemID CHAR(8),
    IN boughtItemQuantity TINYINT UNSIGNED,
    OUT errorMessage VARCHAR(100)
    )
    BEGIN
		IF typeOfItem = 'Equip' THEN
			SET @stockInStore = (SELECT stock FROM maplestory.store WHERE idItem = boughtItemID);
            SET @charMoney = (SELECT mesos FROM maplestory.character AS ch JOIN maplestory.inventory AS inv WHERE ch.name = charName AND ch.Inventory_idInventory = inv.idInventory);
            SET @charInventory = (SELECT Inventory_idInventory FROM maplestory.character WHERE name = charName);
            SET @charSubinventory = (SELECT idEquipSubInventory FROM maplestory.equipsubinventory WHERE Inventory_idInventory = @charInventory LIMIT 1);
            SET @itemPrice = (SELECT value FROM maplestory.store WHERE idItem = boughtItemID);
            SET @itemQuantityOwned = (SELECT equipQuantity FROM maplestory.equipsubinventory WHERE EquipBase_idEquip = boughtItemID AND idEquipSubInventory = @charSubinventory AND equipRarity = "Rare");
            IF @stockInStore < boughtItemQuantity THEN
				SET errorMessage = "Store does not have enough in stock";
			ELSEIF @charMoney < (@itemPrice*boughtItemQuantity) THEN
				SET errorMessage = "Character does not have enough mesos";
			ELSEIF (@itemQuantityOwned IS NOT NULL) and (@itemQuantityOwned + boughtItemQuantity > 255) THEN
				SET errorMessage = "Character does not have enough space in the subinventory";
			ELSEIF (@itemQuantityOwned IS NOT NULL) THEN
				UPDATE store SET stock = stock - boughtItemQuantity WHERE idItem = boughtItemID;
                UPDATE inventory SET mesos = mesos - (@itemPrice * boughtItemQuantity) WHERE idInventory = @charInventory;
                UPDATE equipsubinventory SET equipQuantity = equipQuantity + boughtItemQuantity WHERE idEquipSubInventory = @charSubinventory AND EquipBase_idEquip = boughtItemID;
			ELSEIF (@itemQuantityOwned IS NULL) THEN
				UPDATE store SET stock = stock - boughtItemQuantity WHERE idItem = boughtItemID;
                UPDATE inventory SET mesos = mesos - (@itemPrice * boughtItemQuantity) WHERE idInventory = @charInventory;
				INSERT INTO equipsubinventory VALUES (@charSubinventory, @charInventory, boughtItemID, boughtItemQuantity, "Rare");
            ELSE
				SET errorMessage = "Check if all given information is correct and exists";
            END IF;
        
		ELSEIF typeOfItem = 'Use' THEN
			SET @stockInStore = (SELECT stock FROM maplestory.store WHERE idItem = boughtItemID);
            SET @charMoney = (SELECT mesos FROM maplestory.character AS ch JOIN maplestory.inventory AS inv WHERE ch.name = charName AND ch.Inventory_idInventory = inv.idInventory);
            SET @charInventory = (SELECT Inventory_idInventory FROM maplestory.character WHERE name = charName);
            SET @charSubinventory = (SELECT idUseSubInventory FROM maplestory.usesubinventory WHERE Inventory_idInventory = @charInventory LIMIT 1);
            SET @itemPrice = (SELECT value FROM maplestory.store WHERE idItem = boughtItemID);
            SET @itemQuantityOwned = (SELECT useQuantity FROM maplestory.usesubinventory WHERE UseBase_idUse = boughtItemID AND idUseSubInventory = @charSubinventory);

            IF @stockInStore < boughtItemQuantity THEN
				SET errorMessage = "Store does not have enough in stock";
			ELSEIF @charMoney < (@itemPrice*boughtItemQuantity) THEN
				SET errorMessage = "Character does not have enough mesos";
			ELSEIF (@itemQuantityOwned IS NOT NULL) and (@itemQuantityOwned + boughtItemQuantity > 255) THEN
				SET errorMessage = "Character does not have enough space in the subinventory";
			ELSEIF (@itemQuantityOwned IS NOT NULL) THEN
				UPDATE store SET stock = stock - boughtItemQuantity WHERE idItem = boughtItemID;
                UPDATE inventory SET mesos = mesos - (@itemPrice * boughtItemQuantity) WHERE idInventory = @charInventory;
                UPDATE usesubinventory SET useQuantity = (useQuantity + boughtItemQuantity) WHERE idUseSubInventory = @charSubinventory AND UseBase_idUse = boughtItemID;
			ELSEIF (@itemQuantityOwned IS NULL) THEN
				UPDATE store SET stock = stock - boughtItemQuantity WHERE idItem = boughtItemID;
                UPDATE inventory SET mesos = mesos - (@itemPrice * boughtItemQuantity) WHERE idInventory = @charInventory;
				INSERT INTO usesubinventory VALUES (@charSubinventory, @charInventory, boughtItemID, boughtItemQuantity);
            ELSE
				SET errorMessage = "Check if all given information is correct and exists";
            END IF;
            
		ELSE
			SET @stockInStore = (SELECT stock FROM maplestory.store WHERE idItem = boughtItemID);
            SET @charMoney = (SELECT mesos FROM maplestory.character AS ch JOIN maplestory.inventory AS inv WHERE ch.name = charName AND ch.Inventory_idInventory = inv.idInventory);
            SET @charInventory = (SELECT Inventory_idInventory FROM maplestory.character WHERE name = charName);
            SET @charSubinventory = (SELECT idEtcSubInventory FROM maplestory.etcsubinventory WHERE Inventory_idInventory = @charInventory LIMIT 1);
            SET @itemPrice = (SELECT value FROM maplestory.store WHERE idItem = boughtItemID);
            SET @itemQuantityOwned = (SELECT etcQuantity FROM maplestory.etcsubinventory WHERE EtcBase_idEtc = boughtItemID AND idEtcSubInventory = @charSubinventory);

            IF @stockInStore < boughtItemQuantity THEN
				SET errorMessage = "Store does not have enough in stock";
			ELSEIF @charMoney < (@itemPrice*boughtItemQuantity) THEN
				SET errorMessage = "Character does not have enough mesos";
			ELSEIF (@itemQuantityOwned IS NOT NULL) and (@itemQuantityOwned + boughtItemQuantity > 255) THEN
				SET errorMessage = "Character does not have enough space in the subinventory";
			ELSEIF (@itemQuantityOwned IS NOT NULL) THEN
				UPDATE store SET stock = stock - boughtItemQuantity WHERE idItem = boughtItemID;
                UPDATE inventory SET mesos = mesos - (@itemPrice * boughtItemQuantity) WHERE idInventory = @charInventory;
                UPDATE etcsubinventory SET etcQuantity = etcQuantity + boughtItemQuantity WHERE idEtcSubInventory = @charSubinventory AND EtcBase_idEtc = boughtItemID;
			ELSEIF (@itemQuantityOwned IS NULL) THEN
				UPDATE store SET stock = stock - boughtItemQuantity WHERE idItem = boughtItemID;
                UPDATE inventory SET mesos = mesos - (@itemPrice * boughtItemQuantity) WHERE idInventory = @charInventory;
				INSERT INTO etcsubinventory VALUES (@charSubinventory, @charInventory, boughtItemID, boughtItemQuantity);
            ELSE
				SET errorMessage = "Check if all given information is correct and exists";
            END IF;
            
		END IF;
    END $$ 
DELIMITER ;

DELIMITER $$
    CREATE PROCEDURE sellOnStore( 
    IN charName VARCHAR(20),
    IN typeOfItem VARCHAR(5),
    IN soldItemID CHAR(8),
    IN soldItemQuantity TINYINT UNSIGNED,
    IN soldItemRarity VARCHAR(9),
    OUT errorMessage VARCHAR(100)
    )
    BEGIN
		IF typeOfItem = 'Equip' THEN
			SET @stockInStore = (SELECT stock FROM maplestory.store WHERE idItem = soldItemID);
            SET @charMoney = (SELECT mesos FROM maplestory.character AS ch JOIN maplestory.inventory AS inv WHERE ch.name = charName AND ch.Inventory_idInventory = inv.idInventory);
            SET @charInventory = (SELECT Inventory_idInventory FROM maplestory.character WHERE name = charName);
            SET @charSubinventory = (SELECT idEquipSubInventory FROM maplestory.equipsubinventory WHERE Inventory_idInventory = @charInventory LIMIT 1);
            SET @itemValue = (SELECT value FROM maplestory.equipbase WHERE idEquip = soldItemID);
            SET @itemQuantityOwned = (SELECT equipQuantity FROM maplestory.equipsubinventory WHERE EquipBase_idEquip = soldItemID AND idEquipSubInventory = @charSubinventory AND equipRarity = soldItemRarity);
            IF (@itemQuantityOwned IS NOT NULL) AND (@itemQuantityOwned < soldItemQuantity) THEN
				SET errorMessage = "Character does not have enough items to sell";
			ELSEIF (@charMoney + @itemValue*soldItemQuantity) > 99999999999 THEN
				SET errorMessage = "Character cannot have that much money";
			ELSEIF (@itemQuantityOwned IS NOT NULL) and (@stockInStore + soldItemQuantity > (~0 >> 32)) THEN
				SET errorMessage = "Store does not have enough space in stock";
			ELSEIF (@itemQuantityOwned IS NOT NULL) THEN
				IF (@stockInStore IS NULL) THEN
					INSERT INTO store VALUE (soldItemID, @itemValue*1.5, soldItemQuantity);
				ELSE
					UPDATE store SET stock = stock + soldItemQuantity WHERE idItem = soldItemID;
                END IF;
                UPDATE inventory SET mesos = mesos + (@itemValue * soldItemQuantity) WHERE idInventory = @charInventory;
                UPDATE equipsubinventory SET equipQuantity = equipQuantity - soldItemQuantity WHERE idEquipSubInventory = @charSubinventory AND EquipBase_idEquip = soldItemID;
				SET @itemQuantityOwned = (SELECT equipQuantity FROM maplestory.equipsubinventory WHERE EquipBase_idEquip = soldItemID AND idEquipSubInventory = @charSubinventory AND equipRarity = soldItemRarity);
                IF @itemQuantityOwned = 0 THEN
					DELETE FROM equipsubinventory WHERE idEquipSubInventory = @charSubinventory AND EquipBase_idEquip = soldItemID AND equipQuantity = 0;
                END IF;
			ELSE
				SET errorMessage = "Check if all given information is correct and exists";
            END IF;
        
		ELSEIF typeOfItem = 'Use' THEN
			SET @stockInStore = (SELECT stock FROM maplestory.store WHERE idItem = soldItemID);
            SET @charMoney = (SELECT mesos FROM maplestory.character AS ch JOIN maplestory.inventory AS inv WHERE ch.name = charName AND ch.Inventory_idInventory = inv.idInventory);
            SET @charInventory = (SELECT Inventory_idInventory FROM maplestory.character WHERE name = charName);
            SET @charSubinventory = (SELECT idUseSubInventory FROM maplestory.usesubinventory WHERE Inventory_idInventory = @charInventory LIMIT 1);
            SET @itemValue = (SELECT value FROM maplestory.usebase WHERE idUse = soldItemID);
            SET @itemQuantityOwned = (SELECT useQuantity FROM maplestory.usesubinventory WHERE UseBase_idUse = soldItemID AND idUseSubInventory = @charSubinventory);
            IF (@itemQuantityOwned IS NOT NULL) AND (@itemQuantityOwned < soldItemQuantity) THEN
				SET errorMessage = "Character does not have enough items to sell";
			ELSEIF (@charMoney + @itemValue*soldItemQuantity) > 99999999999 THEN
				SET errorMessage = "Character cannot have that much money";
			ELSEIF (@itemQuantityOwned IS NOT NULL) and (@stockInStore + soldItemQuantity > (~0 >> 32)) THEN
				SET errorMessage = "Store does not have enough space in stock";
			ELSEIF (@itemQuantityOwned IS NOT NULL) THEN
				IF (@stockInStore IS NULL) THEN
					INSERT INTO store VALUE (soldItemID, @itemValue*1.5, soldItemQuantity);
				ELSE
					UPDATE store SET stock = stock + soldItemQuantity WHERE idItem = soldItemID;
                END IF;
                UPDATE inventory SET mesos = mesos + (@itemValue * soldItemQuantity) WHERE idInventory = @charInventory;
                UPDATE usesubinventory SET useQuantity = useQuantity - soldItemQuantity WHERE idUseSubInventory = @charSubinventory AND UseBase_idUse = soldItemID;
				SET @itemQuantityOwned = (SELECT useQuantity FROM maplestory.usesubinventory WHERE UseBase_idUse = soldItemID AND idUseSubInventory = @charSubinventory);
                IF @itemQuantityOwned = 0 THEN
					DELETE FROM usesubinventory WHERE idUseSubInventory = @charSubinventory AND UseBase_idUse = soldItemID AND useQuantity = 0;
                END IF;
			ELSE
				SET errorMessage = "Check if all given information is correct and exists";
            END IF;
            
		ELSE
			SET @stockInStore = (SELECT stock FROM maplestory.store WHERE idItem = soldItemID);
            SET @charMoney = (SELECT mesos FROM maplestory.character AS ch JOIN maplestory.inventory AS inv WHERE ch.name = charName AND ch.Inventory_idInventory = inv.idInventory);
            SET @charInventory = (SELECT Inventory_idInventory FROM maplestory.character WHERE name = charName);
            SET @charSubinventory = (SELECT idEtcSubInventory FROM maplestory.etcsubinventory WHERE Inventory_idInventory = @charInventory LIMIT 1);
            SET @itemValue = (SELECT value FROM maplestory.etcbase WHERE idEtc = soldItemID);
            SET @itemQuantityOwned = (SELECT etcQuantity FROM maplestory.etcsubinventory WHERE EtcBase_idEtc = soldItemID AND idEtcSubInventory = @charSubinventory);
            IF (@itemQuantityOwned IS NOT NULL) AND (@itemQuantityOwned < soldItemQuantity) THEN
				SET errorMessage = "Character does not have enough items to sell";
			ELSEIF (@charMoney + @itemValue*soldItemQuantity) > 99999999999 THEN
				SET errorMessage = "Character cannot have that much money";
			ELSEIF (@itemQuantityOwned IS NOT NULL) and (@stockInStore + soldItemQuantity > (~0 >> 32)) THEN
				SET errorMessage = "Store does not have enough space in stock";
			ELSEIF (@itemQuantityOwned IS NOT NULL) THEN
				IF (@stockInStore IS NULL) THEN
					INSERT INTO store VALUE (soldItemID, @itemValue*1.5, soldItemQuantity);
				ELSE
					UPDATE store SET stock = stock + soldItemQuantity WHERE idItem = soldItemID;
				END IF;
                UPDATE inventory SET mesos = mesos + (@itemValue * soldItemQuantity) WHERE idInventory = @charInventory;
                UPDATE etcsubinventory SET etcQuantity = etcQuantity - soldItemQuantity WHERE idEtcSubInventory = @charSubinventory AND EtcBase_idEtc = soldItemID;
				SET @itemQuantityOwned = (SELECT etcQuantity FROM maplestory.etcsubinventory WHERE EtcBase_idEtc = soldItemID AND idEtcSubInventory = @charSubinventory);
                IF @itemQuantityOwned = 0 THEN
					DELETE FROM etcsubinventory WHERE idEtcSubInventory = @charSubinventory AND EtcBase_idEtc = soldItemID AND etcQuantity = 0;
                END IF;
			ELSE
				SET errorMessage = "Check if all given information is correct and exists";
            END IF;
            
		END IF;
    END $$ 
DELIMITER ;