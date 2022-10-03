# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Jarvis2UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1921, 970)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1921, 1051))
        self.background.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.background.setText("")
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.foreground = QtWidgets.QLabel(self.centralwidget)
        self.foreground.setGeometry(QtCore.QRect(0, -20, 1921, 1001))
        self.foreground.setText("")
        self.foreground.setPixmap(QtGui.QPixmap(".\\GUI/ExtraGui/Jarvis_Gui (2).gif"))
        self.foreground.setScaledContents(True)
        self.foreground.setObjectName("foreground")
        self.startbtn = QtWidgets.QPushButton(self.centralwidget)
        self.startbtn.setGeometry(QtCore.QRect(1470, 430, 181, 71))
        self.startbtn.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"CaskaydiaCove NF\";\n"
"border: 1px solid white;\n"
"/*background-color: rgb(85, 255, 255);*/")
        self.startbtn.setObjectName("startbtn")
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(1470, 530, 181, 71))
        self.exitbtn.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 16pt \"CaskaydiaCove NF\";\n"
"background-color: rgb(255, 0, 0);\n"
"border: 1px solid white;")
        self.exitbtn.setObjectName("exitbtn")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(770, 380, 391, 61))
        self.textBrowser.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid white;")
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startbtn.setText(_translate("MainWindow", "START"))
        self.exitbtn.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
