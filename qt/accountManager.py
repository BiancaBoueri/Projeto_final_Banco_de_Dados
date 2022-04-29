# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from accountManagerAdvancedView import Ui_accountManagerAdvancedView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import Account

grey_background = "background-color: rgb(245, 245, 245);"
white_background = "background-color: rgb(255, 255, 255);"

ADD_BUTTON = -2
VIEW_BUTTON = -3
UPDATE_BUTTON = -4
DELETE_BUTTON = -5

class Ui_accountManager(object):
    def setupUi(self, accountManager):

        accountManager.setObjectName("accountManager")
        accountManager.setMinimumSize(QtCore.QSize(434, 340))
        accountManager.setMaximumSize(QtCore.QSize(434, 340))
        icon = QIcon()
        icon.addFile(u"images\maplestoryIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        accountManager.setWindowIcon(icon)
        accountManager.setStyleSheet(white_background)

        self.createRadioButton = QtWidgets.QRadioButton(accountManager)
        self.createRadioButton.setGeometry(QtCore.QRect(20, 20, 81, 17))
        self.createRadioButton.setObjectName("createRadioButton")

        self.readRadioButton = QtWidgets.QRadioButton(accountManager)
        self.readRadioButton.setGeometry(QtCore.QRect(120, 20, 91, 17))
        self.readRadioButton.setObjectName("readRadioButton")

        self.updateRadioButton = QtWidgets.QRadioButton(accountManager)
        self.updateRadioButton.setGeometry(QtCore.QRect(220, 20, 101, 17))
        self.updateRadioButton.setObjectName("updateRadioButton")

        self.deleteRadioButton = QtWidgets.QRadioButton(accountManager)
        self.deleteRadioButton.setGeometry(QtCore.QRect(330, 20, 101, 17))
        self.deleteRadioButton.setObjectName("deleteRadioButton")

        self.username = QtWidgets.QLineEdit(accountManager)
        self.username.setGeometry(QtCore.QRect(20, 60, 113, 20))
        self.username.setText("")
        self.username.setObjectName("username")

        self.password = QtWidgets.QLineEdit(accountManager)
        self.password.setGeometry(QtCore.QRect(20, 100, 113, 20))
        self.password.setText("")
        self.password.setObjectName("password")

        self.profilePicture = QtWidgets.QLineEdit(accountManager)
        self.profilePicture.setGeometry(QtCore.QRect(20, 140, 113, 20))
        self.profilePicture.setText("")
        self.profilePicture.setObjectName("profilePicture")

        self.localization = QtWidgets.QLineEdit(accountManager)
        self.localization.setGeometry(QtCore.QRect(20, 180, 113, 20))
        self.localization.setText("")
        self.localization.setObjectName("localization")

        self.preferredLanguage = QtWidgets.QLineEdit(accountManager)
        self.preferredLanguage.setGeometry(QtCore.QRect(20, 220, 113, 20))
        self.preferredLanguage.setText("")
        self.preferredLanguage.setObjectName("preferredLanguage")

        self.pin = QtWidgets.QLineEdit(accountManager)
        self.pin.setGeometry(QtCore.QRect(20, 260, 113, 20))
        self.pin.setText("")
        self.pin.setObjectName("pin")

        self.output = QtWidgets.QTableWidget(accountManager)
        self.output.setGeometry(QtCore.QRect(160, 60, 256, 221))
        self.output.setObjectName("output")
        self.output.setColumnCount(6)

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

        column1 = self.output.horizontalHeaderItem(0)
        column1.setText(QtCore.QCoreApplication.translate("accountManager", "Username"))
        column2 = self.output.horizontalHeaderItem(1)
        column2.setText(QtCore.QCoreApplication.translate("accountManager", "Password"))
        column3 = self.output.horizontalHeaderItem(2)
        column3.setText(QtCore.QCoreApplication.translate("accountManager", "Creation Date"))
        column4 = self.output.horizontalHeaderItem(3)
        column4.setText(QtCore.QCoreApplication.translate("accountManager", "Localization"))
        column5 = self.output.horizontalHeaderItem(4)
        column5.setText(QtCore.QCoreApplication.translate("accountManager", "Language"))
        column6 = self.output.horizontalHeaderItem(5)
        column6.setText(QtCore.QCoreApplication.translate("accountManager", "PIN"))

        self.advancedViewButton = QtWidgets.QPushButton(accountManager)
        self.advancedViewButton.setGeometry(QtCore.QRect(304, 300, 111, 31))
        self.advancedViewButton.setStyleSheet(grey_background)
        self.advancedViewButton.setObjectName("advancedViewButton")
        self.advancedViewButton.clicked.connect(self.callAdvancedView)

        self.buttonGroup = QtWidgets.QButtonGroup()
        self.buttonGroup.addButton(self.createRadioButton)
        self.buttonGroup.addButton(self.readRadioButton)
        self.buttonGroup.addButton(self.updateRadioButton)
        self.buttonGroup.addButton(self.deleteRadioButton)

        self.okButton = QtWidgets.QPushButton(accountManager)
        self.okButton.setObjectName("okButton")
        self.okButton.setGeometry(QtCore.QRect(20, 300, 111, 31))
        self.okButton.setStyleSheet(grey_background)
        self.okButton.clicked.connect(lambda: self.parseInformation())

        self.retranslateUi(accountManager)
        QtCore.QMetaObject.connectSlotsByName(accountManager)

    def retranslateUi(self, accountManager):
        _translate = QtCore.QCoreApplication.translate
        accountManager.setWindowTitle(_translate("accountManager", "Maplestory Manager - Account"))
        self.createRadioButton.setText(_translate("accountManager", "Add Account"))
        self.readRadioButton.setText(_translate("accountManager", "View Account"))
        self.updateRadioButton.setText(_translate("accountManager", "Update Account"))
        self.deleteRadioButton.setText(_translate("accountManager", "Delete Account"))
        self.username.setPlaceholderText(_translate("accountManager", "Username"))
        self.password.setPlaceholderText(_translate("accountManager", "Password"))
        self.profilePicture.setPlaceholderText(_translate("accountManager", "Profile Picture (PATH)"))
        self.localization.setPlaceholderText(_translate("accountManager", "Localization"))
        self.preferredLanguage.setPlaceholderText(_translate("accountManager", "Language"))
        self.pin.setPlaceholderText(_translate("accountManager", "PIN"))
        self.advancedViewButton.setText(_translate("accountManager", "Advanced View..."))
        self.okButton.setText(_translate("accountManager", "OK"))

    def callAdvancedView(self):
        self.accountManagerAdvancedViewWindow = QtWidgets.QWidget()
        self.ui = Ui_accountManagerAdvancedView()
        self.ui.setupUi(self.accountManagerAdvancedViewWindow)
        self.accountManagerAdvancedViewWindow.show()

    def parseInformation(self):
        tempUsername = self.username.text()
        tempPassword = self.password.text()
        tempProfilePicturePath = self.profilePicture.text()
        tempLocalization = self.localization.text()
        tempLanguage = self.preferredLanguage.text()
        tempPIN = self.pin.text()
        action = self.buttonGroup.checkedId()

        if (action == ADD_BUTTON):
            Account.insert(tempUsername, tempPassword, tempProfilePicturePath, tempLocalization, tempLanguage, tempPIN)
        
        elif (action == VIEW_BUTTON):
            if (not tempUsername):
                result = Account.selectAll()
            else:
                result = Account.select(tempUsername)
                result = [result]
            self.output.setRowCount(len(result))
            for i in range(len(result)):
                self.output.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
                self.output.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
                self.output.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][3])))
                self.output.setItem(i, 3, QtWidgets.QTableWidgetItem(str(result[i][4])))
                self.output.setItem(i, 4, QtWidgets.QTableWidgetItem(str(result[i][5])))
                self.output.setItem(i, 5, QtWidgets.QTableWidgetItem(str(result[i][6])))

        elif (action == UPDATE_BUTTON):
            Account.update(tempUsername, tempPassword, tempProfilePicturePath, tempLocalization, tempLanguage, tempPIN)

        elif (action == DELETE_BUTTON):
            Account.delete(tempUsername)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    accountManager = QtWidgets.QWidget()
    ui = Ui_accountManager()
    ui.setupUi(accountManager)
    accountManager.show()
    sys.exit(app.exec_())
