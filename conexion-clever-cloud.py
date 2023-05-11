import mysql.connector

try:
    conexion =mysql.connector.connect(
        host = "bxxc0tkhaeyzswnmqrgd-mysql.services.clever-cloud.com",
        user = "uj0iv2ccqtlaeb23",
        passwd = "x9ckzcWrjhrauD6wpoM1",
        database = "bxxc0tkhaeyzswnmqrgd"
)
    if conexion.is_connected():
        print("La conexion fue exitosa.")
    
        informacionServidor = conexion.get_server_info()
        print ("Detalle de conexion: ", conexion) 
        print ("Informacion del servidor: ", informacionServidor)
        cursor = conexion.cursor()
        #cursor.execute("CREATE TABLE  tema (id_tema int not null auto_increment primary key, titulo varchar(100), duracion time,autor varchar(100) not null, compositor varchar(100) not null, id_album int, id_interprete int, foreign key(id_album) references album(id_album), foreign key(id_interprete) references interprete(id_interprete))")
        #print ( "Tu CREATE TABLE  fue exitoso!")
except:
        print ("Error en conexion con base de datos.")

finally:
    if conexion.is_connected():
        conexion.close()
        print ("Conexion cerrada")