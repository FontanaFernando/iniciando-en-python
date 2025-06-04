"""
#!Requerimientos:

Ingreso de datos de productos: El sistema debe permitir ingresar datos básicos de los productos: nombre, categoría, y precio (sin centavos).
Estos datos deben almacenarse en una lista, donde cada cliente sea representado/a como una sublista de tres elementos (nombre, categoría, y precio).

Visualización de productos registrados: El programa debe incluir una funcionalidad para mostrar en pantalla todos los productos ingresados.
La información debe presentarse de manera ordenada y legible, con cada producto numerado.

Búsqueda de productos: El sistema debe permitir buscar productos por su nombre.
Si encuentra coincidencias, debe mostrar la información completa de los productos que coincidan.
Si no hay coincidencias, debe informar que no se encontraron resultados.

Eliminación de productos: El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.

#!Requisitos:

1. Usar listas para almacenar y gestionar los datos.

2. Incorporar bucles while y for según corresponda.

3. Validar entradas del usuario o usuaria, asegurándote de que no se ingresen datos vacíos o incorrectos.

4. Utilizar condicionales para gestionar las opciones del menú y las validaciones necesarias.

5. Presentar un menú que permita elegir entre las funcionalidades disponibles: agregar productos, visualizar productos, buscar productos y eliminar productos.

6. El programa debe continuar funcionando hasta que se elija una opción para salir.

"""

#Sistema de gestión de productos

""" productos = [] #lista de productos vacía """

# lista de productos con datos de ejemplo
productos = [
    {"nombre": "Laptop Gamer XYZ",
     "categoria": "Electrónica",
     "precio": 1200},
    {"nombre": "Teclado Mecánico RGB Pro",
     "categoria": "Electrónica",
     "precio": 85},
    {"nombre": "Ratón Inalámbrico Ergonómico",
     "categoria": "Electrónica",
     "precio": 40},
    {"nombre": "Monitor Curvo UltraWide",
     "categoria": "Electrónica",
     "precio": 450},
    {"nombre": "Silla Gaming Confort Plus",
     "categoria": "Muebles",
     "precio": 250},
    {"nombre": "Auriculares con Cancelación de Ruido",
     "categoria": "Audio",
     "precio": 150},
    {"nombre": "Mochila Antirrobo para Laptop",
     "categoria": "Accesorios",
     "precio": 60},
    {"nombre": "Disco Duro Externo 2TB",
     "categoria": "Almacenamiento",
     "precio": 90},
    {"nombre": "Impresora Multifunción Láser",
     "categoria": "Periféricos",
     "precio": 300},
    {"nombre": "Webcam Full HD Streamer",
     "categoria": "Periféricos",
     "precio": 75}
]


while True: # Menu de opciones
    print("\nBienvenido al sistema de gestión de productos.")
    print("Seleccione una opción:")
    print("1. Agregar producto")
    print("2. Visualizar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":  # Agregar producto
        print("\nA continuación, ingrese los datos del producto.")

        while True:
            producto = {"nombre": "", "categoria": "", "precio": 0}
            while True:
                producto["nombre"] = input("Ingrese el nombre del producto: ").strip()
                if producto["nombre"]:
                    break
                else:
                    print("El nombre no puede estar vacío.")

            while True:
                producto["categoria"] = input("Ingrese la categoría del producto: ").strip()
                if producto["categoria"]:
                    break
                else:
                    print("La categoría no puede estar vacía.")

            while True:
                precio_str = input("Ingrese el precio del producto: ")
                if precio_str.isdigit():
                    producto["precio"] = int(precio_str)
                    break
                else:
                    print("El precio debe ser un número entero y no puede estar vacío.")

            productos.append(producto)
            print(f"Producto '{producto['nombre']}' agregado exitosamente.")

            while True:
                continuar = (
                    input("¿Desea agregar otro producto? (s/n): ").strip().lower()
                )
                if continuar in ["s", "n"]:
                    break
                else:
                    print("Por favor, ingrese 's' para sí o 'n' para no.")

            if continuar != "s":
                break

    elif opcion == "2":  # Visualizar productos
        if not productos:
            print("\nNo hay productos registrados aún.")

        else:
            print("\n--- Productos Registrados ---")

            i = 0
            for producto in productos:
                print(f"{i + 1}. Nombre: {producto['nombre']}")
                print(f"   Categoría: {producto['categoria']}")
                print(f"   Precio: ${producto['precio']}")
                print("-----------------------------")
                i += 1

    elif opcion == "3":  # Buscar producto
        if not productos:
            print("\nNo hay productos para buscar.")
            continue

        nombre_buscar = (input("Ingrese el nombre del producto a buscar: ").strip().lower())
        encontrado = False
        print("\n--- Resultados de Búsqueda ---")

        i = 0
        for producto in productos:
            if nombre_buscar in producto["nombre"].lower():
                print(f"{i + 1}. Nombre: {producto['nombre']}")
                print(f"   Categoría: {producto['categoria']}")
                print(f"   Precio: ${producto['precio']}")
                print("-----------------------------")
                encontrado = True
            i += 1

        if not encontrado:
            print(f"No se encontró ningún producto con el nombre '{nombre_buscar}'.")

    elif opcion == "4":  # Eliminar producto
        if not productos:
            print("\nNo hay productos para eliminar.")
            continue

        while True:
            print("\n--- Productos Actuales ---")
            i = 0
            for producto in productos:
                print(f"{i + 1}. {producto['nombre']}")
                i += 1
            
            indice_str = input("Ingrese el número del producto a eliminar (0 para cancelar): ")
            
            if indice_str.isdigit():
                indice_eliminar = int(indice_str) - 1
                
                if indice_eliminar == -1:
                    print("Eliminación cancelada.")
                    break
                elif 0 <= indice_eliminar < len(productos):
                    producto_eliminado = productos.pop(indice_eliminar)
                    print(f"Producto '{producto_eliminado['nombre']}' eliminado exitosamente.")
                    break
                else:
                    print("Número de producto no válido. Intente de nuevo.")
            else:
                print("Entrada no válida. Por favor, ingrese un número.")

    elif opcion == "5": # Salir
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")
