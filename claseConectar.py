import mysql.connector

class conectar ():

    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "root",
                password = "root",
                db = "disqueria"
            )

        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!", descripcionError)

    def ListarAlbumes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM album")
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
                 

            except mysql.connector.Error as descripcionError:
                print("¡No se conectó!", descripcionError) 

#Listado de álbumes disponibles por artista, en orden alfabético.

con = conectar()

for album in con.ListarAlbumes():
    print(album)
 
                    

