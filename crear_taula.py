import psycopg2

# def create_table():
#     """ create tables in the PostgreSQL database"""
#     commands = (
#         """
#         CREATE TABLE vendors (
#             vendor_id SERIAL PRIMARY KEY,
#             vendor_name VARCHAR(255) NOT NULL
#         )
#         """,
#         """ CREATE TABLE parts (
#                 part_id SERIAL PRIMARY KEY,
#                 part_name VARCHAR(255) NOT NULL
#                 )
#         """,
#         """
#         CREATE TABLE part_drawings (
#                 part_id INTEGER PRIMARY KEY,
#                 file_extension VARCHAR(5) NOT NULL,
#                 drawing_data BYTEA NOT NULL,
#                 FOREIGN KEY (part_id)
#                 REFERENCES parts (part_id)
#                 ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """,
#         """
#         CREATE TABLE vendor_parts (
#                 vendor_id INTEGER NOT NULL,
#                 part_id INTEGER NOT NULL,
#                 PRIMARY KEY (vendor_id , part_id),
#                 FOREIGN KEY (vendor_id)
#                     REFERENCES vendors (vendor_id)
#                     ON UPDATE CASCADE ON DELETE CASCADE,
#                 FOREIGN KEY (part_id)
#                     REFERENCES parts (part_id)
#                     ON UPDATE CASCADE ON DELETE CASCADE
#         )
#         """)
#     conn = None
#     try:
#         # read the connection parameters
#         params = config()
#         # connect to the PostgreSQL server
#         conn = psycopg2.connect(**params)
#         cur = conn.cursor()
#         # create table one by one
#         for command in commands:
#             cur.execute(command)
#         # close communication with the PostgreSQL database server
#         cur.close()
#         # commit the changes
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#
# create_table()

#!/usr/bin/python

import psycopg2
from config import config


def insert_vendor(vendor_name):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO vendors(vendor_name)
             VALUES(%s) RETURNING vendor_id;"""
    conn = None
    vendor_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (vendor_name,))
        # get the generated id back
        vendor_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return vendor_id

def insert_cliente(id, nom, cognom, telefon, correu, adreca, ciudad):
    """ insert a new vendor into the vendors table """
    cur.execute("INSERT INTO cliente(cliente_id,cliente_name,cliente_cognom,cliente_telefon,cliente_correu,cliente_adreca,cliente_ciutat) VALUES(%s,%s,%s,%s,%s,%s,%s);")

try:
    conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
    cur = conn.cursor()
    print("Exercici 1:")
    cur.execute("DROP TABLE IF EXISTS cliente")
    command = ("CREATE TABLE cliente (cliente_id VARCHAR(199), cliente_name VARCHAR(255), cliente_cognom VARCHAR(255), cliente_telefon VARCHAR(255), cliente_correu VARCHAR(255), cliente_adreca VARCHAR(255), cliente_ciutat VARCHAR(255))")
    cur.execute(command)
    cur.execute(sql, insert_cliente(cliente_id,cliente_name,cliente_cognom,cliente_telefon,cliente_correu,cliente_adreca,cliente_ciutat))
    #modificar


    conn.commit()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()


#1.Creeuunnoumòdulcrear_taula.pyques’encarreguidecrearlataulaaunabasededades.
# 2.Modifiqueuelsmètodes/funcionsquerealitzenoperacionssobreelsclientsperquèaccedeixin a la taula i no a la llista.


# 3. Feu servir Commits i Rollbacks en cas necessari per garantir la integritat de les dades.
# 4. Feu servir noms de funcions, mètodes i de variables que siguin descriptius.
# 5. Procureu que el codi sigui clar i ben estructurat.