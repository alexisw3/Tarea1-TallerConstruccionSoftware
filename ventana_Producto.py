# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_Producto.ui'
#
# Created: Mon Jun  2 11:13:50 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_newWindow(object):
    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(700, 500)
        self.ok_Button = QtGui.QPushButton(newWindow)
        self.ok_Button.setGeometry(QtCore.QRect(150, 200, 98, 27))
        self.ok_Button.setObjectName("ok_Button")
        self.nombre_line = QtGui.QLineEdit(newWindow)
        self.nombre_line.setGeometry(QtCore.QRect(180, 20, 191, 27))
        self.nombre_line.setObjectName("nombre_line")
        self.descripcion_line = QtGui.QLineEdit(newWindow)
        self.descripcion_line.setGeometry(QtCore.QRect(180, 50, 191, 27))
        self.descripcion_line.setObjectName("descripcion_line")
        self.color_line = QtGui.QLineEdit(newWindow)
        self.color_line.setGeometry(QtCore.QRect(180, 80, 191, 27))
        self.color_line.setObjectName("color_line")
        self.precio_line = QtGui.QLineEdit(newWindow)
        self.precio_line.setGeometry(QtCore.QRect(180, 110, 191, 27))
        self.precio_line.setObjectName("precio_line")
        self.fk_line = QtGui.QLineEdit(newWindow)
        self.fk_line.setGeometry(QtCore.QRect(400, 120, 191, 27))
        self.fk_line.setObjectName("fk_line")
        self.label = QtGui.QLabel(newWindow)
        self.label.setGeometry(QtCore.QRect(30, 30, 131, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(newWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 121, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(newWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 90, 121, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(newWindow)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 121, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtGui.QLabel(newWindow)
        self.label_5.setGeometry(QtCore.QRect(400, 100, 200, 20))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtGui.QLabel(newWindow)
        self.label_7.setGeometry(QtCore.QRect(400, 20, 131, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtGui.QLabel(newWindow)
        self.label_8.setGeometry(QtCore.QRect(400, 40, 131, 20))
        self.label_8.setObjectName("label_9")
        self.label_9 = QtGui.QLabel(newWindow)
        self.label_9.setGeometry(QtCore.QRect(400, 60, 131, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtGui.QLabel(newWindow)
        self.label_10.setGeometry(QtCore.QRect(400, 80, 131, 20))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtGui.QLabel(newWindow)
        self.label_11.setGeometry(QtCore.QRect(550, 40, 131, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtGui.QLabel(newWindow)
        self.label_12.setGeometry(QtCore.QRect(550, 60, 131, 20))
        self.label_12.setObjectName("label_12")
        self.label_6 = QtGui.QLabel(newWindow)
        self.label_6.setGeometry(QtCore.QRect(200, 200, 300, 300))
        self.retranslateUi(newWindow)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

    def retranslateUi(self, newWindow):
        newWindow.setWindowTitle(QtGui.QApplication.translate(
            "newWindow", "Nuevo producto", None,
             QtGui.QApplication.UnicodeUTF8))
        self.ok_Button.setText(QtGui.QApplication.translate(
            "newWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_line.setPlaceholderText(QtGui.QApplication.translate(
            "newWindow", "Ej: zapatilla", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion_line.setPlaceholderText(QtGui.QApplication.translate(
            "newWindow", "Ej: calzado", None, QtGui.QApplication.UnicodeUTF8))
        self.color_line.setPlaceholderText(QtGui.QApplication.translate(
            "newWindow", "Ej: blancas", None, QtGui.QApplication.UnicodeUTF8))
        self.precio_line.setPlaceholderText(QtGui.QApplication.translate(
            "newWindow", "Ej: 20000", None, QtGui.QApplication.UnicodeUTF8))
        self.fk_line.setPlaceholderText(QtGui.QApplication.translate(
            "newWindow", "Ej: 1", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate(
            "newWindow", "Nombre Producto:", None,
             QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate(
            "newWindow", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate(
            "newWindow", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate(
            "newWindow", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate(
            "newWindow", "Ingrese opcion numero:", None,
             QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate(
            "newWindow", "Opciones de Marcas:",
             None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate(
           "newWindow", "1 : Nike", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate(
            "newWindow", "2 : Reebok", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate(
            "newWindow", "3 : Apple", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate(
            "newWindow", "4 : Samsung", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate(
            "newWindow", "5 : Microsoft", None, QtGui.QApplication.UnicodeUTF8))


