import sqlite3
import os

# Asegura que el directorio DataBase exista
def asegurar_directorio_db():
    """
    Asegura que el directorio 'DataBase' exista.
    """
    db_dir = "DataBase"
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
        print(f"Directorio '{db_dir}' creado.")

def crear_base_datos():
    """
    Crea la tabla 'inventario' si no existe.
    Maneja errores de conexión y ejecución de la base de datos.
    """
    asegurar_directorio_db()
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        )
        """)
        conexion.commit()
        print("Base de datos 'inventario.db' y tabla 'inventario' creadas o ya existentes.")
    except sqlite3.Error as e:
        print(f"Error al crear la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()

def agregar():
    """
    Permite al usuario agregar un nuevo producto al inventario.
    Maneja errores de entrada de usuario y de base de datos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        
        # Validación de entrada para cantidad y precio
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                return
        except ValueError:
            print("Cantidad inválida. Por favor, ingrese un número entero.")
            return

        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
                return
        except ValueError:
            print("Precio inválido. Por favor, ingrese un número.")
            return
            
        categoria = input("Ingrese la categoría del producto: ")

        cursor.execute("INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto agregado exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al agregar el producto: {e}")
    finally:
        if conexion:
            conexion.close()

def mostrar_inventario():
    """
    Muestra todos los productos en el inventario.
    Maneja errores de conexión a la base de datos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        cursor.execute("SELECT * FROM inventario")
        productos = cursor.fetchall()

        if productos:
            print("\n--- Inventario Actual ---")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]:.2f}, Categoría: {producto[5]}")
        else:
            print("El inventario está vacío.")
    except sqlite3.Error as e:
        print(f"Error al mostrar el inventario: {e}")
    finally:
        if conexion:
            conexion.close()

def buscar():
    """
    Busca productos en el inventario por ID, nombre o categoría.
    Maneja errores de entrada de usuario y de base de datos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        id_producto = input("Ingrese el ID del producto a buscar (opcional, presione Enter para omitir): ")
        nombre_producto = input("Ingrese el nombre del producto a buscar (opcional, presione Enter para omitir): ")
        categoria = input("Ingrese la categoría del producto a buscar (opcional, presione Enter para omitir): ")

        query = "SELECT * FROM inventario WHERE 1=1"
        params = []

        if id_producto.strip():
            try:
                query += " AND id = ?"
                params.append(int(id_producto))
            except ValueError:
                print("ID inválido. Por favor, ingrese un número entero para el ID.")
                return
        if nombre_producto.strip():
            query += " AND nombre LIKE ?"
            params.append('%' + nombre_producto + '%')
        if categoria.strip():
            query += " AND categoria LIKE ?"
            params.append('%' + categoria + '%')

        cursor.execute(query, params)
        productos = cursor.fetchall()

        if productos:
            print("\n--- Productos Encontrados ---")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]:.2f}, Categoría: {producto[5]}")
        else:
            print("No se encontraron productos con esos criterios.")
    except sqlite3.Error as e:
        print(f"Error al buscar productos: {e}")
    finally:
        if conexion:
            conexion.close()

