import sys
sys.path.append(sys.path[0]+"\qt")

from dbConnection import mydb, mycursor 
from qt import mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

import Map
import Store
import Account
import Inventory
import EquipBase
import UseBase
import EtcBase

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
#Store.selectAll()
#printTerminal()


#Account.insert("leevanf","teste123",None,"2013-08-02","BR","Brazilian Portuguese","8009");
#Account.delete("leevanf")
#Account.deleteAll()
#Account.select("leevanf")
#Account.update("leevanf","5",None,"BR","french","8")
#Account.selectAll()
#printTerminal()


#Inventory.insert("0leevanf","2654332984","2473")
#Inventory.insert("annahild","150489556","2473")
#Inventory.delete("0leevanf")
#Inventory.deleteAll()
#Inventory.select("0leevanf")
#Inventory.update("0leevanf","10","8")
#Inventory.selectAll()
#printTerminal()



#EquipBase.insert("w1111111","Arcane Umbra Two Handed Sword","Warrior","255","0","STR","40","100000")
#EquipBase.delete("w1111111")
#EquipBase.deleteAll()
#EquipBase.select("w1111111")
#EquipBase.update("w1111111","Arcane Umbra Two Handed Sword","W","2","0","STR","40","1")
#EquipBase.selectAll()
#printTerminal()


#UseBase.insert("g1111111","Power Elixir","99999","99999","0","3000")
#UseBase.delete("g1111111")
#UseBase.deleteAll()
#UseBase.select("g1111111")
#UseBase.update("g1111111","Power Elixir","9","9","0","3")
#UseBase.selectAll()
#printTerminal()


#EtcBase.insert("m1111111","Necki Jr. Skin","237")
#EtcBase.delete("m1111111")
#EtcBase.deleteAll()
#EtcBase.select("m1111111")
#EtcBase.update("m1111111","Necki Jr. Skin","1")
#EtcBase.selectAll()
#printTerminal()





# INSERT INTO maplestory.character VALUES ("LeevOrDie","Warrior","STR",241,97000,15000,150000000000,"Luna",101325,"0leevanf");
# INSERT INTO maplestory.character VALUES ("Annahild","Archer","DEX",206,23487,19554,14595625100,"Luna",145,"annahild");

# INSERT INTO accounttocharacter VALUES ("leevanf","LeevOrDie","2015-05-05"),("leevanf","Annahild","2018-04-02");

# INSERT INTO equipsubinventory (Inventory_idInventory, EquipBase_idEquip, equipQuantity, equipRarity) VALUES ("0leevanf","w1111111",1,"Unique");

# INSERT INTO usesubinventory (Inventory_idInventory, UseBase_idUse, useQuantity) VALUES ("0leevanf","g1111111",255),("0leevanf","g1111111",150);

# INSERT INTO etcsubinventory (Inventory_idInventory, EtcBase_idEtc, etcQuantity) VALUES ("0leevanf","m1111111",100);


sys.exit(app.exec_())