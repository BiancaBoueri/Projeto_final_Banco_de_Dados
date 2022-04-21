# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventoryManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

grey_background = "background-color: rgb(245, 245, 245);"
white_background = "background-color: rgb(255, 255, 255);"

class Ui_inventoryManager(object):
    def setupUi(self, inventoryManager):
        inventoryManager.setObjectName("inventoryManager")
        inventoryManager.resize(592, 324)
        icon = QIcon()
        icon.addFile(u"images\maplestoryIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        inventoryManager.setWindowIcon(icon)
        inventoryManager.setStyleSheet(white_background)

        self.characterID = QtWidgets.QLineEdit(inventoryManager)
        self.characterID.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.characterID.setText("")
        self.characterID.setObjectName("characterID")

        self.inventoryId = QtWidgets.QLineEdit(inventoryManager)
        self.inventoryId.setGeometry(QtCore.QRect(20, 120, 113, 20))
        self.inventoryId.setText("")
        self.inventoryId.setObjectName("inventoryId")

        self.output = QtWidgets.QListView(inventoryManager)
        self.output.setGeometry(QtCore.QRect(320, 10, 256, 301))
        self.output.setObjectName("output")

        self.readInventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.readInventoryRadioButton.setGeometry(QtCore.QRect(20, 50, 41, 17))
        self.readInventoryRadioButton.setObjectName("readInventoryRadioButton")

        self.subinventoryID = QtWidgets.QLineEdit(inventoryManager)
        self.subinventoryID.setGeometry(QtCore.QRect(170, 120, 113, 20))
        self.subinventoryID.setText("")
        self.subinventoryID.setObjectName("subinventoryID")

        self.createInventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.createInventoryRadioButton.setGeometry(QtCore.QRect(20, 30, 41, 17))
        self.createInventoryRadioButton.setObjectName("createInventoryRadioButton")

        self.inventoryForeignID = QtWidgets.QLineEdit(inventoryManager)
        self.inventoryForeignID.setGeometry(QtCore.QRect(170, 80, 113, 20))
        self.inventoryForeignID.setText("")
        self.inventoryForeignID.setObjectName("inventoryForeignID")

        self.nx = QtWidgets.QLineEdit(inventoryManager)
        self.nx.setGeometry(QtCore.QRect(20, 200, 113, 20))
        self.nx.setText("")
        self.nx.setObjectName("nx")

        self.okButton = QtWidgets.QPushButton(inventoryManager)
        self.okButton.setGeometry(QtCore.QRect(20, 280, 261, 31))
        self.okButton.setStyleSheet(grey_background)
        self.okButton.setObjectName("okButton")

        self.updateInventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.updateInventoryRadioButton.setGeometry(QtCore.QRect(80, 30, 61, 17))
        self.updateInventoryRadioButton.setObjectName("updateInventoryRadioButton")

        self.itemID = QtWidgets.QLineEdit(inventoryManager)
        self.itemID.setGeometry(QtCore.QRect(170, 160, 113, 20))
        self.itemID.setText("")
        self.itemID.setObjectName("itemID")

        self.deleteInventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.deleteInventoryRadioButton.setGeometry(QtCore.QRect(80, 50, 51, 17))
        self.deleteInventoryRadioButton.setObjectName("deleteInventoryRadioButton")

        self.inventoryLabel = QtWidgets.QLabel(inventoryManager)
        self.inventoryLabel.setGeometry(QtCore.QRect(20, 10, 111, 16))
        self.inventoryLabel.setObjectName("inventoryLabel")

        self.subinventoryLabel = QtWidgets.QLabel(inventoryManager)
        self.subinventoryLabel.setGeometry(QtCore.QRect(170, 10, 111, 16))
        self.subinventoryLabel.setObjectName("subinventoryLabel")

        self.deleteSubinventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.deleteSubinventoryRadioButton.setGeometry(QtCore.QRect(230, 50, 51, 17))
        self.deleteSubinventoryRadioButton.setObjectName("deleteSubinventoryRadioButton")

        self.readSubinventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.readSubinventoryRadioButton.setGeometry(QtCore.QRect(170, 50, 41, 17))
        self.readSubinventoryRadioButton.setObjectName("readSubinventoryRadioButton")

        self.updateSubinventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.updateSubinventoryRadioButton.setGeometry(QtCore.QRect(230, 30, 61, 17))
        self.updateSubinventoryRadioButton.setObjectName("updateSubinventoryRadioButton")

        self.createSubinventoryRadioButton = QtWidgets.QRadioButton(inventoryManager)
        self.createSubinventoryRadioButton.setGeometry(QtCore.QRect(170, 30, 41, 17))
        self.createSubinventoryRadioButton.setObjectName("createSubinventoryRadioButton")

        self.mesos = QtWidgets.QLineEdit(inventoryManager)
        self.mesos.setGeometry(QtCore.QRect(20, 160, 113, 20))
        self.mesos.setText("")
        self.mesos.setObjectName("mesos")

        self.quantity = QtWidgets.QLineEdit(inventoryManager)
        self.quantity.setGeometry(QtCore.QRect(170, 200, 113, 20))
        self.quantity.setObjectName("quantity")
        
        self.rarity = QtWidgets.QLineEdit(inventoryManager)
        self.rarity.setGeometry(QtCore.QRect(170, 240, 113, 20))
        self.rarity.setObjectName("rarity")

        self.retranslateUi(inventoryManager)
        QtCore.QMetaObject.connectSlotsByName(inventoryManager)

    def retranslateUi(self, inventoryManager):
        _translate = QtCore.QCoreApplication.translate
        inventoryManager.setWindowTitle(_translate("inventoryManager", "Maplestory Manager - Inventory"))
        self.inventoryId.setPlaceholderText(_translate("inventoryManager", "Inventory ID"))
        self.readInventoryRadioButton.setText(_translate("inventoryManager", "View"))
        self.characterID.setPlaceholderText(_translate("inventoryManager", "Character (ID)"))
        self.subinventoryID.setPlaceholderText(_translate("inventoryManager", "SubInventory ID"))
        self.createInventoryRadioButton.setText(_translate("inventoryManager", "Add"))
        self.inventoryForeignID.setPlaceholderText(_translate("inventoryManager", "Parent Inventory (ID)"))
        self.nx.setPlaceholderText(_translate("inventoryManager", "NX"))
        self.okButton.setText(_translate("inventoryManager", "OK"))
        self.updateInventoryRadioButton.setText(_translate("inventoryManager", "Update"))
        self.itemID.setPlaceholderText(_translate("inventoryManager", "Item (ID)"))
        self.deleteInventoryRadioButton.setText(_translate("inventoryManager", "Delete"))
        self.inventoryLabel.setText(_translate("inventoryManager", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Inventory</span></p></body></html>"))
        self.subinventoryLabel.setText(_translate("inventoryManager", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Subinventory</span></p></body></html>"))
        self.deleteSubinventoryRadioButton.setText(_translate("inventoryManager", "Delete"))
        self.readSubinventoryRadioButton.setText(_translate("inventoryManager", "View"))
        self.updateSubinventoryRadioButton.setText(_translate("inventoryManager", "Update"))
        self.createSubinventoryRadioButton.setText(_translate("inventoryManager", "Add"))
        self.mesos.setPlaceholderText(_translate("inventoryManager", "Mesos"))
        self.quantity.setPlaceholderText(_translate("inventoryManager", "Quantity"))
        self.rarity.setPlaceholderText(_translate("inventoryManager", "Rarity (EQUIP ONLY)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    inventoryManager = QtWidgets.QWidget()
    ui = Ui_inventoryManager()
    ui.setupUi(inventoryManager)
    inventoryManager.show()
    sys.exit(app.exec_())