# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storeManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import sys
import inspect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from storeTransactionManager import Ui_transactionManager
import Store

grey_background = "background-color: rgb(245, 245, 245);"
white_background = "background-color: rgb(255, 255, 255);"

class Ui_storeManager(object):
    def setupUi(self, storeManager):
        storeManager.setObjectName("storeManager")
        storeManager.resize(428, 306)
        storeManager.setMinimumSize(QtCore.QSize(428, 306))
        storeManager.setMaximumSize(QtCore.QSize(428, 306))
        icon = QIcon()
        icon.addFile(u"images\maplestoryIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        storeManager.setWindowIcon(icon)
        storeManager.setStyleSheet(white_background)

        self.idItem = QtWidgets.QLineEdit(storeManager)
        self.idItem.setGeometry(QtCore.QRect(10, 40, 121, 20))
        self.idItem.setText("")
        self.idItem.setObjectName("idItem")

        self.value = QtWidgets.QLineEdit(storeManager)
        self.value.setGeometry(QtCore.QRect(10, 80, 121, 20))
        self.value.setText("")
        self.value.setObjectName("value")

        self.createRadioButton = QtWidgets.QRadioButton(storeManager)
        self.createRadioButton.setGeometry(QtCore.QRect(10, 10, 81, 17))
        self.createRadioButton.setObjectName("createRadioButton")

        self.readRadioButton = QtWidgets.QRadioButton(storeManager)
        self.readRadioButton.setGeometry(QtCore.QRect(110, 10, 81, 17))
        self.readRadioButton.setObjectName("readRadioButton")

        self.updateRadioButton = QtWidgets.QRadioButton(storeManager)
        self.updateRadioButton.setGeometry(QtCore.QRect(210, 10, 101, 17))
        self.updateRadioButton.setObjectName("updateRadioButton")

        self.deleteRadioButton = QtWidgets.QRadioButton(storeManager)
        self.deleteRadioButton.setGeometry(QtCore.QRect(320, 10, 101, 17))
        self.deleteRadioButton.setObjectName("deleteRadioButton")

        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.addButton(self.createRadioButton)
        self.buttonGroup.addButton(self.readRadioButton)
        self.buttonGroup.addButton(self.updateRadioButton)
        self.buttonGroup.addButton(self.deleteRadioButton)

        self.stock = QtWidgets.QLineEdit(storeManager)
        self.stock.setGeometry(QtCore.QRect(10, 120, 121, 20))
        self.stock.setText("")
        self.stock.setObjectName("stock")

        self.okButton = QtWidgets.QPushButton(storeManager)
        self.okButton.setGeometry(QtCore.QRect(10, 160, 121, 31))
        self.okButton.setStyleSheet(grey_background)
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(lambda: self.parseInformation())

        self.output = QtWidgets.QTableWidget(storeManager)
        self.output.setGeometry(QtCore.QRect(150, 40, 261, 251))
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
        column1.setText(QtCore.QCoreApplication.translate("accountManagerAdvancedView", "idItem"))
        column2 = self.output.horizontalHeaderItem(1)
        column2.setText(QtCore.QCoreApplication.translate("accountManagerAdvancedView", "value"))
        column3 = self.output.horizontalHeaderItem(2)
        column3.setText(QtCore.QCoreApplication.translate("accountManagerAdvancedView", "stock"))

        self.simulateButton = QtWidgets.QPushButton(storeManager)
        self.simulateButton.setGeometry(QtCore.QRect(10, 210, 121, 31))
        self.simulateButton.setStyleSheet(grey_background)
        self.simulateButton.setObjectName("simulateButton")
        self.simulateButton.clicked.connect(lambda: self.callStoreTransaction())

        self.retranslateUi(storeManager)
        QtCore.QMetaObject.connectSlotsByName(storeManager)

    def retranslateUi(self, storeManager):
        _translate = QtCore.QCoreApplication.translate
        storeManager.setWindowTitle(_translate("storeManager", "Maplestory Manager - Store"))
        self.idItem.setPlaceholderText(_translate("storeManager", "Item ID"))
        self.value.setPlaceholderText(_translate("storeManager", "Value"))
        self.updateRadioButton.setText(_translate("storeManager", "Update Product"))
        self.createRadioButton.setText(_translate("storeManager", "Add Product"))
        self.deleteRadioButton.setText(_translate("storeManager", "Delete Product"))
        self.stock.setPlaceholderText(_translate("storeManager", "Stock"))
        self.okButton.setText(_translate("storeManager", "OK"))
        self.readRadioButton.setText(_translate("storeManager", "View Product"))
        self.simulateButton.setText(_translate("storeManager", "Shop Transaction..."))

    def callStoreTransaction(self):
        self.storeTransactionWindow = QtWidgets.QWidget()
        self.ui = Ui_transactionManager()
        self.ui.setupUi(self.storeTransactionWindow)
        self.storeTransactionWindow.show()

    def parseInformation(self):
        tempItemID = self.idItem.text()
        tempValue = self.value.text()
        tempStock = self.stock.text()
        action = self.buttonGroup.checkedId()

        if (action == -2):
            Store.insert(tempItemID, tempValue, tempStock)

        elif (action == -3):
            if (not tempItemID and not tempValue and not tempStock):
                result = Store.selectAll()
            else:
                result = Store.select(tempItemID)
                result = [result]
            self.output.setRowCount(len(result))
            for i in range(len(result)):
                self.output.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
                self.output.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
                self.output.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))

        elif (action == -4):
            Store.update(tempItemID, tempValue, tempStock)

        elif (action == -5):
            Store.delete(tempItemID)

        else:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    storeManager = QtWidgets.QWidget()
    ui = Ui_storeManager()
    ui.setupUi(storeManager)
    storeManager.show()
    sys.exit(app.exec_())
