from client import Client
import psycopg2

class Llibreta:

    try:
        conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
        cur = conn.cursor()
        print("Exercici 1:")
        cur.execute("DROP TABLE IF EXISTS cliente")
        command = (
            "CREATE TABLE cliente (cliente_id VARCHAR(199), cliente_name VARCHAR(255), cliente_cognom VARCHAR(255), cliente_telefon VARCHAR(255), cliente_correu VARCHAR(255), cliente_adreca VARCHAR(255), cliente_ciutat VARCHAR(255))")
        cur.execute(command)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


    llista_clients = []
    id_client = 0

    def __init__(self, llista_clients, id_client):
        self.id_client = id_client
        self.llista_clients = llista_clients


    def get_llista_clients(self):
        for i in self.llista_clients:
            print(i.__str__())

    def afegir_client(self,nom,cognom,telefon,correu,adreca,ciutat):

        client = Client(self.id_client, nom, cognom, telefon, correu, adreca, ciutat)
        self.id_client += 1
        # self.llista_clients.append(client)
        print(client.__str__())
        # insertar cliente en la tabla de Bddemo:

        try:
            conn = psycopg2.connect("dbname='Bddemo' user='odoo' host='172.17.0.1'password='odoo'")
            cur = conn.cursor()
            cur.execute("INSERT INTO cliente(cliente_id,cliente_name,cliente_cognom,cliente_telefon,cliente_correu,cliente_adreca,cliente_ciutat) VALUES(%s,%s,%s,%s,%s,%s,%s);",self.id_client,nom,cognom,telefon,correu,adreca,ciutat)

            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()




    def eliminar_client(self, id):
        found = False
        for i in self.llista_clients:
            if id == i.identificador:
                print("Eliminado:\n", i.__str__())
                self.llista_clients.remove(i)
                found = True

        if not found: print("Cliente no encontrado en la lista")

    def cercar_per_id(self, id):
        primero = []
        #primero = self.llista_clients.get()
        for i in self.llista_clients:
            if id== i.identificador:
                primero.append(i)
                return primero
        print("Cliente no encontrado con ese identificador")
        return None
    def cercar_per_nom(self, nom):
        list =[]
        for i in self.llista_clients:
            if nom == i.nom:
                list.append(i)

        return list

    def cercar_per_cognom(self, cognom):
        list = []
        for i in self.llista_clients:
            if cognom == i.cognom:
                list.append(i)

        return list
