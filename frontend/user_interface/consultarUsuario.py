# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultarUsuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 601)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BuscarNoIdConsultaUsuario = QtWidgets.QPushButton(self.centralwidget)
        self.BuscarNoIdConsultaUsuario.setEnabled(True)
        self.BuscarNoIdConsultaUsuario.setGeometry(QtCore.QRect(620, 53, 100, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BuscarNoIdConsultaUsuario.setFont(font)
        self.BuscarNoIdConsultaUsuario.setObjectName("BuscarNoIdConsultaUsuario")
        self.splitter_4 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_4.setGeometry(QtCore.QRect(70, 53, 550, 35))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_12 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.noIdConsultaUsuario = QtWidgets.QLineEdit(self.splitter_4)
        self.noIdConsultaUsuario.setEnabled(True)
        self.noIdConsultaUsuario.setFrame(True)
        self.noIdConsultaUsuario.setObjectName("noIdConsultaUsuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 53, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 120, 641, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 8, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 4, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 9, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 7, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 5, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 6, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 510, 611, 31))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuVolver = QtWidgets.QMenu(self.menubar)
        self.menuVolver.setObjectName("menuVolver")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuVolver.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Consultar usuario"))
        self.BuscarNoIdConsultaUsuario.setText(_translate("MainWindow", "Buscar"))
        self.label_12.setText(_translate("MainWindow", "Ingrese el documento de identidad del usuario "))
        self.label_21.setText(_translate("MainWindow", "Vacunado"))
        self.label_17.setText(_translate("MainWindow", "Correo"))
        self.label_22.setText(_translate("MainWindow", "Fecha desafiliacion"))
        self.label_14.setText(_translate("MainWindow", "Direccion"))
        self.label_15.setText(_translate("MainWindow", "Telefono"))
        self.label_20.setText(_translate("MainWindow", "Fecha de afiliacion"))
        self.label_18.setText(_translate("MainWindow", "Ciudad"))
        self.label_13.setText(_translate("MainWindow", "Apellido"))
        self.label_16.setText(_translate("MainWindow", "Nombre"))
        self.label_19.setText(_translate("MainWindow", "Fecha de nacimiento         "))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#aa0000;\"><br/></span></p></body></html>"))
        self.menuVolver.setTitle(_translate("MainWindow", "Volver"))
