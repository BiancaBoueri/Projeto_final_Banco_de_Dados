from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(720,450,300,300)
    win.setWindowTitle("Hello, World!")

    label = QtWidgets.QLabel(win)
    label.setText("It works!")
    label.move(100,100)

    win.show()
    sys.exit(app.exec_())

window()