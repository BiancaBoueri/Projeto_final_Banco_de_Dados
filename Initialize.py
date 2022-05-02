from logging.config import valid_ident
from dbConnection import mydb, mycursor 

def accountInitializer():
    sql = """ INSERT INTO maplestory.account VALUES ("leevanf","!myQTpa2","./images/avatar5.png","2010-08-02","BR","Brazilian Portuguese",8009),
    ("Miranda","plusultra","./images/avatar2.png","2014-04-09","BR","Portuguese",1496),
    ("Bianca","senhasegura","./images/avatar.png","2022-03-03","BR","Portuguese",1651),
    ("Haachama","H44CH4M4CH4M4","./images/avatar3.png","2013-08-02","JP","Japanese",8888),
    ("RickAstley","nevergonnagiveyouup",NULL,"1987-07-27","UK","British English",1987),
    ("BarryBenson","yalikejazz","./images/avatar4.png","2007-12-07","EN","American English",1856);"""
    mycursor.execute(sql)
    mydb.commit()

def mapInitializer():
    sql = """ INSERT INTO maplestory.map VALUES (101325, "Mirror Touched Sea 5", 3),
    (145, "Ruined Past 5", 4),
    (1, "Henesys", 1),
    (1985, "Path of Time", 2),
    (277, "Twilight Perion", 4),
    (4873, "Fire Plateau", 1),
    (6144, "Haunted House: Foyer", 5);"""
    mycursor.execute(sql)
    mydb.commit()

def inventoryInitializer():
    sql = """ INSERT INTO maplestory.inventory VALUES ("LeeInv00",2654332984,2473),
    ("AnnInv01",150489556,2473),
    ("AanInv23",184569223,0),
    ("BarInv64",1224556981,0),
    ("RicInv42",25664851330,94560),
    ("HacInv88",888888888,88888),
    ("MirInv32",756844123,2168);"""
    mycursor.execute(sql)
    mydb.commit()

def characterInitializer():
    sql = """ INSERT INTO maplestory.character VALUES ("LeevOrDie","Warrior","STR",241,97000,15000,150000000000,"Luna",101325,"LeeInv00"),
    ("Annahild","Archer","DEX",206,23487,19554,14595625100,"Luna",145,"AnnInv01"),
    ("Avatar","Mage","INT",59,4671,35644,242187670,"Demethos",1,"AanInv23"),
    ("Stinger","Warrior","STR",124,19440,6554,777861640,"Scania",6144,"BarInv64"),
    ("DesertYou","Pirate","DEX",220,64694,26544,121051278710,"Supreme",277,"RicInv42"),
    ("CH4MM3RS","Thief","LUK",88,8888,8888,88888888,"Holoalt",1985,"HacInv88"),
    ("Amal","Mage","Int",235,6999,45894,131951978990,"Gaia",101325,"MirInv32");"""
    mycursor.execute(sql)
    mydb.commit()

def accountToCharacterInitializer():
    sql = """ INSERT INTO maplestory.accounttocharacter VALUES ("leevanf","LeevOrDie","2015-05-05"),
    ("leevanf","Annahild","2018-04-02"),
    ("Bianca","Avatar","2022-03-03"),
    ("BarryBenson","Stinger","2008-11-12"),
    ("RickAstley","DesertYou","2014-01-01"),
    ("Haachama","CH4MM3RS","2018-08-08"),
    ("Miranda","Amal","2017-09-12");"""
    mycursor.execute(sql)
    mydb.commit()

def equipBaseInitializer():
    sql = """ INSERT INTO maplestory.equipbase VALUES ("w1111111","Arcane Umbra Two Handed Sword","Warrior",255,0,"STR",40,100000),
    ("w1111110","Arcane Umbra One Handed Sword","Warrior",250,0,"STR",45,100000),
    ("w1200000","Fafnir Bow","Archer",212,0,"DEX",25,84500),
    ("w1200001","Fafnir Crossbow","Archer",220,0,"DEX",15,84500),
    ("w1300000","Absolab Handgun","Pirate",218,0,"DEX",20,89500),
    ("w1400000","Frozen Claw","Thief",156,0,"LUK",10,15450),
    ("w1666000","Twisted Chaos Wand","Mage",240,0,"INT",50,450000);
    """
    mycursor.execute(sql)
    mydb.commit()

