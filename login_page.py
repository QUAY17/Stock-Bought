

from PyQt5 import QtCore, QtGui, QtWidgets
from step_code_var import Ui_Dialog
from stockboughtgui import Ui_MainWindow
import robin_stocks_functions as rsf
import stockboughtgui as sbg

#import robin_stocks as robin
#import robin_stocks.urls as urls
#import robin_stocks.helper as helper
#import robin_stocks.authentication as authentication



class Ui_LoginWindow(object):

    #def openWindow(self):
    #   email = self.lineEdit_email.text()
#    password = self.lineEdit_pswd.text()
 #       rsf.login(email, password)

  #      self.window = QtWidgets.QDialog()
   #     self.ui = Ui_Dialog()
    #   self.window.show()

    def openWindow(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_pswd.text()
        rsf.login(email, password)

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setEnabled(True)
        LoginWindow.resize(1057, 805)
        LoginWindow.setStyleSheet("background-color: #ffffff")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background_color = QtWidgets.QLabel(self.centralwidget)
        self.background_color.setGeometry(QtCore.QRect(0, 0, 1058, 753))
        self.background_color.setAutoFillBackground(False)
        self.background_color.setText("")
        self.background_color.setPixmap(QtGui.QPixmap("background.png"))
        self.background_color.setScaledContents(True)
        self.background_color.setObjectName("background_color")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(250, 110, 531, 181))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label_email_background = QtWidgets.QLabel(self.centralwidget)
        self.label_email_background.setGeometry(QtCore.QRect(260, 325, 511, 51))
        self.label_email_background.setStyleSheet("background-color:  rgb(129, 146, 165);")
        self.label_email_background.setText("")
        self.label_email_background.setScaledContents(False)
        self.label_email_background.setObjectName("label_email_background")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(290, 335, 111, 31))
        self.label_email.setMouseTracking(False)
        self.label_email.setAutoFillBackground(False)
        self.label_email.setStyleSheet("font-size: 15pt; color: rgb(0, 0, 0);\n"
"background-color:  rgb(129, 146, 165);")
        self.label_email.setWordWrap(False)
        self.label_email.setObjectName("label_email")
        self.label_pswd_background = QtWidgets.QLabel(self.centralwidget)
        self.label_pswd_background.setGeometry(QtCore.QRect(260, 400, 511, 51))
        self.label_pswd_background.setStyleSheet("background-color:  rgb(129, 146, 165);")
        self.label_pswd_background.setText("")
        self.label_pswd_background.setScaledContents(False)
        self.label_pswd_background.setObjectName("label_pswd_background")
        self.label_pswd = QtWidgets.QLabel(self.centralwidget)
        self.label_pswd.setGeometry(QtCore.QRect(290, 410, 111, 31))
        self.label_pswd.setAutoFillBackground(False)
        self.label_pswd.setStyleSheet("font-size: 15pt; color: rgb(0, 0, 0);\n"
"background-color:  rgb(129, 146, 165);")
        self.label_pswd.setScaledContents(False)
        self.label_pswd.setWordWrap(False)
        self.label_pswd.setObjectName("label_pswd")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(340, 340, 391, 21))
        self.lineEdit_email.setStyleSheet("font-size: 14pt; color: rgb(0, 0, 0);")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_pswd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_pswd.setGeometry(QtCore.QRect(370, 415, 361, 21))
        self.lineEdit_pswd.setStyleSheet("font-size: 14pt; color: rgb(0, 0, 0);")
        self.lineEdit_pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_pswd.setObjectName("lineEdit_pswd")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(430, 480, 181, 41))
        self.login_button.setStyleSheet("font-size: 15pt; color: rgb(0, 0, 0); \n"
"background-color:  rgb(129, 146, 165);")
        self.login_button.clicked.connect(self.openWindow())
        self.login_button.setObjectName("login_button")

        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(415, 455, 271, 20))
        self.error_label.setAutoFillBackground(False)
        self.error_label.setStyleSheet("font-size: 11pt; color: rgb(252, 0, 7);\n"
                                      "background-color:  rgb(34, 37, 40);")
        self.error_label.setScaledContents(False)
        self.error_label.setWordWrap(False)
        self.error_label.setObjectName("error_label")

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1057, 24))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    #def loginFunction(self):
    #    email = self.lineEdit_email.text()
    #    password = self.lineEdit_pswd.text()

    #    if len(email) == 0 or len(password) == 0:
     #       self.error_label.setText("Please enter your login and password")

    #    else:
     #       rsf.login(email, password)
            #self.openWindow()
            #self.step_var_popup()


        #rsf.login(email, password)

    #def step_var_popup(self):
     #   QMessageBox.setObjectName("QMsgBox")
      #  QMessageBox.resize(378, 109)
       # QMessageBox.setStyleSheet("background-color: rgb(34, 37, 40);")
      #  self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
      #  self.buttonBox.setGeometry(QtCore.QRect(90, 70, 171, 32))
      #  self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
      #  self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
      #  self.buttonBox.setObjectName("buttonBox")
      #  self.label = QtWidgets.QLabel(QMessageBox)
      #  self.label.setGeometry(QtCore.QRect(70, 10, 251, 16))
      #  self.label.setObjectName("label")
      #  self.lineEdit = QtWidgets.QLineEdit(QMessageBox)
      #  self.lineEdit.setGeometry(QtCore.QRect(82, 40, 211, 21))
      #  self.lineEdit.setStyleSheet("background-color: rgb(129, 146, 165);\n"
       #                                 "font-size: 14pt; color: rgb(0, 0, 0);")
      #  self.lineEdit.setObjectName("lineEdit")

      #  self.retranslateUi(QMessageBox)
      #  self.buttonBox.accepted.connect(QMessageBox.accept)
      #  self.buttonBox.rejected.connect(QMessageBox.reject)
      #  QtCore.QMetaObject.connectSlotsByName(QMessageBox)



    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.label_email.setText(_translate("LoginWindow", "Email:"))
        self.label_pswd.setText(_translate("LoginWindow", "Password:"))
        self.login_button.setText(_translate("LoginWindow", "Sign In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
