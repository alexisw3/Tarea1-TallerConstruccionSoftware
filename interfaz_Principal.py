# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_Principal.ui'
#
# Created: Sat May 31 19:14:43 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TareaWindow(object):
    def setupUi(self, TareaWindow):
        TareaWindow.setObjectName("TareaWindow")
        TareaWindow.resize(1024, 680)
        self.table_mark = QtGui.QTableView(TareaWindow)
        self.table_mark.setGeometry(QtCore.QRect(30, 170, 961, 471))
        self.table_mark.setObjectName("table_mark")
        self.table_mark.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.delete_Button = QtGui.QPushButton(TareaWindow)
        self.delete_Button.setGeometry(QtCore.QRect(880, 50, 111, 27))
        self.delete_Button.setObjectName("delete_Button")
        self.edit_Button = QtGui.QPushButton(TareaWindow)
        self.edit_Button.setGeometry(QtCore.QRect(740, 50, 121, 27))
        self.edit_Button.setObjectName("edit_Button")
        self.new_Button = QtGui.QPushButton(TareaWindow)
        self.new_Button.setGeometry(QtCore.QRect(580, 50, 141, 27))
        self.new_Button.setObjectName("new_Button")
        self.search_name = QtGui.QLineEdit(TareaWindow)
        self.search_name.setGeometry(QtCore.QRect(80, 110, 331, 27))
        self.search_name.setStatusTip("")
        self.search_name.setText("")
        self.search_name.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.search_name.setObjectName("search_name")
        self.label = QtGui.QLabel(TareaWindow)
        self.label.setGeometry(QtCore.QRect(550, 110, 161, 21))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.combo_brands = QtGui.QComboBox(TareaWindow)
        self.combo_brands.setGeometry(QtCore.QRect(710, 110, 271, 27))
        self.combo_brands.setObjectName("combo_brands")

        self.retranslateUi(TareaWindow)
        QtCore.QMetaObject.connectSlotsByName(TareaWindow)

    def retranslateUi(self, TareaWindow):
        TareaWindow.setWindowTitle(QtGui.QApplication.translate("TareaWindow", "Tarea 1: Base de Datos de Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.delete_Button.setText(QtGui.QApplication.translate("TareaWindow", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_Button.setText(QtGui.QApplication.translate("TareaWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.new_Button.setText(QtGui.QApplication.translate("TareaWindow", "Nuevo producto", None, QtGui.QApplication.UnicodeUTF8))
        self.search_name.setPlaceholderText(QtGui.QApplication.translate("TareaWindow", "¿Qué producto está buscando?", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("TareaWindow", "Seleccione una marca:", None, QtGui.QApplication.UnicodeUTF8))

