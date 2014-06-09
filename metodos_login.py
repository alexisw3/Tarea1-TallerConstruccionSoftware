# -*- coding: utf-8 -*-

import sqlite3


#conecto con la base de datos de los usuarios
def connect():
    con = sqlite3.connect('base_usuarios.db')
    con.row_factory = sqlite3.Row
    return con


#obtengo todos los usuarios
def obtener_usuarios():
    con = connect()
    c = con.cursor()
    query = """SELECT * FROM usuarios"""
    result = c.execute(query)
    usuarios = result.fetchall()
    con.close()
    return usuarios

# obtengo la clave de acuerdo a cierto usuario
def obt_clave(usuario):
    con = connect()
    c = con.cursor()
    query = "SELECT password FROM usuarios WHERE user = ?"
    resultado= c.execute(query, [usuario])
    clave = resultado.fetchone()
    con.close()
    return clave


# obtengo el usuario de a acuerdo a la clave
def obt_usuario(clave):
    con = connect()
    c = con.cursor()
    query = "SELECT user FROM usuarios WHERE password = ?"
    resultado= c.execute(query, [clave])
    usuario = resultado.fetchone()
    con.close()
    return usuario



#if __name__ == "__main__":
#    usuarios = obt_usuario("pajarito1")
#    for usuario in usuarios:
#        print usuarios["user"]
