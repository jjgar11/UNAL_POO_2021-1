# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consultaProgramacionVacuna.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConsultaProgramacion(object):
    def setupUi(self, ConsultaProgramacion):
        ConsultaProgramacion.setObjectName("ConsultaProgramacion")
        ConsultaProgramacion.resize(850, 700)
        self.centralwidget = QtWidgets.QWidget(ConsultaProgramacion)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 20, 341, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 511, 31))
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 240, 810, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.verticalHeader().setDefaultSectionSize(35)
        self.buttonAtras = QtWidgets.QPushButton(self.centralwidget)
        self.buttonAtras.setGeometry(QtCore.QRect(20, 610, 101, 31))
        self.buttonAtras.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.buttonAtras.setObjectName("buttonAtras")
        self.mensaje = QtWidgets.QLabel(self.centralwidget)
        self.mensaje.setGeometry(QtCore.QRect(170, 610, 541, 31))
        self.mensaje.setObjectName("mensaje")
        self.noId = QtWidgets.QLineEdit(self.centralwidget)
        self.noId.setGeometry(QtCore.QRect(540, 100, 161, 32))
        self.noId.setObjectName("noId")
        self.btnBuscar = QtWidgets.QPushButton(self.centralwidget)
        self.btnBuscar.setGeometry(QtCore.QRect(710, 100, 88, 34))
        self.btnBuscar.setObjectName("btnBuscar")
        self.btnConsultaCompleta = QtWidgets.QPushButton(self.centralwidget)
        self.btnConsultaCompleta.setGeometry(QtCore.QRect(710, 180, 111, 34))
        self.btnConsultaCompleta.setObjectName("btnConsultaCompleta")
        self.campoConsulta = QtWidgets.QComboBox(self.centralwidget)
        self.campoConsulta.setGeometry(QtCore.QRect(470, 180, 231, 31))
        self.campoConsulta.setObjectName("campoConsulta")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.campoConsulta.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        ConsultaProgramacion.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ConsultaProgramacion)
        self.statusbar.setObjectName("statusbar")
        ConsultaProgramacion.setStatusBar(self.statusbar)

        self.retranslateUi(ConsultaProgramacion)
        QtCore.QMetaObject.connectSlotsByName(ConsultaProgramacion)

    def retranslateUi(self, ConsultaProgramacion):
        _translate = QtCore.QCoreApplication.translate
        ConsultaProgramacion.setWindowTitle(_translate("ConsultaProgramacion", "MainWindow"))
        self.label.setText(_translate("ConsultaProgramacion", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Programación de vacunación</span></p></body></html>"))
        self.label_2.setText(_translate("ConsultaProgramacion", "<html><head/><body><p><span style=\" font-size:14pt;\">Ingrese el documento de identidad que desea consultar</span></p></body></html>"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("ConsultaProgramacion", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ConsultaProgramacion", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ConsultaProgramacion", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ConsultaProgramacion", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ConsultaProgramacion", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("ConsultaProgramacion", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("ConsultaProgramacion", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("ConsultaProgramacion", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("ConsultaProgramacion", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("ConsultaProgramacion", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConsultaProgramacion", "No. Identificación"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConsultaProgramacion", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ConsultaProgramacion", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ConsultaProgramacion", "Dirección"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ConsultaProgramacion", "Teléfono"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ConsultaProgramacion", "Correo"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ConsultaProgramacion", "Fecha Programada"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ConsultaProgramacion", "Hora programada"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("ConsultaProgramacion", "Número de lote de vacuna"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("ConsultaProgramacion", "Fabricante de la vacuna"))
        self.buttonAtras.setText(_translate("ConsultaProgramacion", "Volver"))
        self.mensaje.setText(_translate("ConsultaProgramacion", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.btnBuscar.setText(_translate("ConsultaProgramacion", "Buscar"))
        self.btnConsultaCompleta.setText(_translate("ConsultaProgramacion", "Consultar"))
        self.campoConsulta.setItemText(0, _translate("ConsultaProgramacion", "Número de Identificación"))
        self.campoConsulta.setItemText(1, _translate("ConsultaProgramacion", "Nombre"))
        self.campoConsulta.setItemText(2, _translate("ConsultaProgramacion", "Apellido"))
        self.campoConsulta.setItemText(3, _translate("ConsultaProgramacion", "Dirección"))
        self.campoConsulta.setItemText(4, _translate("ConsultaProgramacion", "Teléfono"))
        self.campoConsulta.setItemText(5, _translate("ConsultaProgramacion", "Correo"))
        self.campoConsulta.setItemText(6, _translate("ConsultaProgramacion", "Fecha Programada"))
        self.campoConsulta.setItemText(7, _translate("ConsultaProgramacion", "Hora Programada"))
        self.campoConsulta.setItemText(8, _translate("ConsultaProgramacion", "Número de lote"))
        self.campoConsulta.setItemText(9, _translate("ConsultaProgramacion", "Fabricante"))
        self.label_4.setText(_translate("ConsultaProgramacion", "<html><head/><body><p>O consulte la programacion completa ordenada por:</p></body></html>"))
