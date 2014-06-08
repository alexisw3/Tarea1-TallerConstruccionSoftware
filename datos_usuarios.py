# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('base_usuarios.db')
c = conn.cursor()

#creo tabla usuarios
c.execute("""CREATE TABLE usuarios (id integer primary key AUTOINCREMENT,
                                nombre text, user text, password text)""")


#agrego usuarios a la tabla
c.execute("""INSERT INTO usuarios (nombre, user, password)
                                VALUES("Alexis Garcia", "alexisw3", "pajarito1")""")
c.execute("""INSERT INTO usuarios (nombre, user, password)
                                VALUES("Yarithza Bustos", "yarithza", "pajarito2")""")
c.execute("""INSERT INTO usuarios (nombre, user, password)
                                VALUES("Cristian Rojas", "crrojas", "pajarito3")""")


conn.commit()
c.close()
