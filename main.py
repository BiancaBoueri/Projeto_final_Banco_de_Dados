import Map
import Store
import Account
import Inventory
import EquipBase
import UseBase
import EtcBase
import EquipSubInventory
import UseSubInventory
import EtcSubInventory
import Character

import sys
sys.path.append(sys.path[0]+"\qt")
from qt import mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


app = QtWidgets.QApplication(sys.argv)
appWindow = QtWidgets.QMainWindow()
ui = mainWindow.Ui_mainWindow()
ui.setupUi(appWindow)
appWindow.show()


#Map.insert("101325","Mirror Touched Sea 5","3")
#Map.insert("145","Ruined Past 5","4")
#Map.delete("1")
#Map.deleteAll()
#print(Map.select("145"))
#Map.update("145","p","9")
#print(Map.selectAll())

#Store.insert("w1111111","1999999999","1")
#Store.insert("g1111111","5999","150000")
#Store.insert("g","5","1")
#Store.delete("g1111111")
#Store.deleteAll()
#Store.update('w1111111',"5","99")
#print(Store.selectAll())
#print(Store.select("g1111111"))

#Account.insert("leevanf4","teste123","./images/avatar.png","BR","Brazilian Portuguese","8009")
#Account.insert("leevanf3","teste123",None,"BR","Brazilian Portuguese","8009")
#Account.delete("leevanf4")
#Account.deleteAll()
#print(Account.select("leevanf"))
#Account.update("leevanf4","teste","./images/avatar.png","B","Portuguese","80")
#print(Account.selectAll())

#Inventory.insert("0leevanf","2654332984","2473")
#Inventory.insert("annahild","150489556","2473")
#Inventory.delete("0leevanf")
#Inventory.deleteAll()
#print(Inventory.select("0leevanf"))
#Inventory.update("0leevanf","10","8")
#print(Inventory.selectAll())

#EquipBase.insert("w1111111","Arcane Umbra Two Handed Sword","Warrior","255","0","STR","40","100000")
#EquipBase.delete("w1111111")
#EquipBase.deleteAll()
#print(EquipBase.select("w1111111"))
#EquipBase.update("w1111111","Arcane Umbra Two Handed Sword","W","2","0","STR","40","1")
#print(EquipBase.selectAll())

#UseBase.insert("g1111111","Power Elixir","99999","99999","0","3000")
#UseBase.delete("g1111111")
#UseBase.deleteAll()
#print(UseBase.select("g1111111"))
#UseBase.update("g1111111","Power Elixir","9","9","0","3")
#print(UseBase.selectAll())

#EtcBase.insert("m1111111","Necki Jr. Skin","237")
#EtcBase.delete("m1111111")
#EtcBase.deleteAll()
#print(EtcBase.select("m1111111"))
#EtcBase.update("m1111111","Necki Jr. Skin","1")
#print(EtcBase.selectAll())

#EquipSubInventory.insert("0leevanf","w1111111","1","Unique")
#EquipSubInventory.delete("1")
#EquipSubInventory.deleteAll()
#print(EquipSubInventory.select("3"))
#EquipSubInventory.update("3","30","Nice")
#print(EquipSubInventory.selectAll())

#UseSubInventory.insert("0leevanf","g1111111","255"),
#UseSubInventory.insert("0leevanf","g1111111","150")
#UseSubInventory.delete("1")
#UseSubInventory.deleteAll()
#print(UseSubInventory.select("3"))
#UseSubInventory.update("3","1")
#print(UseSubInventory.selectAll())

#EtcSubInventory.insert("0leevanf","m1111111","100")
#EtcSubInventory.delete("1")
#EtcSubInventory.deleteAll()
#print(EtcSubInventory.select("3"))
#EtcSubInventory.update("3","1")
#print(EtcSubInventory.selectAll())
    
#Character.insert("leevanf","LeevOrDie8","Warrior","STR","241","97000","15000","150000000000","Luna","101325","0leevanf")
#Character.insert("leevanf","Annahild1","Archer","DEX","206","23487","19554","14595625100","Luna","145","annahild")
#Character.delete("Annahild1")
#Character.deleteAll()
#print(Character.select("Annahild1"))
#Character.update("Annahild1","A","D","2","23","14","100","L")
#print(Character.selectAll())


sys.exit(app.exec_())