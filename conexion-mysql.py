import mysql.connector

try:
    conexion =mysql.connector.connect(
        host= 'localhost',
        port = 3306,
        user = 'root',
        password = '',
        db = 'disco_app_db'
    )
    if conexion.is_connected():
        print ("Conexion exitosa!")

        informacionServidor = conexion.get_server_info()
        print ("Informacion del servidor: ", informacionServidor)

except:
        print ("Error en conexion con base de datos.")

finally:
    if conexion.is_connected():
        conexion.close()
        print ("Conexion cerrada")