import sqlite3

class DataBaseInventario:
    
    def __init__(self,nombre_tabla, nombre, precio, cantidad):
        self.nombre_tabla = nombre_tabla
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        conexion = sqlite3.connect("productos.db")
        cursor = conexion.cursor()
        
    #----------------------Funcion para crear una tabla
    def crear_tabla(self,nombre_tabla,cursor, conexion):    
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {nombre_tabla}  (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NO NULL,
                precio DECIMAL,
                cantidad INTEGER
            )    
            """
        )
        conexion.commit()

    #--------------------Funcion para insertar datos a una tabla
    def insertar_datos(cursor,nombre_tabla, nombre , precio, cantidad):
        cursor.execute(
            f"INSERT INTO {nombre_tabla} ({nombre}, {precio}, {cantidad}) VALUES (?,?,?)"
        )
        
    #------------------------Funcion para consultar una tabla
    def consultar_datos(cursor,nombre_tabla):
        cursor.execute(
            f"SELECT * FROM {nombre_tabla} "
        )
            
    def elimininar_datos(cursor, nombre_tabla,nombre):
        cursor.execute(
            f"DELETE FROM {nombre_tabla} WHERE {nombre}"
        )
        
    def cerrar_conexion(conexion):
        conexion.close()
    