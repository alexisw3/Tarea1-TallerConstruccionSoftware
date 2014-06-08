# -*- coding: utf-8 -*-

import sqlite3


def connect():#conecto con la base de datos de los usuarios
    con = sqlite3.connect('base_usuarios.db')
    con.row_factory = sqlite3.Row
    return con


def obtener_usuarios():#obtengo todos los usuarios
    con = connect()
    c = con.cursor()
    query = """SELECT * FROM usuarios"""
    result = c.execute(query)
    usuarios = result.fetchall()
    con.close()
    return usuarios


def obt_clave(usuario):# obtengo la clave de acuerdo a cierto usuario
    con = connect()
    c = con.cursor()
    query = "SELECT password FROM usuarios WHERE user = ?"
    resultado= c.execute(query, [usuario])
    clave = resultado.fetchone()
    con.close()
    return clave

def obt_usuario(clave):# obtengo el usuario de a acuerdo a la clave
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
