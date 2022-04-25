# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2stepCode.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from stockboughtgui import Ui_MainWindow


class Ui_Dialog(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 100)
        Dialog.setStyleSheet("background-color: rgb(129, 146, 165);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 251, 16))
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(82, 40, 211, 21))
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"font-size: 14pt; color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        #function call to openWindow on button press.
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked = lambda: self.openWindow())
        self.pushButton.setGeometry(QtCore.QRect(130, 70, 101, 21))
        self.pushButton.setStyleSheet("background-color: rgb(0, 0, 0); color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please Enter Two Step Varification Code:"))
        self.pushButton.setText(_translate("Dialog", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
