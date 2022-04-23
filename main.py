import sys
sys.path.append(sys.path[0]+"\qt")

from dbConnection import mydb, mycursor 
from qt import mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import Map
import Store

def printTerminal():
  for i in mycursor: 
    print(i)
    #a,b,c = i
    #print(a,b,c)


print("main")

app = QtWidgets.QApplication(sys.argv)
appWindow = QtWidgets.QMainWindow()
ui = mainWindow.Ui_mainWindow()
ui.setupUi(appWindow)
appWindow.show()

#Map.insert("101325","Mirror Touched Sea 5","3")
#Map.insert("145","Ruined Past 5","4")
#Map.delete("1")
#Map.deleteAll()
#Map.select("145")
#Map.update("145","p","9")
#Map.selectAll()
#printTerminal()


#Store.insert("w1111111","1999999999","1")
#Store.insert("g1111111","5999","150000")
#Store.delete("g1111111")
#Store.deleteAll()
#Store.select("g1111111")
#Store.update('w1111111',"5","99")
Store.selectAll()
printTerminal()





# INSERT INTO maplestory.account VALUES ("leevanf","teste123",NULL,"2013-08-02","BR","Brazilian Portuguese",8009);

# INSERT INTO inventory VALUES ("0leevanf",2654332984,2473);
# INSERT INTO inventory VALUES ("annahild",150489556,2473);

# INSERT INTO maplestory.character VALUES ("LeevOrDie","Warrior","STR",241,97000,15000,150000000000,"Luna",101325,"0leevanf");
# INSERT INTO maplestory.character VALUES ("Annahild","Archer","DEX",206,23487,19554,14595625100,"Luna",145,"annahild");

# INSERT INTO accounttocharacter VALUES ("leevanf","LeevOrDie","2015-05-05"),("leevanf","Annahild","2018-04-02");

# INSERT INTO equipbase VALUES ("w1111111","Arcane Umbra Two Handed Sword","Warrior",255,0,"STR",40,100000);

# INSERT INTO usebase VALUES ("g1111111","Power Elixir",99999,99999,0,3000);

# INSERT INTO etcbase VALUES ("m1111111","Necki Jr. Skin",237);

# INSERT INTO equipsubinventory (Inventory_idInventory, EquipBase_idEquip, equipQuantity, equipRarity) VALUES ("0leevanf","w1111111",1,"Unique");

# INSERT INTO usesubinventory (Inventory_idInventory, UseBase_idUse, useQuantity) VALUES ("0leevanf","g1111111",255),("0leevanf","g1111111",150);

# INSERT INTO etcsubinventory (Inventory_idInventory, EtcBase_idEtc, etcQuantity) VALUES ("0leevanf","m1111111",100);


sys.exit(app.exec_())