def actualizar():
    """
    Actualiza el precio de un producto existente.
    Maneja errores de entrada de usuario y de base de datos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        try:
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        except ValueError:
            print("ID inválido. Por favor, ingrese un número entero.")
            return

        cursor.execute("SELECT id FROM inventario WHERE id = ?", (id_producto,))
        if cursor.fetchone() is None:
            print(f"No se encontró ningún producto con el ID {id_producto}.")
            return

        try:
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            if nuevo_precio < 0:
                print("El precio no puede ser negativo. Intente de nuevo.")
                return
        except ValueError:
            print("Precio inválido. Por favor, ingrese un número.")
            return

        cursor.execute("UPDATE inventario SET precio = ? WHERE id = ?", (nuevo_precio, id_producto))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"Producto con ID {id_producto} actualizado exitosamente.")
        else:
            print(f"No se pudo actualizar el producto con ID {id_producto}.")
    except sqlite3.Error as e:
        print(f"Error al actualizar el producto: {e}")
    finally:
        if conexion:
            conexion.close()

def eliminar():
    """
    Elimina un producto del inventario por su ID.
    Maneja errores de entrada de usuario y de base de datos.
    """
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        try:
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        except ValueError:
            print("ID inválido. Por favor, ingrese un número entero.")
            return

        cursor.execute("DELETE FROM inventario WHERE id = ?", (id_producto,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print(f"No se encontró ningún producto con el ID {id_producto}.")
    except sqlite3.Error as e:
        print(f"Error al eliminar el producto: {e}")
    finally:
        if conexion:
            conexion.close()

def reporte_inventario():
    """
    Genera un reporte de productos con una cantidad igual o inferior a un límite especificado.
    """
    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        try:
            limite_cantidad = int(input("Ingrese el límite de cantidad para el reporte: "))
            if limite_cantidad < 0:
                print("El límite de cantidad no puede ser negativo. Intente de nuevo.")
                return
        except ValueError:
            print("Límite de cantidad inválido. Por favor, ingrese un número entero.")
            return

        cursor.execute("SELECT * FROM inventario WHERE cantidad <= ?", (limite_cantidad,))
        productos_bajo_limite = cursor.fetchall()

        if productos_bajo_limite:
            print(f"\n--- Reporte de Productos con Cantidad <= {limite_cantidad} ---")
            for producto in productos_bajo_limite:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]:.2f}, Categoría: {producto[5]}")
        else:
            print(f"No se encontraron productos con una cantidad igual o inferior a {limite_cantidad}.")
    except sqlite3.Error as e:
        print(f"Error al generar el reporte de inventario: {e}")
    finally:
        if conexion:
            conexion.close()

def insertar_productos_ejemplo():
    """
    Inserta una lista predefinida de productos en la base de datos.
    """
    productos_ejemplo = [
        ('Laptop "UltraBook"', 'Portátil ligero y potente', 15, 1200.00, 'Electrónica'),
        ('Teclado Mecánico', 'Teclado con switches Cherry MX', 50, 85.50, 'Electrónica'),
        ('Ratón Inalámbrico', 'Ratón ergonómico con batería de larga duración', 100, 25.99, 'Electrónica'),
        ('Monitor Curvo 27"', 'Monitor de alta resolución para gaming', 10, 350.00, 'Electrónica'),
        ('Auriculares Bluetooth', 'Auriculares con cancelación de ruido', 75, 120.00, 'Electrónica'),
        ('Silla Ergonómica', 'Silla de oficina con soporte lumbar', 20, 180.00, 'Muebles'),
        ('Escritorio Ajustable', 'Escritorio de altura regulable', 12, 250.00, 'Muebles'),
        ('Impresora Multifunción', 'Impresora, escáner y copiadora', 8, 150.00, 'Oficina'),
        ('Resma de Papel A4', 'Paquete de 500 hojas de papel', 200, 5.75, 'Oficina'),
        ('Bolígrafos Azules', 'Caja de 12 bolígrafos de tinta azul', 300, 8.99, 'Oficina')
    ]

    conexion = None
    try:
        conexion = sqlite3.connect("DataBase/inventario.db")
        cursor = conexion.cursor()

        for producto in productos_ejemplo:
            cursor.execute("INSERT INTO inventario (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", producto)
        
        conexion.commit()
        print(f"{len(productos_ejemplo)} productos de ejemplo insertados exitosamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar productos de ejemplo: {e}")
    finally:
        if conexion:
            conexion.close()

def menu():
    """
    Muestra el menú principal y maneja la interacción con el usuario.
    """
    ejecutando = True
    while ejecutando:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar todo el inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Reporte de inventario (Ingrese límite de cantidad)")
        # print("7. Insertar productos de ejemplo (10 productos)") # Agregar si se desea insertar productos de ejemplo
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar()
        elif opcion == "4":
            actualizar()
        elif opcion == "5":
            eliminar()
        elif opcion == "6":
            reporte_inventario()
        # elif opcion == "7": # Añadir opción para insertar productos de ejemplo
            # insertar_productos_ejemplo()
        elif opcion == "0":
            print("Saliendo del programa...")
            ejecutando = False
        else:
            print("Opción no válida, intente nuevamente.")

# Punto de entrada del programa
if __name__ == "__main__":
    crear_base_datos()
    menu()