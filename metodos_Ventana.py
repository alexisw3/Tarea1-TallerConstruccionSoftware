#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui

import metodos
from ventana_Producto import Ui_newWindow


class Form(QtGui.QDialog):
    def __init__(self, parent=None, codigo=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_newWindow()
        self.ui.setupUi(self)
        if codigo is None:
            self.ui.ok_Button.clicked.connect(self.agregar)
        else:
            self.ui.codigo = codigo
            datos_productos = metodos.obt_ProducXCod(codigo)
            self.ui.nombre_line.setText(datos_productos["nombre"])
            self.ui.descripcion_line.setText(datos_productos["descripcion"])
            self.ui.color_line.setText(datos_productos["color"])
            string_precio = str(datos_productos["precio"])
            self.ui.precio_line.setText(string_precio)
            string_fk_id_marca = str(datos_productos["fk_id_marca"])
            self.ui.fk_line.setText(string_fk_id_marca)
            self.ui.ok_Button.clicked.connect(self.editar)


    def agregar(self):
        nombre = self.ui.nombre_line.text()
        descripcion = self.ui.descripcion_line.text()
        color = self.ui.color_line.text()
        precio = self.ui.precio_line.text()
        marca = self.ui.fk_line.text()
        result = metodos.agregar_nuevo(
            nombre, descripcion, color, precio, marca)
        if result:
            self.reject()
        else:
            self.ui.mensajes.setText(
                "Hubo un problema al intentar crear el producto")

    #Metodo para editar los productos
    def editar(self):
        codigo = self.ui.codigo
        nombre = self.ui.nombre_line.text()
        descripcion = self.ui.descripcion_line.text()
        color = self.ui.color_line.text()
        precio = self.ui.precio_line.text()
        marca = self.ui.fk_line.text()
        result = metodos.editar(codigo, nombre, descripcion, color, precio, marca)
        if result:
            self.reject()
        else:
            self.ui.mensajes.setText("Hubo un problema al editar el producto")

    def cancel(self):
        self.reject()