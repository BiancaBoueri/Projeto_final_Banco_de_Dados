# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'characterManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from characterManagerAdvancedView import Ui_characterManagerAdvancedView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import Character

grey_background = "background-color: rgb(245, 245, 245);"
white_background = "background-color: rgb(255, 255, 255);"

ADD_BUTTON = -2
VIEW_BUTTON = -3
UPDATE_BUTTON = -4
DELETE_BUTTON = -5

class Ui_characterManager(object):
    def setupUi(self, characterManager):
        characterManager.setObjectName("characterManager")
        characterManager.resize(590, 349)
        characterManager.setMinimumSize(QtCore.QSize(590, 349))
        characterManager.setMaximumSize(QtCore.QSize(590, 349))
        icon = QIcon()
        icon.addFile(u"images\maplestoryIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        characterManager.setWindowIcon(icon)
        characterManager.setStyleSheet(white_background)

        self.username = QtWidgets.QLineEdit(characterManager)
        self.username.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.username.setText("")
        self.username.setObjectName("username")

        self.charMP = QtWidgets.QLineEdit(characterManager)
        self.charMP.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.charMP.setText("")
        self.charMP.setObjectName("charMP")

        self.charClass = QtWidgets.QLineEdit(characterManager)
        self.charClass.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.charClass.setText("")
        self.charClass.setObjectName("charClass")

        self.charName = QtWidgets.QLineEdit(characterManager)
        self.charName.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.charName.setText("")
        self.charName.setObjectName("charName")

        self.charHP = QtWidgets.QLineEdit(characterManager)
        self.charHP.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.charHP.setText("")
        self.charHP.setObjectName("charHP")

        self.createRadioButton = QtWidgets.QRadioButton(characterManager)
        self.createRadioButton.setGeometry(QtCore.QRect(20, 20, 91, 17))
        self.createRadioButton.setObjectName("createRadioButton")

        self.readRadioButton = QtWidgets.QRadioButton(characterManager)
        self.readRadioButton.setGeometry(QtCore.QRect(170, 20, 101, 17))
        self.readRadioButton.setObjectName("readRadioButton")

        self.updateRadioButton = QtWidgets.QRadioButton(characterManager)
        self.updateRadioButton.setGeometry(QtCore.QRect(320, 20, 111, 17))
        self.updateRadioButton.setObjectName("updateRadioButton")

        self.deleteRadioButton = QtWidgets.QRadioButton(characterManager)
        self.deleteRadioButton.setGeometry(QtCore.QRect(470, 20, 101, 17))
        self.deleteRadioButton.setObjectName("deleteRadioButton")

        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.addButton(self.createRadioButton)
        self.buttonGroup.addButton(self.readRadioButton)
        self.buttonGroup.addButton(self.updateRadioButton)
        self.buttonGroup.addButton(self.deleteRadioButton)

        self.charAttribute = QtWidgets.QComboBox(characterManager)
        self.charAttribute.setGeometry(QtCore.QRect(20, 220, 111, 22))
        self.charAttribute.setStyleSheet(grey_background)
        self.charAttribute.setObjectName("charAttribute")
        self.charAttribute.addItem("")
        self.charAttribute.addItem("")
        self.charAttribute.addItem("")
        self.charAttribute.addItem("")

        self.charLevel = QtWidgets.QSpinBox(characterManager)
        self.charLevel.setGeometry(QtCore.QRect(50, 260, 42, 22))
        self.charLevel.setStyleSheet(grey_background)
        self.charLevel.setMaximum(255)
        self.charLevel.setObjectName("charLevel")

        self.levelLabel = QtWidgets.QLabel(characterManager)
        self.levelLabel.setGeometry(QtCore.QRect(20, 260, 31, 21))
        self.levelLabel.setStyleSheet("background-color: rgb(255, 255, 255, 0);")
        self.levelLabel.setObjectName("levelLabel")

        self.charEXP = QtWidgets.QLineEdit(characterManager)
        self.charEXP.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.charEXP.setText("")
        self.charEXP.setObjectName("charEXP")

        self.server = QtWidgets.QLineEdit(characterManager)
        self.server.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.server.setText("")
        self.server.setObjectName("server")

        self.charMap = QtWidgets.QLineEdit(characterManager)
        self.charMap.setGeometry(QtCore.QRect(150, 180, 113, 20))
        self.charMap.setText("")
        self.charMap.setObjectName("charMap")

        self.charInventory = QtWidgets.QLineEdit(characterManager)
        self.charInventory.setGeometry(QtCore.QRect(150, 220, 113, 20))
        self.charInventory.setText("")
        self.charInventory.setObjectName("charInventory")

        self.advancedViewButton = QtWidgets.QPushButton(characterManager)
        self.advancedViewButton.setGeometry(QtCore.QRect(150, 300, 111, 31))
        self.advancedViewButton.setStyleSheet(grey_background)
        self.advancedViewButton.setObjectName("advancedViewButton")
        self.advancedViewButton.clicked.connect(self.callAdvancedView)

        self.okButton = QtWidgets.QPushButton(characterManager)
        self.okButton.setGeometry(QtCore.QRect(20, 300, 111, 31))
        self.okButton.setStyleSheet(grey_background)
        self.okButton.setObjectName("okViewButton")
        self.okButton.clicked.connect(lambda: self.parseInformation())

        self.output = QtWidgets.QTableWidget(characterManager)
        self.output.setGeometry(QtCore.QRect(280, 60, 291, 271))
        self.output.setObjectName("output")
        self.output.setColumnCount(11)

        column1 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(0, column1)
        column2 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(1, column2)
        column3 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(2, column3)
        column4 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(3, column4)
        column5 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(4, column5)
        column6 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(5, column6)
        column7 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(6, column7)
        column8 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(7, column8)
        column9 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(8, column9)
        column10 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(9, column10)
        column11 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(10, column11)

        column1 = self.output.horizontalHeaderItem(0)
        column1.setText(QtCore.QCoreApplication.translate("characterManager", "Username"))
        column2 = self.output.horizontalHeaderItem(1)
        column2.setText(QtCore.QCoreApplication.translate("characterManager", "Character Name"))
        column3 = self.output.horizontalHeaderItem(2)
        column3.setText(QtCore.QCoreApplication.translate("characterManager", "Character Class"))
        column4 = self.output.horizontalHeaderItem(3)
        column4.setText(QtCore.QCoreApplication.translate("characterManager", "Server"))
        column5 = self.output.horizontalHeaderItem(4)
        column5.setText(QtCore.QCoreApplication.translate("characterManager", "Attribute"))
        column6 = self.output.horizontalHeaderItem(5)
        column6.setText(QtCore.QCoreApplication.translate("characterManager", "Level"))
        column7 = self.output.horizontalHeaderItem(6)
        column7.setText(QtCore.QCoreApplication.translate("characterManager", "HP"))
        column8 = self.output.horizontalHeaderItem(7)
        column8.setText(QtCore.QCoreApplication.translate("characterManager", "MP"))
        column9 = self.output.horizontalHeaderItem(8)
        column9.setText(QtCore.QCoreApplication.translate("characterManager", "EXP"))
        column10 = self.output.horizontalHeaderItem(9)
        column10.setText(QtCore.QCoreApplication.translate("characterManager", "Last Map"))
        column11 = self.output.horizontalHeaderItem(10)
        column11.setText(QtCore.QCoreApplication.translate("characterManager", "Inventory ID"))

        self.retranslateUi(characterManager)
        QtCore.QMetaObject.connectSlotsByName(characterManager)

    def retranslateUi(self, characterManager):
        _translate = QtCore.QCoreApplication.translate
        characterManager.setWindowTitle(_translate("characterManager", "Maplestory Manager - Character"))
        self.charMP.setPlaceholderText(_translate("characterManager", "MP"))
        self.createRadioButton.setText(_translate("characterManager", "Add Character"))
        self.advancedViewButton.setText(_translate("characterManager", "Advanced View..."))
        self.charClass.setPlaceholderText(_translate("characterManager", "Character Class"))
        self.charName.setPlaceholderText(_translate("characterManager", "Character Name"))
        self.charHP.setPlaceholderText(_translate("characterManager", "HP"))
        self.deleteRadioButton.setText(_translate("characterManager", "Delete Character"))
        self.readRadioButton.setText(_translate("characterManager", "View Character"))
        self.updateRadioButton.setText(_translate("characterManager", "Update Character"))
        self.charAttribute.setItemText(0, _translate("characterManager", "STR"))
        self.charAttribute.setItemText(1, _translate("characterManager", "DEX"))
        self.charAttribute.setItemText(2, _translate("characterManager", "INT"))
        self.charAttribute.setItemText(3, _translate("characterManager", "LUK"))
        self.levelLabel.setText(_translate("characterManager", "Level"))
        self.charEXP.setPlaceholderText(_translate("characterManager", "EXP"))
        self.server.setPlaceholderText(_translate("characterManager", "Server"))
        self.charMap.setPlaceholderText(_translate("characterManager", "Last Map Visited"))
        self.charInventory.setPlaceholderText(_translate("characterManager", "Inventory ID"))
        self.okButton.setText(_translate("characterManager", "OK"))
        self.username.setPlaceholderText(_translate("characterManager", "Username"))

    def callAdvancedView(self):
        self.characterManagerAdvancedViewWindow = QtWidgets.QWidget()
        self.ui = Ui_characterManagerAdvancedView()
        self.ui.setupUi(self.characterManagerAdvancedViewWindow)
        self.characterManagerAdvancedViewWindow.show()

    def parseInformation(self):
        tempUsername = self.username.text()
        tempCharacterName = self.charName.text()
        tempCharacterClass = self.charClass.text()
        tempServer = self.server.text()
        tempAttribute = self.charAttribute.currentText()
        tempLevel = self.charLevel.text()
        tempHP = self.charHP.text()
        tempMP = self.charMP.text()
        tempEXP = self.charEXP.text()
        tempLastMap = self.charMap.text()
        tempInventoryID = self.charInventory.text()
        action = self.buttonGroup.checkedId()

        if (action == ADD_BUTTON):
            Character.insert(tempUsername, tempCharacterName, tempCharacterClass, tempAttribute, tempLevel, tempHP, tempMP, tempEXP, tempServer, tempLastMap, tempInventoryID)
        
        elif (action == VIEW_BUTTON):
            if (not tempUsername and not tempCharacterName and not tempCharacterClass and not tempServer and not tempAttribute and not tempLevel and not tempHP and not tempMP and not tempEXP and not tempServer and not tempLastMap and not tempInventoryID):
                result = Character.selectAll()
            else:
                result = Character.select(tempCharacterName)
                result = [result]
            self.output.setRowCount(len(result))
            for i in range(len(result)):
                self.output.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
                self.output.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
                self.output.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))
                self.output.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][3])))
                self.output.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[i][4])))
                self.output.setItem(i, 5, QtWidgets.QTableWidgetItem(str(result[i][5])))
                self.output.setItem(i, 6, QtWidgets.QTableWidgetItem(str(result[i][6])))
                self.output.setItem(i, 7, QtWidgets.QTableWidgetItem(str(result[i][7])))
                self.output.setItem(i, 8, QtWidgets.QTableWidgetItem(str(result[i][8])))
                self.output.setItem(i, 9, QtWidgets.QTableWidgetItem(str(result[i][9])))
                self.output.setItem(i, 10, QtWidgets.QTableWidgetItem(str(result[i][10])))

        elif (action == UPDATE_BUTTON):
            Character.update(tempCharacterName, tempCharacterClass, tempAttribute, tempLevel, tempHP, tempMP, tempEXP, tempServer, tempLastMap)

        elif (action == DELETE_BUTTON):
            Character.delete(tempCharacterName)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    characterManager = QtWidgets.QWidget()
    ui = Ui_characterManager()
    ui.setupUi(characterManager)
    characterManager.show()
    sys.exit(app.exec_())
