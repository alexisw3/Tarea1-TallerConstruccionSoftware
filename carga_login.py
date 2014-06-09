# -*- coding: utf-8 -*-

from PySide import QtGui
from login import Ui_Form
import sys
import carga_Productos
import metodos_login


#clase para ver ventana de login
class Login(QtGui.QWidget):
    def __init__(self):
        super(Login, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.escuchador()
        self.show()

#respuestas al hacer click sobre los botones
    def escuchador(self):
        self.ui.user_in.clicked.connect(self.aceptado)
        self.ui.user_out.clicked.connect(self.cerrar)

#mostrar ventana principal
    def ventana_principal(self):
        form = carga_Productos.Bd_Productos()
        form.exec_()

#funcion para verificar identidad del usuario
    def aceptado(self):
        clave = self.ui.line_pass.text()
        usuario = self.ui.line_user.text()
        clave_bd = metodos_login.obt_clave(usuario)
        usuario_bd = metodos_login.obt_usuario(clave)
        if clave or usuario:
            try:
                for i in clave_bd:
                    c = clave_bd["password"]
            except:
                self.error_usuario()
            for i in usuario_bd:
                u = usuario_bd["user"]
        else:
            self.error_usuario()
        if clave == c and usuario == u:
            self.cerrar()
            self.ventana_principal()
        else:
            self.error_usuario()

    def error_usuario(self):
        self.ui.m_error = QtGui.QMessageBox()
        self.ui.m_error.setWindowTitle(" Error ")
        self.ui.m_error.setText("Error de Usuario y/o Clave")
        self.ui.m_error.setDefaultButton(QtGui.QMessageBox.Ok)
        self.ui.m_error.exec_()

    def cerrar(self):
        self.close()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Login()
    sys.exit(app.exec_())
