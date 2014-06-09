# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Jun  7 12:30:09 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayoutWidget = QtGui.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 60, 160, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_user = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.line_user.setObjectName("line_user")
        self.verticalLayout.addWidget(self.line_user)
        self.line_pass = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.line_pass.setObjectName("line_pass")
        self.verticalLayout.addWidget(self.line_pass)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(70, 70, 61, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(110, 180, 160, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.user_in = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.user_in.setObjectName("user_in")
        self.verticalLayout_3.addWidget(self.user_in)
        self.user_out = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.user_out.setObjectName("user_out")
        self.verticalLayout_3.addWidget(self.user_out)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate(
            "Form", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate(
            "Form", "Usuario:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate(
            "Form", "Clave:", None, QtGui.QApplication.UnicodeUTF8))
        self.user_in.setText(QtGui.QApplication.translate(
            "Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.user_out.setText(QtGui.QApplication.translate(
            "Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

