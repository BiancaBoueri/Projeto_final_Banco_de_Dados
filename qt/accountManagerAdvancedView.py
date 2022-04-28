# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'accountManagerAdvancedView.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio.windows_events import NULL
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
import Account
import io
from PIL import Image, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

grey_background = "background-color: rgb(245, 245, 245);"
white_background = "background-color: rgb(255, 255, 255);"

class Ui_accountManagerAdvancedView(object):
    def setupUi(self, accountManagerAdvancedView):
        accountManagerAdvancedView.setObjectName("accountManagerAdvancedView")
        accountManagerAdvancedView.resize(893, 428)
        accountManagerAdvancedView.setMinimumSize(QSize(893, 428))
        accountManagerAdvancedView.setMaximumSize(QSize(893, 428))
        icon = QIcon()
        icon.addFile(u"images\maplestoryIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        accountManagerAdvancedView.setWindowIcon(icon)
        accountManagerAdvancedView.setStyleSheet(white_background)

        self.output = QtWidgets.QListWidget(accountManagerAdvancedView)
        self.output.setGeometry(QtCore.QRect(320, 20, 551, 391))
        self.output.setObjectName("output")

        self.usernameCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.usernameCheckbox.setGeometry(QtCore.QRect(20, 20, 70, 17))
        self.usernameCheckbox.setObjectName("usernameCheckbox")

        self.creationDateCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.creationDateCheckbox.setGeometry(QtCore.QRect(20, 80, 91, 17))
        self.creationDateCheckbox.setObjectName("creationDateCheckbox")

        self.localizationCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.localizationCheckbox.setGeometry(QtCore.QRect(20, 110, 81, 17))
        self.localizationCheckbox.setObjectName("localizationCheckbox")

        self.preferredLanguageCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.preferredLanguageCheckbox.setGeometry(QtCore.QRect(20, 140, 70, 17))
        self.preferredLanguageCheckbox.setObjectName("preferredLanguageCheckbox")

        self.pinCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.pinCheckbox.setGeometry(QtCore.QRect(20, 170, 70, 17))
        self.pinCheckbox.setObjectName("pinCheckbox")

        self.profilePictureCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.profilePictureCheckbox.setGeometry(QtCore.QRect(20, 200, 91, 17))
        self.profilePictureCheckbox.setObjectName("profilePictureCheckbox")

        self.passwordCheckbox = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.passwordCheckbox.setGeometry(QtCore.QRect(20, 50, 70, 17))
        self.passwordCheckbox.setObjectName("passwordCheckbox")

        self.inputFirstConditional = QtWidgets.QComboBox(accountManagerAdvancedView)
        self.inputFirstConditional.setGeometry(QtCore.QRect(20, 250, 81, 22))
        self.inputFirstConditional.setStyleSheet(grey_background)
        self.inputFirstConditional.setObjectName("inputFirstConditional")
        self.inputFirstConditional.addItem("")
        self.inputFirstConditional.setItemText(0, "")
        self.inputFirstConditional.addItem("")
        self.inputFirstConditional.addItem("")
        self.inputFirstConditional.addItem("")
        self.inputFirstConditional.addItem("")

        self.andFirst = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.andFirst.setGeometry(QtCore.QRect(20, 290, 41, 17))
        self.andFirst.setObjectName("andFirst")

        self.orFirst = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.orFirst.setGeometry(QtCore.QRect(70, 290, 41, 17))
        self.orFirst.setObjectName("orFirst")

        self.firstButtonGroup = QtWidgets.QButtonGroup()
        self.firstButtonGroup.addButton(self.andFirst)
        self.firstButtonGroup.addButton(self.orFirst)

        self.inputSecondConditional = QtWidgets.QComboBox(accountManagerAdvancedView)
        self.inputSecondConditional.setGeometry(QtCore.QRect(20, 320, 81, 22))
        self.inputSecondConditional.setStyleSheet(grey_background)
        self.inputSecondConditional.setObjectName("inputSecondConditional")
        self.inputSecondConditional.addItem("")
        self.inputSecondConditional.setItemText(0, "")
        self.inputSecondConditional.addItem("")
        self.inputSecondConditional.addItem("")
        self.inputSecondConditional.addItem("")
        self.inputSecondConditional.addItem("")

        self.orSecond = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.orSecond.setGeometry(QtCore.QRect(70, 360, 41, 17))
        self.orSecond.setObjectName("orSecond")

        self.andSecond = QtWidgets.QCheckBox(accountManagerAdvancedView)
        self.andSecond.setGeometry(QtCore.QRect(20, 360, 41, 17))
        self.andSecond.setObjectName("andSecond")

        self.secondButtonGroup = QtWidgets.QButtonGroup()
        self.secondButtonGroup.addButton(self.andSecond)
        self.secondButtonGroup.addButton(self.orSecond)

        self.inputThirdConditional = QtWidgets.QComboBox(accountManagerAdvancedView)
        self.inputThirdConditional.setGeometry(QtCore.QRect(20, 390, 81, 22))
        self.inputThirdConditional.setStyleSheet(grey_background)
        self.inputThirdConditional.setObjectName("inputThirdConditional")
        self.inputThirdConditional.addItem("")
        self.inputThirdConditional.setItemText(0, "")
        self.inputThirdConditional.addItem("")
        self.inputThirdConditional.addItem("")
        self.inputThirdConditional.addItem("")
        self.inputThirdConditional.addItem("")

        self.conditionFirstConditional = QtWidgets.QComboBox(accountManagerAdvancedView)
        self.conditionFirstConditional.setGeometry(QtCore.QRect(120, 250, 41, 22))
        self.conditionFirstConditional.setStyleSheet(grey_background)
        self.conditionFirstConditional.setObjectName("conditionFirstConditional")
        self.conditionFirstConditional.addItem("")
        self.conditionFirstConditional.addItem("")
        self.conditionFirstConditional.addItem("")
        self.conditionFirstConditional.addItem("")
        self.conditionFirstConditional.addItem("")
        self.conditionFirstConditional.addItem("")

        self.conditionSecondConditional = QtWidgets.QComboBox(accountManagerAdvancedView)
        self.conditionSecondConditional.setGeometry(QtCore.QRect(120, 320, 41, 22))
        self.conditionSecondConditional.setStyleSheet(grey_background)
        self.conditionSecondConditional.setObjectName("conditionSecondConditional")
        self.conditionSecondConditional.addItem("")
        self.conditionSecondConditional.addItem("")
        self.conditionSecondConditional.addItem("")
        self.conditionSecondConditional.addItem("")
        self.conditionSecondConditional.addItem("")
        self.conditionSecondConditional.addItem("")

        self.conditionThirdConditional = QtWidgets.QComboBox(accountManagerAdvancedView)
        self.conditionThirdConditional.setGeometry(QtCore.QRect(120, 390, 41, 22))
        self.conditionThirdConditional.setStyleSheet(grey_background)
        self.conditionThirdConditional.setObjectName("conditionThirdConditional")
        self.conditionThirdConditional.addItem("")
        self.conditionThirdConditional.addItem("")
        self.conditionThirdConditional.addItem("")
        self.conditionThirdConditional.addItem("")
        self.conditionThirdConditional.addItem("")
        self.conditionThirdConditional.addItem("")

        self.outputFirstConditional = QtWidgets.QLineEdit(accountManagerAdvancedView)
        self.outputFirstConditional.setGeometry(QtCore.QRect(180, 250, 113, 20))
        self.outputFirstConditional.setStyleSheet("")
        self.outputFirstConditional.setObjectName("outputFirstConditional")

        self.outputSecondConditional = QtWidgets.QLineEdit(accountManagerAdvancedView)
        self.outputSecondConditional.setGeometry(QtCore.QRect(180, 320, 113, 20))
        self.outputSecondConditional.setStyleSheet("")
        self.outputSecondConditional.setObjectName("outputSecondConditional")

        self.outputThirdConditional = QtWidgets.QLineEdit(accountManagerAdvancedView)
        self.outputThirdConditional.setGeometry(QtCore.QRect(180, 390, 113, 20))
        self.outputThirdConditional.setStyleSheet("")
        self.outputThirdConditional.setObjectName("outputThirdConditional")

        self.profilePictureView = QtWidgets.QLabel(accountManagerAdvancedView)
        self.profilePictureView.setGeometry(QtCore.QRect(160, 20, 131, 131))
        self.profilePictureView.setText("")
        self.profilePictureView.setObjectName("profilePictureView")

        self.searchButton = QtWidgets.QPushButton(accountManagerAdvancedView)
        self.searchButton.setGeometry(QtCore.QRect(160, 180, 131, 41))
        self.searchButton.setStyleSheet(grey_background)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(lambda: self.teste())

        self.retranslateUi(accountManagerAdvancedView)
        QtCore.QMetaObject.connectSlotsByName(accountManagerAdvancedView)

    def teste(self):
        #Account.update("leevanf",NULL,"./images/avatar2.png",NULL,NULL,NULL)
        image = Account.select(self.outputFirstConditional.text())[2]
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image)
        pixmap =  pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        self.profilePictureView.setPixmap(pixmap)

    def retranslateUi(self, accountManagerAdvancedView):
        _translate = QtCore.QCoreApplication.translate
        accountManagerAdvancedView.setWindowTitle(_translate("accountManagerAdvancedView", "Maplestory Manager - View Account (Advanced)"))
        self.usernameCheckbox.setText(_translate("accountManagerAdvancedView", "Username"))
        self.creationDateCheckbox.setText(_translate("accountManagerAdvancedView", "Creation Date"))
        self.localizationCheckbox.setText(_translate("accountManagerAdvancedView", "Localization"))
        self.preferredLanguageCheckbox.setText(_translate("accountManagerAdvancedView", "Language"))
        self.pinCheckbox.setText(_translate("accountManagerAdvancedView", "PIN"))
        self.profilePictureCheckbox.setText(_translate("accountManagerAdvancedView", "Profile Picture"))
        self.passwordCheckbox.setText(_translate("accountManagerAdvancedView", "Password"))
        self.inputFirstConditional.setItemText(1, _translate("accountManagerAdvancedView", "Username"))
        self.inputFirstConditional.setItemText(2, _translate("accountManagerAdvancedView", "Creation Date"))
        self.inputFirstConditional.setItemText(3, _translate("accountManagerAdvancedView", "Localization"))
        self.inputFirstConditional.setItemText(4, _translate("accountManagerAdvancedView", "Language"))
        self.andFirst.setText(_translate("accountManagerAdvancedView", "AND"))
        self.orFirst.setText(_translate("accountManagerAdvancedView", "OR"))
        self.inputSecondConditional.setItemText(1, _translate("accountManagerAdvancedView", "Username"))
        self.inputSecondConditional.setItemText(2, _translate("accountManagerAdvancedView", "Creation Date"))
        self.inputSecondConditional.setItemText(3, _translate("accountManagerAdvancedView", "Localization"))
        self.inputSecondConditional.setItemText(4, _translate("accountManagerAdvancedView", "Language"))
        self.orSecond.setText(_translate("accountManagerAdvancedView", "OR"))
        self.andSecond.setText(_translate("accountManagerAdvancedView", "AND"))
        self.inputThirdConditional.setItemText(1, _translate("accountManagerAdvancedView", "Username"))
        self.inputThirdConditional.setItemText(2, _translate("accountManagerAdvancedView", "Creation Date"))
        self.inputThirdConditional.setItemText(3, _translate("accountManagerAdvancedView", "Localization"))
        self.inputThirdConditional.setItemText(4, _translate("accountManagerAdvancedView", "Language"))
        self.conditionFirstConditional.setItemText(0, _translate("accountManagerAdvancedView", "="))
        self.conditionFirstConditional.setItemText(1, _translate("accountManagerAdvancedView", "!="))
        self.conditionFirstConditional.setItemText(2, _translate("accountManagerAdvancedView", ">"))
        self.conditionFirstConditional.setItemText(3, _translate("accountManagerAdvancedView", ">="))
        self.conditionFirstConditional.setItemText(4, _translate("accountManagerAdvancedView", "<"))
        self.conditionFirstConditional.setItemText(5, _translate("accountManagerAdvancedView", "<="))
        self.conditionSecondConditional.setItemText(0, _translate("accountManagerAdvancedView", "="))
        self.conditionSecondConditional.setItemText(1, _translate("accountManagerAdvancedView", "!="))
        self.conditionSecondConditional.setItemText(2, _translate("accountManagerAdvancedView", ">"))
        self.conditionSecondConditional.setItemText(3, _translate("accountManagerAdvancedView", ">="))
        self.conditionSecondConditional.setItemText(4, _translate("accountManagerAdvancedView", "<"))
        self.conditionSecondConditional.setItemText(5, _translate("accountManagerAdvancedView", "<="))
        self.conditionThirdConditional.setItemText(0, _translate("accountManagerAdvancedView", "="))
        self.conditionThirdConditional.setItemText(1, _translate("accountManagerAdvancedView", "!="))
        self.conditionThirdConditional.setItemText(2, _translate("accountManagerAdvancedView", ">"))
        self.conditionThirdConditional.setItemText(3, _translate("accountManagerAdvancedView", ">="))
        self.conditionThirdConditional.setItemText(4, _translate("accountManagerAdvancedView", "<"))
        self.conditionThirdConditional.setItemText(5, _translate("accountManagerAdvancedView", "<="))
        self.searchButton.setText(_translate("accountManagerAdvancedView", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    accountManagerAdvancedView = QtWidgets.QWidget()
    ui = Ui_accountManagerAdvancedView()
    ui.setupUi(accountManagerAdvancedView)
    accountManagerAdvancedView.show()
    sys.exit(app.exec_())
