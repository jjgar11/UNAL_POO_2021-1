# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'propMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PropMainWindow(object):
    def setupUi(self, PropMainWindow):
        PropMainWindow.setObjectName("PropMainWindow")
        PropMainWindow.setEnabled(True)
        PropMainWindow.resize(812, 431)
        PropMainWindow.setMinimumSize(QtCore.QSize(812, 431))
        PropMainWindow.setMaximumSize(QtCore.QSize(813, 431))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        PropMainWindow.setFont(font)
        PropMainWindow.setMouseTracking(False)
        PropMainWindow.setTabletTracking(False)
        PropMainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        PropMainWindow.setAnimated(True)
        PropMainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(PropMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DocumentacionUsuario = QtWidgets.QPushButton(self.centralwidget)
        self.DocumentacionUsuario.setGeometry(QtCore.QRect(0, 350, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.DocumentacionUsuario.setFont(font)
        self.DocumentacionUsuario.setMouseTracking(True)
        self.DocumentacionUsuario.setStyleSheet("background-color: rgb(242, 243, 244);")
        self.DocumentacionUsuario.setCheckable(False)
        self.DocumentacionUsuario.setObjectName("DocumentacionUsuario")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 50, 811, 51))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(0, 163, 224);\n"
"border-color: rgb(85, 170, 255);\n"
"")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 110, 301, 251))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border-image: url(:/icono vacuna/icono vacuna.png);\n"
"border-image: url(:/iconoVacuna/icono vacuna.png);")
        self.label_2.setObjectName("label_2")
        PropMainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(PropMainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 812, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuAfiliados = QtWidgets.QMenu(self.menuBar)
        self.menuAfiliados.setObjectName("menuAfiliados")
        self.menuLotes_de_vacunas = QtWidgets.QMenu(self.menuBar)
        self.menuLotes_de_vacunas.setObjectName("menuLotes_de_vacunas")
        self.menuConsultar = QtWidgets.QMenu(self.menuLotes_de_vacunas)
        self.menuConsultar.setMouseTracking(True)
        self.menuConsultar.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menuConsultar.setObjectName("menuConsultar")
        self.menuPlan_de_vacunacion = QtWidgets.QMenu(self.menuBar)
        self.menuPlan_de_vacunacion.setObjectName("menuPlan_de_vacunacion")
        self.menuConsultar_2 = QtWidgets.QMenu(self.menuPlan_de_vacunacion)
        self.menuConsultar_2.setObjectName("menuConsultar_2")
        self.menuProgramacion_de_vacunacion = QtWidgets.QMenu(self.menuBar)
        self.menuProgramacion_de_vacunacion.setObjectName("menuProgramacion_de_vacunacion")
        self.menuConsultar_3 = QtWidgets.QMenu(self.menuProgramacion_de_vacunacion)
        self.menuConsultar_3.setObjectName("menuConsultar_3")
        PropMainWindow.setMenuBar(self.menuBar)
        self.actionConsultar_Afiliado = QtWidgets.QAction(PropMainWindow)
        self.actionConsultar_Afiliado.setObjectName("actionConsultar_Afiliado")
        self.actionDesafiliar = QtWidgets.QAction(PropMainWindow)
        self.actionDesafiliar.setObjectName("actionDesafiliar")
        self.actionVacunar = QtWidgets.QAction(PropMainWindow)
        self.actionVacunar.setObjectName("actionVacunar")
        self.actionCrear = QtWidgets.QAction(PropMainWindow)
        self.actionCrear.setObjectName("actionCrear")
        self.actionCrear_2 = QtWidgets.QAction(PropMainWindow)
        self.actionCrear_2.setObjectName("actionCrear_2")
        self.actionConsulta_completa = QtWidgets.QAction(PropMainWindow)
        self.actionConsulta_completa.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionConsulta_completa.setObjectName("actionConsulta_completa")
        self.actionIndividual = QtWidgets.QAction(PropMainWindow)
        self.actionIndividual.setObjectName("actionIndividual")
        self.actionCompleta = QtWidgets.QAction(PropMainWindow)
        self.actionCompleta.setObjectName("actionCompleta")
        self.actionCrear_3 = QtWidgets.QAction(PropMainWindow)
        self.actionCrear_3.setObjectName("actionCrear_3")
        self.actionCompleta_2 = QtWidgets.QAction(PropMainWindow)
        self.actionCompleta_2.setObjectName("actionCompleta_2")
        self.actionIndividual_2 = QtWidgets.QAction(PropMainWindow)
        self.actionIndividual_2.setObjectName("actionIndividual_2")
        self.actionCrear_4 = QtWidgets.QAction(PropMainWindow)
        self.actionCrear_4.setObjectName("actionCrear_4")
        self.actionCompleta_3 = QtWidgets.QAction(PropMainWindow)
        self.actionCompleta_3.setObjectName("actionCompleta_3")
        self.actionIndividual_3 = QtWidgets.QAction(PropMainWindow)
        self.actionIndividual_3.setObjectName("actionIndividual_3")
        self.actionCrear_5 = QtWidgets.QAction(PropMainWindow)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.actionCrear_5.setFont(font)
        self.actionCrear_5.setObjectName("actionCrear_5")
        self.menuAfiliados.addAction(self.actionCrear_5)
        self.menuAfiliados.addAction(self.actionConsultar_Afiliado)
        self.menuAfiliados.addAction(self.actionDesafiliar)
        self.menuAfiliados.addAction(self.actionVacunar)
        self.menuConsultar.addAction(self.actionConsulta_completa)
        self.menuConsultar.addAction(self.actionIndividual)
        self.menuLotes_de_vacunas.addAction(self.actionCrear)
        self.menuLotes_de_vacunas.addAction(self.menuConsultar.menuAction())
        self.menuConsultar_2.addAction(self.actionCompleta_2)
        self.menuConsultar_2.addAction(self.actionIndividual_2)
        self.menuPlan_de_vacunacion.addAction(self.actionCrear_3)
        self.menuPlan_de_vacunacion.addAction(self.menuConsultar_2.menuAction())
        self.menuConsultar_3.addAction(self.actionCompleta_3)
        self.menuConsultar_3.addAction(self.actionIndividual_3)
        self.menuProgramacion_de_vacunacion.addAction(self.actionCrear_4)
        self.menuProgramacion_de_vacunacion.addAction(self.menuConsultar_3.menuAction())
        self.menuBar.addAction(self.menuAfiliados.menuAction())
        self.menuBar.addAction(self.menuLotes_de_vacunas.menuAction())
        self.menuBar.addAction(self.menuPlan_de_vacunacion.menuAction())
        self.menuBar.addAction(self.menuProgramacion_de_vacunacion.menuAction())

        self.retranslateUi(PropMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PropMainWindow)

    def retranslateUi(self, PropMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PropMainWindow.setWindowTitle(_translate("PropMainWindow", "P_MainWindow"))
        PropMainWindow.setToolTip(_translate("PropMainWindow", "cosas"))
        self.DocumentacionUsuario.setText(_translate("PropMainWindow", "Ayuda para usuarios"))
        self.label.setText(_translate("PropMainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">Programa de vacunación</span></p></body></html>"))
        self.label_2.setText(_translate("PropMainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menuAfiliados.setTitle(_translate("PropMainWindow", "Afiliados"))
        self.menuLotes_de_vacunas.setTitle(_translate("PropMainWindow", "Lotes de vacunas"))
        self.menuConsultar.setTitle(_translate("PropMainWindow", "Consultar"))
        self.menuPlan_de_vacunacion.setTitle(_translate("PropMainWindow", "Plan de vacunación"))
        self.menuConsultar_2.setTitle(_translate("PropMainWindow", "Consultar"))
        self.menuProgramacion_de_vacunacion.setTitle(_translate("PropMainWindow", "Programacion de vacunación"))
        self.menuConsultar_3.setTitle(_translate("PropMainWindow", "Consultar"))
        self.actionConsultar_Afiliado.setText(_translate("PropMainWindow", "Consultar"))
        self.actionDesafiliar.setText(_translate("PropMainWindow", "Desafiliar"))
        self.actionVacunar.setText(_translate("PropMainWindow", "Vacunar"))
        self.actionCrear.setText(_translate("PropMainWindow", "Crear"))
        self.actionCrear_2.setText(_translate("PropMainWindow", "Crear"))
        self.actionConsulta_completa.setText(_translate("PropMainWindow", "completa"))
        self.actionIndividual.setText(_translate("PropMainWindow", "Individual"))
        self.actionCompleta.setText(_translate("PropMainWindow", "Completa"))
        self.actionCrear_3.setText(_translate("PropMainWindow", "Crear"))
        self.actionCompleta_2.setText(_translate("PropMainWindow", "Completa"))
        self.actionIndividual_2.setText(_translate("PropMainWindow", "Individual"))
        self.actionCrear_4.setText(_translate("PropMainWindow", "Crear"))
        self.actionCompleta_3.setText(_translate("PropMainWindow", "Completa"))
        self.actionIndividual_3.setText(_translate("PropMainWindow", "Individual"))
        self.actionCrear_5.setText(_translate("PropMainWindow", "Crear"))
import imagesForUi_rc
