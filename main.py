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

sys.exit(app.exec_())