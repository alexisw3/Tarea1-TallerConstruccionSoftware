# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('base_productos.db')
c = conn.cursor()

#creo tabla marcas
c.execute("""CREATE TABLE marcas (id_marca integer primary key AUTOINCREMENT,
                                nombre text, descripcion text, pais text)""")

#creo tabla de productos que va asociada con la de marcas
#o sea una marca tiene varios productos, relacion 1 marca N productos
c.execute("""CREATE TABLE productos (codigo integer primary key AUTOINCREMENT, nombre text, descripcion text,
                                        color text, precio integer, fk_id_marca int,
                                        FOREIGN KEY (fk_id_marca) REFERENCES marcas (id_marca))""")

#agrego distintas marcas a su respectiva tabla
c.execute("""INSERT INTO marcas (nombre, descripcion, pais)
                                VALUES("Nike", "deportes", "USA")""")
c.execute("""INSERT INTO marcas (nombre, descripcion, pais)
                                VALUES("Reebok", "deportes", "USA")""")
c.execute("""INSERT INTO marcas (nombre, descripcion, pais)
                                VALUES("Apple", "tecnologia", "USA")""")
c.execute("""INSERT INTO marcas (nombre, descripcion, pais)
                                VALUES("Samsung", "tecnologia", "COREA DEL SUR")""")
c.execute("""INSERT INTO marcas (nombre, descripcion, pais)
                                VALUES("Microsoft", "tecnologia", "USA")""")

#agrego distintos productos a su respectiva tabla

c.execute("""INSERT INTO productos VALUES(3015, "iPhone 5s", "smartphone","plata","400000", 3)""")
c.execute("""INSERT INTO productos VALUES(3316, "iPhone 4", "smartphone","negro","100000", 3)""")
c.execute("""INSERT INTO productos VALUES(2214, "Running", "calzado","azul","30000", 2)""")
c.execute("""INSERT INTO productos VALUES(4214, "SmartTv 6", "Television","negro","200000", 4)""")
c.execute("""INSERT INTO productos VALUES(5642, "Microsoft Office 2013", "software","verde","30000", 5)""")
c.execute("""INSERT INTO productos VALUES(5234, "Windows 7", "software","azul","150000", 5)""")
c.execute("""INSERT INTO productos VALUES(1222, "Lebron IV", "calzado","verde","40000", 1)""")
c.execute("""INSERT INTO productos VALUES(2125, "Polera", "vestuario","amarillo","9000", 2)""")
c.execute("""INSERT INTO productos VALUES(4647, "Automatica", "lavadora","blanco","150000", 4)""")
c.execute("""INSERT INTO productos VALUES(4356, "Galaxy S5", "smartphone","azul","400000", 4)""")
c.execute("""INSERT INTO productos VALUES(5356, "Windows 8", "software","rojo","200000", 5)""")
c.execute("""INSERT INTO productos VALUES(2567, "Poleron", "vestuario","cafe","19000", 2)""")
c.execute("""INSERT INTO productos VALUES(1245, "Poleron", "vestuario","amarillo","20000", 1)""")
c.execute("""INSERT INTO productos VALUES(1211, "Short", "vestuario","negro","10000", 1)""")
c.execute("""INSERT INTO productos VALUES(1535 , "Hyperdunk", "calzado","rojo","45000", 1)""")
c.execute("""INSERT INTO productos VALUES(3212, "iPad", "smartphone","blanco","220000", 3)""")
c.execute("""INSERT INTO productos VALUES(2555, "Short", "vestuario","blanco","20000", 2)""")
c.execute("""INSERT INTO productos VALUES(4678, "Notebook pro", "computacion","azul","300000", 4)""")
c.execute("""INSERT INTO productos VALUES(5888, "Windows XP", "smartphone","plata","40000", 5)""")
c.execute("""INSERT INTO productos VALUES(3875, "Macbook air", "computacion","gris","500000", 3)""")


conn.commit()
c.close()

