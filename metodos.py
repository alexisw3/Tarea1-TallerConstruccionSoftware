#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3


def connect():
    con = sqlite3.connect('base_productos.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_Productos():
    con = connect()
    c = con.cursor()
    query = """SELECT p.codigo, p.nombre, p.descripcion, p.color, p.precio,
             m.nombre as 'marca'FROM productos p,
              marcas m WHERE p.fk_id_marca = m.id_marca"""
    result = c.execute(query)
    productos = result.fetchall()
    con.close()
    return productos


def obt_ProducXCod(codigo):
    con = connect()
    c = con.cursor()
    query = "SELECT * FROM productos WHERE codigo = ?"
    result = c.execute(query, [codigo])
    productos = result.fetchone()
    con.close()
    return productos


#Falta implementar
def buscar_Producto():
    con = connect()
    c = con.cursor()
    query = """SELECT p.codigo, p.nombre, p.descripcion,
            p.color, p.precio, m.nombre as 'marca'FROM productos p,
           marcas m WHERE p.fk_id_marca
           = m.id_marca AND (p.nombre LIKE '%'||?||'%' )"""

    con.close()
    return productos


def obtener_Marcas():
    con = connect()
    c = con.cursor()
    query = """SELECT id_marca, nombre FROM marcas"""
    result = c.execute(query)
    marcas = result.fetchall()
    con.close()
    return marcas


def obt_ProducXMarca(id_marca):
    con = connect()
    c = con.cursor()
    query = """SELECT p.codigo, p.nombre, p.descripcion, p.color,
             p.precio, m.nombre as 'marca'FROM productos p,
             marcas m WHERE p.fk_id_marca = m.id_marca AND p.fk_id_marca = ?"""
    result = c.execute(query, [id_marca])
    productos = result.fetchall()
    con.close()
    return productos


def eliminar(codigo):
    salida = False
    con = connect()
    c = con.cursor()
    query = "DELETE FROM productos WHERE codigo = ?"
    try:
        resultado = c.execute(query, [codigo])
        con.commit()
        salida = True
    except sqlite3.Error as e:
        salida = False
        print "Error:", e.args[0]
    con.close()
    return salida


def editar(entrada, nom, desc, col, prec, marc):
    salida = False
    con = connect()
    c = con.cursor()
    nom = nom
    desc = desc
    col = col
    prec = prec
    marc = marc
    query = """UPDATE productos SET nombre= ?,
     descripcion = ?, color = ?, precio = ?, fk_id_marca = ? WHERE codigo = ?"""
    try:
        resultado = c.execute(query, [nom, desc, col, prec, marc, entrada])
        con.commit()
        salida = True
    except sqlite3.Error as e:
        salida = False
        print "Error:", e.args[0]
    con.close()
    return salida

#Falta implementar Agregar un nuevo producto
def agregar_nuevo(n):
    salida = False
    return salida