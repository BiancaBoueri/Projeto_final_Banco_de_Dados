from PyQt5.QtWidgets import QMessageBox

def AlertBox(errorMessage):
    msg = QMessageBox()
    msg.setWindowTitle("Bad Request")
    msg.setText("Your request could not be finished.                         ")
    msg.setInformativeText("Check the details section for the complete error message.")
    msg.setDetailedText(str(errorMessage))
    msg.setIcon(QMessageBox.Critical)
    exit = msg.exec_()