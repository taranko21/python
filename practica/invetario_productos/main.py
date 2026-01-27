from dataBase import DataBaseInventario


nombre_tabla = input("Escriba el nombre de la tabla")
producto = input("Escribe el nombre del producto")
precio = input("Escribe el precio del producto")
cantidad = input("Escribe la cantidad que hay de ese producto")

print("Bienvenido a la Mini-tiendita")
while(1):   
    print("////////MENU DE OPCIONES////////")
    print("1.-Crear tabla")
    print("2.-Agrega productos a la tabla")
    print("3.-Consultar datos")
    print("4.-Eliminar datos")
    print("6.-Cerrar conexion")
    print("7.-Break")
    opcion = input("Escriba un numero del menu para realizar una tarea")
    
    
    match opcion: 
        case 1:
            nombre_tabla = input("Escriba el nombre de la tabla")
            producto = input("Escribe el nombre del producto")
            precio = input("Escribe el precio del producto")
            cantidad = input("Escribe la cantidad que hay de ese producto")
            db = DataBaseInventario(nombre_tabla,producto, precio, cantidad)
            db.crear_tabla
            
        case 2:
            nombre_tabla = input("Escriba el nombre de la tabla")
            producto = input("Escribe el nombre del producto")
            precio = input("Escribe el precio del producto")
            cantidad = input("Escribe la cantidad que hay de ese producto")
            db = DataBaseInventario(nombre_tabla, producto,precio, cantidad)
            db.insertar_datos
            
        case 3:
            nombre_tabla = input("Escriba el nombre de la tabla")
            db = DataBaseInventario(nombre_tabla)
            db.consultar_datos
            
        case 4:
            nombre_tabla = input("Escriba el nombre de la tabla")
            producto = input("Escribe el nombre del producto")
            db = DataBaseInventario(nombre_tabla, producto)
            db.elimininar_datos
            
        case 5:
            db = DataBaseInventario()
            db.elimininar_datos