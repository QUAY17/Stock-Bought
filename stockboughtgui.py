# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stockboughtgui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import numpy as np


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 783)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1058, 16777215))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gather_MED = QtWidgets.QPushButton(self.centralwidget)
        self.gather_MED.setGeometry(QtCore.QRect(10, 310, 351, 61))
        self.gather_MED.setAutoFillBackground(False)
        self.gather_MED.setObjectName("gather_MED")
        self.gather_FAD = QtWidgets.QPushButton(self.centralwidget)
        self.gather_FAD.setGeometry(QtCore.QRect(10, 230, 351, 61))
        self.gather_FAD.setObjectName("gather_FAD")
        self.gather_FAD.clicked.connect(self.fundamentalcliked)
        self.gather_MED.clicked.connect(self.macrocliked)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(370, -10, 20, 761))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-40, 0, 421, 131))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setObjectName("logo")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-20, 0, 1141, 761))
        self.background.setMouseTracking(False)
        self.background.setAutoFillBackground(False)
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.backtesting_background = QtWidgets.QLabel(self.centralwidget)
        self.backtesting_background.setGeometry(QtCore.QRect(0, 410, 381, 351))
        self.backtesting_background.setText("")
        self.backtesting_background.setPixmap(QtGui.QPixmap("backtestingbg.png"))
        self.backtesting_background.setScaledContents(True)
        self.backtesting_background.setObjectName("backtesting_background")
        self.label_backtesting = QtWidgets.QLabel(self.centralwidget)
        self.label_backtesting.setGeometry(QtCore.QRect(10, 420, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_backtesting.setFont(font)
        self.label_backtesting.setObjectName("label_backtesting")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 460, 381, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_begindate = QtWidgets.QLabel(self.centralwidget)
        self.label_begindate.setGeometry(QtCore.QRect(10, 490, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_begindate.setFont(font)
        self.label_begindate.setObjectName("label_begindate")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 520, 381, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_enddate = QtWidgets.QLabel(self.centralwidget)
        self.label_enddate.setGeometry(QtCore.QRect(10, 540, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_enddate.setFont(font)
        self.label_enddate.setObjectName("label_enddate")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 570, 381, 41))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.search_stock = QtWidgets.QLineEdit(self.centralwidget)
        self.search_stock.setGeometry(QtCore.QRect(10, 170, 351, 31))
        self.search_stock.setObjectName("search_stock")
        self.begin_date = QtWidgets.QLineEdit(self.centralwidget)
        self.begin_date.setGeometry(QtCore.QRect(120, 490, 241, 21))
        self.begin_date.setObjectName("begin_date")
        self.end_date = QtWidgets.QLineEdit(self.centralwidget)
        self.end_date.setGeometry(QtCore.QRect(100, 540, 261, 21))
        self.end_date.setObjectName("end_date")
        self.trading_algo_menu = QtWidgets.QComboBox(self.centralwidget)
        self.trading_algo_menu.setGeometry(QtCore.QRect(180, 620, 191, 25))
        self.trading_algo_menu.setObjectName("trading_algo_menu")
        self.trading_algo_menu.addItem("")
        self.trading_algo_menu.addItem("")
        self.trading_algo_menu.addItem("")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(0, 660, 381, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.trading_algo = QtWidgets.QLabel(self.centralwidget)
        self.trading_algo.setGeometry(QtCore.QRect(10, 620, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.trading_algo.setFont(font)
        self.trading_algo.setObjectName("trading_algo")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 680, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.financial_ad_label = QtWidgets.QLabel(self.centralwidget)
        self.financial_ad_label.setGeometry(QtCore.QRect(390, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.financial_ad_label.setFont(font)
        self.financial_ad_label.setStyleSheet("color = rgb(238, 238, 236)")
        self.financial_ad_label.setObjectName("financial_ad_label")
        self.fad_med = QtWidgets.QFrame(self.centralwidget)
        self.fad_med.setFrameShape(QtWidgets.QFrame.VLine)
        self.fad_med.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.fad_med.setObjectName("fad_med")
        self.label_FAD1 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD1.setGeometry(QtCore.QRect(390, 350, 67, 17))
        self.label_FAD1.setObjectName("label_FAD1")
        self.label_FAD2 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD2.setGeometry(QtCore.QRect(470, 350, 67, 17))
        self.label_FAD2.setObjectName("label_FAD2")
        self.label_FAD3 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD3.setGeometry(QtCore.QRect(390, 380, 67, 17))
        self.label_FAD3.setObjectName("label_FAD3")
        self.label_FAD4 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD4.setGeometry(QtCore.QRect(470, 380, 67, 17))
        self.label_FAD4.setObjectName("label_FAD4")
        self.label_FAD5 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD5.setGeometry(QtCore.QRect(390, 410, 67, 17))
        self.label_FAD5.setObjectName("label_FAD5")
        self.label_FAD6 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD6.setGeometry(QtCore.QRect(470, 410, 67, 17))
        self.label_FAD6.setObjectName("label_FAD6")
        self.label_FAD7 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD7.setGeometry(QtCore.QRect(550, 350, 67, 17))
        self.label_FAD7.setObjectName("label_FAD7")
        self.label_FAD8 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD8.setGeometry(QtCore.QRect(650, 350, 67, 17))
        self.label_FAD8.setObjectName("label_FAD8")
        self.label_FAD9 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD9.setGeometry(QtCore.QRect(550, 380, 91, 17))
        self.label_FAD9.setObjectName("label_FAD9")
        self.label_FAD10 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD10.setGeometry(QtCore.QRect(650, 380, 67, 17))
        self.label_FAD10.setObjectName("label_FAD10")
        self.label_FAD11 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD11.setGeometry(QtCore.QRect(550, 410, 67, 17))
        self.label_FAD11.setObjectName("label_FAD11")
        self.label_FAD12 = QtWidgets.QLabel(self.centralwidget)
        self.label_FAD12.setGeometry(QtCore.QRect(650, 410, 67, 17))
        self.label_FAD12.setObjectName("label_FAD12")
        self.macro_ed_label = QtWidgets.QLabel(self.centralwidget)
        self.macro_ed_label.setGeometry(QtCore.QRect(730, 310, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.macro_ed_label.setFont(font)
        self.macro_ed_label.setStyleSheet("color = rgb(238, 238, 236)")
        self.macro_ed_label.setObjectName("macro_ed_label")
        self.label_MED1 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED1.setGeometry(QtCore.QRect(730, 350, 67, 17))
        self.label_MED1.setObjectName("label_MED1")
        self.label_MED2 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED2.setGeometry(QtCore.QRect(810, 350, 67, 17))
        self.label_MED2.setObjectName("label_MED2")
        self.label_MED3 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED3.setGeometry(QtCore.QRect(730, 380, 67, 17))
        self.label_MED3.setObjectName("label_MED3")
        self.label_MED4 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED4.setGeometry(QtCore.QRect(810, 380, 67, 17))
        self.label_MED4.setObjectName("label_MED4")
        self.label_MED5 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED5.setGeometry(QtCore.QRect(730, 410, 67, 17))
        self.label_MED5.setObjectName("label_MED5")
        self.label_MED6 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED6.setGeometry(QtCore.QRect(810, 410, 67, 17))
        self.label_MED6.setObjectName("label_MED6")
        self.label_MED7 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED7.setGeometry(QtCore.QRect(890, 350, 67, 17))
        self.label_MED7.setObjectName("label_MED7")
        self.label_MED8 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED8.setGeometry(QtCore.QRect(990, 350, 67, 17))
        self.label_MED8.setObjectName("label_MED8")
        self.label_MED9 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED9.setGeometry(QtCore.QRect(890, 380, 91, 17))
        self.label_MED9.setObjectName("label_MED9")
        self.label_MED10 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED10.setGeometry(QtCore.QRect(990, 380, 67, 17))
        self.label_MED10.setObjectName("label_MED10")
        self.label_MED11 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED11.setGeometry(QtCore.QRect(890, 410, 67, 17))
        self.label_MED11.setObjectName("label_MED11")
        self.label_MED12 = QtWidgets.QLabel(self.centralwidget)
        self.label_MED12.setGeometry(QtCore.QRect(990, 410, 67, 17))
        self.label_MED12.setObjectName("label_MED12")
        self.graph = PlotWidget(self.centralwidget)
        self.graph.setObjectName("graph")
        self.stock_name = QtWidgets.QLabel(self.centralwidget)
        self.stock_name.setGeometry(QtCore.QRect(900, 1000, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stock_name.setFont(font)
        self.stock_name.setObjectName("stock_name")
        self.background.raise_()
        self.logo.raise_()
        self.gather_MED.raise_()
        self.gather_FAD.raise_()
        self.line.raise_()
        self.backtesting_background.raise_()
        self.label_backtesting.raise_()
        self.line_2.raise_()
        self.label_begindate.raise_()
        self.line_3.raise_()
        self.label_enddate.raise_()
        self.line_4.raise_()
        self.search_stock.raise_()
        self.begin_date.raise_()
        self.end_date.raise_()
        self.trading_algo_menu.raise_()
        self.line_5.raise_()
        self.trading_algo.raise_()
        self.pushButton.raise_()
        self.financial_ad_label.raise_()
        self.label_FAD1.raise_()
        self.label_FAD2.raise_()
        self.label_FAD3.raise_()
        self.label_FAD4.raise_()
        self.label_FAD5.raise_()
        self.label_FAD6.raise_()
        self.label_FAD7.raise_()
        self.label_FAD8.raise_()
        self.label_FAD9.raise_()
        self.label_FAD10.raise_()
        self.label_FAD11.raise_()
        self.label_FAD12.raise_()
        self.macro_ed_label.raise_()
        self.label_MED1.raise_()
        self.label_MED2.raise_()
        self.label_MED3.raise_()
        self.label_MED4.raise_()
        self.label_MED5.raise_()
        self.label_MED6.raise_()
        self.label_MED7.raise_()
        self.label_MED8.raise_()
        self.label_MED9.raise_()
        self.label_MED10.raise_()
        self.label_MED11.raise_()
        self.label_MED12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.search_stock.returnPressed.connect(lambda:self.name_entered())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stock Bought"))
        self.gather_MED.setText(_translate("MainWindow", "Gather Macro Environment Data"))
        self.gather_FAD.setText(_translate("MainWindow", "Gather Financial Analyst Data"))
        self.label_backtesting.setText(_translate("MainWindow", "Backtesting"))
        self.label_begindate.setText(_translate("MainWindow", "Begin Date:"))
        self.label_enddate.setText(_translate("MainWindow", "End Date:"))
        self.search_stock.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.trading_algo_menu.setItemText(0, _translate("MainWindow", "Alg1"))
        self.trading_algo_menu.setItemText(1, _translate("MainWindow", "Alg2"))
        self.trading_algo_menu.setItemText(2, _translate("MainWindow", "Alg3"))
        self.trading_algo.setText(_translate("MainWindow", "Trading Algorithms:"))
        self.pushButton.setText(_translate("MainWindow", "Backtest"))
    

    def fundamentalcliked(self):
        _translate = QtCore.QCoreApplication.translate
        self.financial_ad_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Finacial Analyst Data</span></p></body></html>"))
        self.label_FAD1.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Open</span></p></body></html>"))
        self.label_FAD2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">238.10</span></p></body></html>"))
        self.label_FAD3.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">High</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>"))
        self.label_FAD4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">774.33</span></p></body></html>"))
        self.label_FAD5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Low</span></p></body></html>"))
        self.label_FAD6.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">300.13</span></p></body></html>"))
        self.label_FAD7.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Volume</span></p></body></html>"))
        self.label_FAD8.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">63.29M</span></p></body></html>"))
        self.label_FAD9.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">AVG Volume</span></p></body></html>"))
        self.label_FAD10.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">68.29M</span></p></body></html>"))
        self.label_FAD11.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MKT Cap</span></p></body></html>"))
        self.label_FAD12.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">47.38M</span></p></body></html>"))
        self.fad_med.setGeometry(QtCore.QRect(700, 310, 20, 131))
        self.fad_med.raise_()
        self.fad_med.show()

    def macrocliked(self):
        _translate = QtCore.QCoreApplication.translate
        self.macro_ed_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Macro Environment Data</span></p></body></html>"))
        self.label_MED1.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Open</span></p></body></html>"))
        self.label_MED2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">238.10</span></p></body></html>"))
        self.label_MED3.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">High</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>"))
        self.label_MED4.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">774.33</span></p></body></html>"))
        self.label_MED5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Low</span></p></body></html>"))
        self.label_MED6.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">300.13</span></p></body></html>"))
        self.label_MED7.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Volume</span></p></body></html>"))
        self.label_MED8.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">63.29M</span></p></body></html>"))
        self.label_MED9.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">AVG Volume</span></p></body></html>"))
        self.label_MED10.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">68.29M</span></p></body></html>"))
        self.label_MED11.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MKT Cap</span></p></body></html>"))
        self.label_MED12.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">47.38M</span></p></body></html>"))
        self.fad_med.setGeometry(QtCore.QRect(700, 310, 20, 131))
        self.fad_med.raise_()
        self.fad_med.show()

    def name_entered(self):
        _translate = QtCore.QCoreApplication.translate
        self.graph.setGeometry(QtCore.QRect(400, 10, 641, 291))
        self.graph.raise_()
        x = np.random.normal(size=1000)
        y = np.random.normal(size=(3,1000))
        for i in range(3):
            self.graph.plot(x,y[i], pen=(i,3))

        self.stock_name.setGeometry(QtCore.QRect(900, 10, 141, 31))
        self.stock_name.raise_()
        self.stock_name.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">" + self.search_stock.text() + "</span></p></body></html>"))
        self.search_stock.clear()
        self.financial_ad_label.setText("")
        self.label_FAD1.setText("")
        self.label_FAD2.setText("")
        self.label_FAD3.setText("")
        self.label_FAD4.setText("")
        self.label_FAD5.setText("")
        self.label_FAD6.setText("")
        self.label_FAD7.setText("")
        self.label_FAD8.setText("")
        self.label_FAD9.setText("")
        self.label_FAD10.setText("")
        self.label_FAD11.setText("")
        self.label_FAD12.setText("")
        self.macro_ed_label.setText("")
        self.label_MED1.setText("")
        self.label_MED2.setText("")
        self.label_MED3.setText("")
        self.label_MED4.setText("")
        self.label_MED5.setText("")
        self.label_MED6.setText("")
        self.label_MED7.setText("")
        self.label_MED8.setText("")
        self.label_MED9.setText("")
        self.label_MED10.setText("")
        self.label_MED11.setText("")
        self.label_MED12.setText("")
        self.fad_med.hide()
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
