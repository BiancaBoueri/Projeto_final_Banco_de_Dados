# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMessageBox, QErrorMessage
import Map

grey_background = "background-color: rgb(245, 245, 245);"
white_background = "background-color: rgb(255, 255, 255);"

ADD_BUTTON = -2
VIEW_BUTTON = -3
UPDATE_BUTTON = -4
DELETE_BUTTON = -5

class Ui_mapManager(object):
    def setupUi(self, mapManager):
        mapManager.setObjectName("mapManager")
        mapManager.resize(400, 215)
        mapManager.setMinimumSize(QtCore.QSize(400, 215))
        mapManager.setMaximumSize(QtCore.QSize(400, 215))
        icon = QIcon()
        icon.addFile(u"images\maplestoryIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        mapManager.setWindowIcon(icon)
        mapManager.setStyleSheet(white_background)

        self.idMap = QtWidgets.QLineEdit(mapManager)
        self.idMap.setGeometry(QtCore.QRect(10, 50, 113, 20))
        self.idMap.setText("")
        self.idMap.setObjectName("idMap")

        self.mapName = QtWidgets.QLineEdit(mapManager)
        self.mapName.setGeometry(QtCore.QRect(10, 90, 113, 20))
        self.mapName.setText("")
        self.mapName.setObjectName("mapName")

        self.spawnPosition = QtWidgets.QLineEdit(mapManager)
        self.spawnPosition.setGeometry(QtCore.QRect(10, 130, 113, 20))
        self.spawnPosition.setText("")
        self.spawnPosition.setObjectName("spawnPosition")

        self.okButton = QtWidgets.QPushButton(mapManager)
        self.okButton.setGeometry(QtCore.QRect(10, 170, 111, 31))
        self.okButton.setStyleSheet(grey_background)
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(lambda: self.parseInformation())
        #self.okButton.clicked.connect(lambda: self.alertBox())

        self.createRadioButton = QtWidgets.QRadioButton(mapManager)
        self.createRadioButton.setGeometry(QtCore.QRect(10, 10, 61, 17))
        self.createRadioButton.setObjectName("createRadioButton")

        self.readRadioButton = QtWidgets.QRadioButton(mapManager)
        self.readRadioButton.setGeometry(QtCore.QRect(110, 10, 71, 17))
        self.readRadioButton.setObjectName("readRadioButton")

        self.updateRadioButton = QtWidgets.QRadioButton(mapManager)
        self.updateRadioButton.setGeometry(QtCore.QRect(210, 10, 81, 17))
        self.updateRadioButton.setObjectName("updateRadioButton")

        self.deleteRadioButton = QtWidgets.QRadioButton(mapManager)
        self.deleteRadioButton.setGeometry(QtCore.QRect(310, 10, 81, 17))
        self.deleteRadioButton.setObjectName("deleteRadioButton")

        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.addButton(self.createRadioButton)
        self.buttonGroup.addButton(self.readRadioButton)
        self.buttonGroup.addButton(self.updateRadioButton)
        self.buttonGroup.addButton(self.deleteRadioButton)
        
        self.output = QtWidgets.QTableWidget(mapManager)
        self.output.setGeometry(QtCore.QRect(145, 50, 241, 151))
        self.output.setMinimumSize(QtCore.QSize(241, 151))
        self.output.setObjectName("output")
        self.output.setColumnCount(3)

        column1 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(0, column1)
        column2 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(1, column2)
        column3 = QtWidgets.QTableWidgetItem()
        self.output.setHorizontalHeaderItem(2, column3)

        column1 = self.output.horizontalHeaderItem(0)
        column1.setText(QtCore.QCoreApplication.translate("mapManager", "Map ID"))
        column2 = self.output.horizontalHeaderItem(1)
        column2.setText(QtCore.QCoreApplication.translate("mapManager", "Map Name"))
        column3 = self.output.horizontalHeaderItem(2)
        column3.setText(QtCore.QCoreApplication.translate("mapManager", "Spawn Position"))

        self.retranslateUi(mapManager)
        QtCore.QMetaObject.connectSlotsByName(mapManager)

    def retranslateUi(self, mapManager):
        _translate = QtCore.QCoreApplication.translate
        mapManager.setWindowTitle(_translate("mapManager", "Maplestory Manager - Map"))
        self.idMap.setPlaceholderText(_translate("mapManager", "Map ID"))
        self.mapName.setPlaceholderText(_translate("mapManager", "Map Name"))
        self.readRadioButton.setText(_translate("mapManager", "View Map"))
        self.createRadioButton.setText(_translate("mapManager", "Add Map"))
        self.spawnPosition.setPlaceholderText(_translate("mapManager", "Spawn Position"))
        self.okButton.setText(_translate("mapManager", "OK"))
        self.updateRadioButton.setText(_translate("mapManager", "Update Map"))
        self.deleteRadioButton.setText(_translate("mapManager", "Delete Map"))

    def parseInformation(self):
        tempMapID = self.idMap.text()
        tempMapName = self.mapName.text()
        tempSpawn = self.spawnPosition.text()
        action = self.buttonGroup.checkedId()

        if (action == ADD_BUTTON):
            Map.insert(tempMapID, tempMapName, tempSpawn)
        
        elif (action == VIEW_BUTTON):
            if (not tempMapID and not tempMapName and not tempSpawn):
                result = Map.selectAll()
            else:
                result = Map.select(tempMapID)
                result = [result]
            self.output.setRowCount(len(result))
            for i in range(len(result)):
                for j in range(0,3):
                    self.output.setItem(i, j, QtWidgets.QTableWidgetItem(str(result[i][j])))

        elif (action == UPDATE_BUTTON):
            Map.update(tempMapID, tempMapName, tempSpawn)

        elif (action == DELETE_BUTTON):
            Map.delete(tempMapID)

    def alertBox(self):
        msg = QMessageBox()
        msg.setWindowTitle("Bad Request")
        msg.setText("Your request could not be finished.                         ")
        msg.setInformativeText("Error 101: Given type for mapId isn't compatible.\n\nCheck the details section for the complete error message.")
        msg.setDetailedText("Error sql here")
        msg.setIcon(QMessageBox.Critical)

        x = msg.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mapManager = QtWidgets.QWidget()
    ui = Ui_mapManager()
    ui.setupUi(mapManager)
    mapManager.show()
    sys.exit(app.exec_())
