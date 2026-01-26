import sqlite3


conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()


class DataBaseInventario: 
    
    
    def __init__(self,nombre_tabla, nombre, precio, cantidad):
        self.nombre_tabla = nombre_tabla
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
       
        
    #----------------------Funcion para crear una tabla
    def crear_tabla(self):    
        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.nombre_tabla}  (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                {self.nombre} TEXT NO NULL,
                {self.precio} DECIMAL,
                {self.cantidad} INTEGER
            )    
            """
        )
        conexion.commit()

    #--------------------Funcion para insertar datos a una tabla
    def insertar_datos(self):
        cursor.execute(
            f"INSERT INTO {self.nombre_tabla} ({self.nombre}, {self.precio}, {self.cantidad}) VALUES (?,?,?)"
        )
        
    #------------------------Funcion para consultar una tabla
    def consultar_datos(self):
        cursor.execute(
            f"SELECT * FROM {self.nombre_tabla} "
        )
            
    def elimininar_datos(self):
        cursor.execute(
            f"DELETE FROM {self.nombre_tabla} WHERE {self.nombre}"
        )
        
    def cerrar_conexion(self):
        conexion.close()
    