# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_Producto.ui'
#
# Created: Sat May 31 19:17:01 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_newWindow(object):
    def setupUi(self, newWindow):
        newWindow.setObjectName("newWindow")
        newWindow.resize(411, 240)
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
        self.fk_line.setGeometry(QtCore.QRect(180, 140, 191, 27))
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
        self.label_5.setGeometry(QtCore.QRect(30, 150, 131, 20))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(newWindow)
        QtCore.QMetaObject.connectSlotsByName(newWindow)

    def retranslateUi(self, newWindow):
        newWindow.setWindowTitle(QtGui.QApplication.translate("newWindow", "Nuevo producto", None, QtGui.QApplication.UnicodeUTF8))
        self.ok_Button.setText(QtGui.QApplication.translate("newWindow", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_line.setPlaceholderText(QtGui.QApplication.translate("newWindow", "Ej: zapatilla", None, QtGui.QApplication.UnicodeUTF8))
        self.descripcion_line.setPlaceholderText(QtGui.QApplication.translate("newWindow", "Ej: calzado", None, QtGui.QApplication.UnicodeUTF8))
        self.color_line.setPlaceholderText(QtGui.QApplication.translate("newWindow", "Ej: blancas", None, QtGui.QApplication.UnicodeUTF8))
        self.precio_line.setPlaceholderText(QtGui.QApplication.translate("newWindow", "Ej: 20000", None, QtGui.QApplication.UnicodeUTF8))
        self.fk_line.setPlaceholderText(QtGui.QApplication.translate("newWindow", "Ej: Nike", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("newWindow", "Nombre Producto:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("newWindow", "Descripcion:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("newWindow", "Color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("newWindow", "Precio:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("newWindow", "Marca:", None, QtGui.QApplication.UnicodeUTF8))

