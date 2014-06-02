#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import metodos
from interfaz_Principal import Ui_TareaWindow
import metodos_Ventana


#funciona el editar y nuevo producto creo DX
class Bd_Productos(QtGui.QWidget):

    def __init__(self):
        super(Bd_Productos, self).__init__()
        self.ui = Ui_TareaWindow()
        self.ui.setupUi(self)
        self.show()
        self.carga_Productos()
        self.escuchadores()

# aqui se hace la magia de la grilla y aparecen en pantalla
    def carga_Productos(self, productos=None):
        if productos is None:
            productos = metodos.obtener_Productos()
        self.model = QtGui.QStandardItemModel(len(productos), 6)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Id"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Descripción"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Color"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Precio"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Marca"))
        r = 0
        for row in productos:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['codigo'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['descripcion'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['precio'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['marca'])
            r = r + 1
        self.ui.table_mark.setModel(self.model)
        self.ui.table_mark.setColumnWidth(0, 2)
        self.ui.table_mark.setColumnWidth(1, 198)
        self.ui.table_mark.setColumnWidth(2, 250)
        self.ui.table_mark.setColumnWidth(3, 150)
        self.ui.table_mark.setColumnWidth(4, 150)
        self.ui.table_mark.setColumnWidth(5, 150)

    def carga_Marcas(self):
        marcas = metodos.obtener_Marcas()
        self.ui.combo_brands.addItem("Todos", -1)
        for marca in marcas:
            self.ui.combo_brands.addItem(marca["nombre"], marca["id_marca"])

    def filtra_Produc_Marcas(self, index):
        id_marca = self.ui.combo_brands.itemData(
            self.ui.combo_brands.currentIndex())
        if id_marca == -1:
            productos = metodos.obtener_Productos()
        else:
            productos = metodos.obt_ProducXMarca(id_marca)
        self.carga_Productos(productos)

    def ventana_agregaProducto(self):
        form = metodos_Ventana.Form(self)
        form.rejected.connect(self.carga_Productos)
        form.exec_()


    def ventana_editaProducto(self):
        model = self.ui.table_mark.model()
        index = self.ui.table_mark.currentIndex()
        if index.row() == -1:
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            codigo = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            form = metodos_Ventana.Form(self, codigo)
            form.rejected.connect(self.carga_Productos)
            form.exec_()

        self.carga_Productos()


    def escuchadores(self):
        self.ui.new_Button.clicked.connect(self.ventana_agregaProducto)
        self.ui.edit_Button.clicked.connect(self.ventana_editaProducto)
        self.ui.table_mark.doubleClicked.connect(self.ventana_editaProducto)
        self.ui.combo_brands.activated[int].connect(
            self.filtra_Produc_Marcas)


#falta lo de eliminar
#lo de text line



def run():
    app = QtGui.QApplication(sys.argv)
    main = Bd_Productos()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
