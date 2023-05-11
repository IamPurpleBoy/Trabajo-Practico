import mysql.connector

class Conectar():

    def __init__(self) -> None:

        try:
         self.conexion =mysql.connector.connect(
            host= 'localhost',
            port = 3306,
            user = 'root',
            password = '',
            db = 'disqueria'
        )
        except mysql.connector.Error as descripcionError:
          print ("¡No se conectó!",descripcionError)

    def ListarAlbumes (self):
        if self.conexion.is_Connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT cod_album, nombre, interprete.nombre, interprete.apellido, genero.nombre, cant_temas, discografia.nombre,formato.tipo,fec_lanzamiento, precio"
                cursor.execute(sentenciaSQL)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados
            except mysql.connector.Error as descripcionError:
                print ("¡No se conectó!",descripcionError)
                
    def ListarInterprete (self):
        if self.conexion.is_Connected():
            try: 
                cursor = self.conexion.cursor()
                sentenciaSQL = "SELECT * from interprete where id_interprete = %s"
                data = (1,)
                cursor.execute (sentenciaSQL, data)
                resultados = cursor.fetchall()
                self.conexion.close()
                return resultados

            except mysql.connector.Error as descripcionError:
                print ("¡No se conectó!",descripcionError)

    def InsertarInterprete (self, nombre, apellido, nacionalidad, foto):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL = "INSERT into interprete values (null,%s,%s,%s,%s)"
                    data= (nombre, apellido, nacionalidad, foto)
                    cursor.execute(sentenciaSQL,data)
                    self.conexion.commit()
                    self.conexion.close()
                    print ("Interprete insertado correctamente ")

                except mysql.connector.Error as descripcionError:
                    print("¡No se conectó!",descripcionError)  

    def ListaTema (self):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    senenciaSQL="SELECT * from tema"
                    cursor.execute(senenciaSQL)
                    resultados = cursor.fetchall()
                    self.conexion.close()
                    return resultados

                except mysql.connector.Error as descripcionError:
                 print ("¡No se conectó!, descripcionError")


con = Conectar ()
con.InsertarInterprete ('')