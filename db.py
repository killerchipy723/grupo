import pymysql

def db_getConnection():
    try:
        conexion = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="grupo"
        )
        print("Conexion Exitosa")
        return conexion
    except Exception as e:
        print("Error al Conectar")
        return None