def useBaseInitializer():
    sql = """ INSERT INTO maplestory.usebase VALUES ("g1111111","Power Elixir",99999,99999,0,3000),
    ("g1111112","Ginger Ale", 49999, 49999, 0, 2500),
    ("g1211000","Red Potion", 50, 0, 0, 10),
    ("g1211001","Blue Potion", 0, 100, 0, 25),
    ("g1211002","White Potion", 300, 0, 0, 50),
    ("g2245000","Takoyaki", 0, 0, 25, 4500),
    ("g6655000","Mushmom Soup", 9500, 9500, 127, 945000);
    """
    mycursor.execute(sql)
    mydb.commit()

def etcBaseInitializer():
    sql = """ INSERT INTO maplestory.etcbase VALUES ("m1111111","Necki Jr. Skin",237),
    ("m1111112","Croc Skin",299),
    ("m4545000","Twisted Time",1),
    ("m6655441","DEX Crystal",15000),
    ("m6655442","STR Crystal",15000),
    ("m6655450","Dark Crystal",150000),
    ("m2222222","Mecateon Cannon",1250);"""
    mycursor.execute(sql)
    mydb.commit()

def equipSubInventoryInitializer():
    sql = """ INSERT INTO maplestory.equipsubinventory VALUES (1,"LeeInv00","w1111111",1,"Unique"),
    (1,"LeeInv00","w1111111",2,"Legendary"),
    (1,"LeeInv00","w1111111",1,"Epic"),
    (2,"AnnInv01","w1200000",1,"Rare"),
    (3,"AanInv23","w1666000",1,"Unique"),
    (4,"BarInv64","w1111110",1,"Rare"),
    (5,"RicInv42","w1300000",1,"Legendary"),
    (6,"HacInv88","w1400000",1,"Epic"),
    (7,"MirInv32","w1666000",1,"Rare");"""
    mycursor.execute(sql)
    mydb.commit()

def useSubInventoryInitializer():
    sql = """ INSERT INTO maplestory.usesubinventory VALUES (1,"LeeInv00","g1111111",250),
    (1,"LeeInv00","g6655000",5),
    (2,"AnnInv01","g2245000",2),
    (2,"AnnInv01","g1111112",250),
    (3,"AanInv23","g1211002",150),
    (4,"BarInv64","g1211001",100),
    (5,"RicInv42","g1211000",25),
    (6,"HacInv88","g1111111",128),
    (7,"MirInv32","g1211000",145);"""
    mycursor.execute(sql)
    mydb.commit()

def etcSubInventoryInitializer():
    sql = """ INSERT INTO maplestory.etcsubinventory VALUES (1,"LeeInv00","m6655442",14),
    (1,"LeeInv00","m4545000",2),
    (2,"AnnInv01","m1111112",25),
    (2,"AnnInv01","m1111111",65),
    (3,"AanInv23","m6655450",44),
    (4,"BarInv64","m6655442",189),
    (4,"BarInv64","m6655441",98),
    (5,"RicInv42","m6655441",9),
    (6,"HacInv88","m6655450",64),
    (7,"MirInv32","m2222222",2);"""
    mycursor.execute(sql)
    mydb.commit()

def storeInitializer():
    sql = """ INSERT INTO maplestory.store VALUES ("w1111111",1999999999,1),
    ("w1111110",1599999999,3),
    ("w1200000",12999999,1),
    ("w1200001",15999999,2),
    ("w1300000",1111111,1),
    ("w1400000",15151515,4),
    ("g1111112",5000,55899),
    ("g1211000",10,10000000),
    ("g1211001",30,10000000),
    ("g1211002",65,9000000),
    ("g2245000",19999,15),
    ("g6655000",1500000,2),
    ("m6655440",65000,500),
    ("m6655441",19111,100),
    ("m6655442",25111,17);"""
    mycursor.execute(sql)
    mydb.commit()


def initializeTables():
    accountInitializer()
    mapInitializer()
    inventoryInitializer()
    characterInitializer()
    accountToCharacterInitializer()
    equipBaseInitializer()
    useBaseInitializer()
    etcBaseInitializer()
    equipSubInventoryInitializer()
    useSubInventoryInitializer()
    etcSubInventoryInitializer()
    storeInitializer()