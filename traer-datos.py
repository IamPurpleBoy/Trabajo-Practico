import mysql.connector

try:
    conexion = mysql.connector.connect(
        host= '127.0.0.1',
        port = 3306,
        user = 'root',
        password = '',
        db = 'disco_app_db'
    )
    if conexion.is_connected():
        print ("Conexion exitosa!")

        cursor = conexion.cursor()
        cursor.execute("SELECT * from interprete")
        lista = cursor.fetchall()
        
        for dato in lista:
            print (dato)

except mysql.connector.Error as ex:
        print ("Error en conexion con base de datos. Motivo: ",ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print ("Conexion cerrada")