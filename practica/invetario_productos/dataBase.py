import sqlite3


class DataBaseInventario: 
    
    
    def __init__(self,nombre_tabla, nombre=None, precio = None, cantidad = None):
        self.nombre_tabla = nombre_tabla
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.conexion = sqlite3.connect("productos.db")
        self.cursor = self.conexion.cursor()
        
    #----------------------Funcion para crear una tabla
    def crear_tabla(self):    
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.nombre_tabla}  (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NO NULL,
                precio DECIMAL,
                cantidad INTEGER
            )    
            """
        )
        self.conexion.commit()

    #--------------------Funcion para insertar datos a una tabla
    def insertar_datos(self, nombre,precio,cantidad):
        self.cursor.execute(
            f"INSERT INTO {self.nombre_tabla} (nombre,precio,cantidad) VALUES (?,?,?)",
            (nombre,precio,cantidad)
        )
        self.conexion.commit()
        
    #------------------------Funcion para consultar datos de una tabla
    def consultar_datos(self):
        self.cursor.execute(
            f"SELECT * FROM {self.nombre_tabla} "
        )
        rows =self.cursor.fetchall()
        return rows
        
    #------------------------Funcion para eliminar datos de una tabla            
    def elimininar_datos(self,nombre):
        self.cursor.execute(
            f"DELETE FROM {self.nombre_tabla} WHERE nombre = {self.nombre}"
        )
        self.conexion.commit()
        
    #------------------------Funcion para cerrar conexion de una database
    def cerrar_conexion(self):
        self.conexion.close()
    