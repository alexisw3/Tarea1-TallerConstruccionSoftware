#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


#se realiza la coneccion a la base de datos
def connect():
    con = sqlite3.connect('base_marcas.db')
    con.row_factory = sqlite3.Row
    return con



def obtener_Productos():

    return productos


def obtener_Marcas():

    return marcas



def obt_ProducXCod(codigo):

    return productos



def obt_ProducXMarca(id_marca):

    return productos



def buscar_Producto(word):

    return productos

def eliminar(codigo):
    salida = False

    return salida


def editar(entrada, nom, desc, col, prec, marc):
    salida = False

    return salida

#agrega un nuevo producto, con todos los parametros necesarios
def agregar_nuevo(nombre, descripcion, color, precio, fk_id_marca):
    salida = False

    return salida