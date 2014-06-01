#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import metodos
from interfaz_Principal import Ui_TareaWindow
import metodos_Ventana


class Bd_Productos(QtGui.QWidget):

    def __init__(self):
        super(Bd_Productos, self).__init__()
        self.ui = Ui_TareaWindow()
        self.ui.setupUi(self)
        #self.carga_Productos()
        #self.carga_Marcas()
        self.show()
        self.escuchadores()




def run():
    app = QtGui.QApplication(sys.argv)
    main = Bd_Productos()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
