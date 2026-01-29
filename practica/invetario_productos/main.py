from dataBase import DataBaseInventario


print("Bienvenido a la Mini-tiendita")
while(1):   
    print("////////MENU DE OPCIONES////////")
    print("1.-Crear tabla")
    print("2.-Agrega productos a la tabla")
    print("3.-Consultar datos")
    print("4.-Eliminar datos")
    print("5.-Cerrar conexion")
    opcion = input("Escriba un numero del menu para realizar una tarea: ")
    
    
    match opcion: 
        case 1:
            nombre_tabla = input("Escriba el nombre de la tabla")
            db = DataBaseInventario(nombre_tabla)
            db.crear_tabla
            
        case 2:
            nombre_tabla = input("Escriba el nombre de la tabla")
            producto = input("Escribe el nombre del producto")
            precio = float(input("Escribe el precio del producto"))
            cantidad = int(input("Escribe la cantidad que hay de ese producto"))
            db = DataBaseInventario(nombre_tabla)
            db.insertar_datos(producto, precio, cantidad)
            
        case 3:
            nombre_tabla = input("Escriba el nombre de la tabla")
            db = DataBaseInventario(nombre_tabla)
            datos = db.consultar_datos()
            for row in datos:
                print(row)
            
        case 4:
            nombre_tabla = input("Escriba el nombre de la tabla")
            producto = input("Escribe el nombre del producto")
            db = DataBaseInventario(nombre_tabla)
            db.elimininar_datos(producto)
            
        case 5:
            db = DataBaseInventario("temp")
            db.cerrar_conexion()
            break
        case _:
            print("Opcion incorrecta. Seleccione una opcion del menu. ")
            