# Form implementation generated from reading ui file 'laba3design.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.concealment = QtWidgets.QPushButton(self.centralwidget)
        self.concealment.setGeometry(QtCore.QRect(20, 100, 200, 40))
        self.concealment.setObjectName("concealment")
        self.string_extraction = QtWidgets.QPushButton(self.centralwidget)
        self.string_extraction.setGeometry(QtCore.QRect(220, 100, 200, 40))
        self.string_extraction.setObjectName("string_extraction")
        self.path = QtWidgets.QPushButton(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(420, 100, 200, 40))
        self.path.setObjectName("path")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(20, 140, 400, 280))
        self.image.setStyleSheet("background-color: rgb(194, 194, 196);")
        self.image.setText("")
        self.image.setObjectName("image")
        self.path_to_pic_label = QtWidgets.QLabel(self.centralwidget)
        self.path_to_pic_label.setGeometry(QtCore.QRect(420, 140, 200, 30))
        self.path_to_pic_label.setObjectName("path_to_pic_label")
        self.ascii_string = QtWidgets.QLineEdit(self.centralwidget)
        self.ascii_string.setGeometry(QtCore.QRect(20, 30, 600, 30))
        self.ascii_string.setObjectName("ascii_string")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.concealment.setText(_translate("MainWindow", "concealment mod"))
        self.string_extraction.setText(_translate("MainWindow", "string extraction"))
        self.path.setText(_translate("MainWindow", "Path"))
        self.path_to_pic_label.setText(_translate("MainWindow", "Текущий путь к картинке"))