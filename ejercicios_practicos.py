# Ejercicio Practico 1  ================================================================================

"""print("Hola Mundo")  # imprime "Hola Mundo" en la consola"""

# Ejercicio Practico 2  ================================================================================

""" nombre = "Juan"  # variable de tipo string
edad = 22  # variable de tipo int
altura = 1.75  # variable de tipo float
tiene_email = True  # variable de tipo booleano

CONSTANTE_PI = 3.1416  # constante (en mayuscula) de tipo float

print("1...\n2...")  # imprime un salto de linea

print(
    "Nombre:\tnombre\nEdad:\tedad"
)  # imprime "Nombre: nombre" y "Edad: edad" en la consola, con un tabulador entre ellos

print("Hola,", end="")
print(" Mundo")  # imprime "Hola, Mundo" en la consola, sin salto de linea entre ellos

print(type(nombre))  # imprime el tipo de dato de la variable nombre """

# ======================================================================================================

""" nombre = str(
    input("Ingrese nombre del cliente: ")
)  # variable de tipo string ingresada por el usuario
apellido = str(
    input("Ingrese apellido del cliente: ")
)  # variable de tipo string ingresada por el usuario
altura = float(
    input("Ingrese altura del cliente: ")
)  # variable de tipo float ingresada por el usuario
edad = int(
    input("Ingrese edad del cliente: ")
)  # variable de tipo int ingresada por el usuario
email = str(
    input("Ingrese e-mail del cliente: ")
)  # variable de tipo string ingresada por el usuario

print("DATOS DEL CLIENTE:")
print("===================================")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Edad:", edad)
print("e-mail:", email) """

# Ejercicio Practico 3 ================================================================================

""" edad = int(input("Ingrese su edad: "))

if edad >= 18:  # si la edad es mayor o igual a 18, se ejecuta el bloque de código
    print("Eres mayor de edad")
else:  # si no, se ejecuta el bloque de código
    print("Eres menor de edad") """

# ======================================================================================================

""" nombre = str(input("Ingrese nombre del cliente: "))
apellido = str(input("Ingrese apellido del cliente: "))
edad = int(input("Ingrese edad del cliente: "))
email = str(input("Ingrese e-mail del cliente: "))

print("DATOS DEL CLIENTE:")
print("===================================")

if nombre == "":
    print("ERROR!")
else:
    print("Nombre:", nombre)

if apellido == "":
    print("ERROR!")
else:
    print("Apellido:", apellido)

if edad <= 18:
    print("ERROR!")
else:
    print("Edad:", edad)

if email == "":
    print("ERROR!")
else:
    print("e-mail:", email) """

# Ejercicio Practico 4  ================================================================================

""" temperatura = float(input("Ingrese temperatura: "))

if temperatura < 0:
    print("Hace mucho frio")
elif temperatura >= 0 and temperatura < 10:
    print("Hace frio")
elif temperatura >= 10 and temperatura < 20:
    print("Hace fresco")
elif temperatura >= 20 and temperatura < 30:
    print("Hace calor")
else:
    print("Hace mucho calor")


print("--------Menu--------")
print("1. Asistencia tecnica")
print("2. Facturacion")
print("3. Soporte")
print("4. Ventas")

opcion = int(input("Ingrese una opcion: "))
print("Usted ha elegido la opcion:", opcion)

match opcion:  # estructura de control de flujo que permite evaluar una variable y ejecutar un bloque de código según su valor
    case 1:
        print("Asistencia tecnica")
    case 2:
        print("Facturacion")
    case 3:
        print("Soporte")
    case 4:
        print("Ventas")
    case _:
        print("Opcion no valida")


nombre = input("Ingrese nombre del cliente: ")

nombre = nombre.upper()  # convierte el string a mayusculas
nombre = nombre.lower()  # convierte el string a minusculas
nombre = (
    nombre.capitalize()
)  # convierte la primera letra del string a mayuscula y el resto a minusculas
nombre = (
    nombre.strip()
)  # elimina los espacios en blanco al principio y al final del string

print("Nombre:", nombre)

mensaje = "Hola Mundo"
numero = "123"

print(mensaje.startswith("Hola"))  # verifica si el string empieza con "Hola"
print(mensaje.endswith("Mundo"))  # verifica si el string termina con "Mundo"
print(mensaje.replace("Mundo", "Python"))  # reemplaza "Mundo" por "Python" en el string
print(
    mensaje.find("Mundo")
)  # busca "Mundo" en el string y devuelve la posicion donde se encuentra

print(numero.isdigit())  # verifica si el string es un numero

print(
    f"Hola {nombre.capitalize()}, bienvenido!/n eres el {numero} en la fila"
)  # imprime "Hola nombre, bienvenido!" en la consola """

# ======================================================================================================

""" nombre = str(input("Ingrese nombre del cliente: ")).capitalize()
apellido = str(input("Ingrese apellido del cliente: ")).capitalize()
edad = int(input("Ingrese edad del cliente: "))
email = str(input("Ingrese e-mail del cliente: "))

print("DATOS DEL CLIENTE:")
print("===================================")

print("Nombre:", nombre)
print("Apellido:", apellido)

if edad < 15:
    print("Niño/a")
elif (edad >= 15) and (edad < 18):
    print("Adolescente")
else:
    print("Adulto/a")

if (email.count("@") == 1) and (email.find(" ") == -1):
    print("Su e-mail es correcto")
else:
    print("Su e-mail es incorrecto") """

# Ejercicio Practico 5 ================================================================================

""" contador = 1

while contador <= 10:
    print(contador)
    contador += 1

nombre = ""

while nombre == "":
    nombre = str(input("Ingrese nombre del cliente: "))
    if nombre == "":
        print("Ingrese su nombre")
    else:
        print(f"Hola {nombre.capitalize()}, bienvenido!")

numero_secreto = 7

while True:
    numero = int(input("Ingrese un numero entre 1 y 10: "))
    if numero == numero_secreto:
        print("Ganaste!")
        break
    else:
        print("Perdiste! Intenta nuevamente")

contador = 0

while contador <= 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador, "es impar")

acumulador = 0

while True:
    numero = int(input("Ingrese un numero: "))
    acumulador += numero

    if acumulador >= 100:
        print("La suma de los numeros es mayor o igual a 100")
        break
    if numero == 0:
        print("La suma de los numeros es cero")
        break

print(f"La suma de los numeros es: {acumulador}") """

# ======================================================================================================

""" lista_strings = ["Juan", "Pedro", "Maria", "Jose", "Ana"]  # lista de strings
lista_enteros = [1, 2, 3, 4, 5]  # lista de enteros
lista_floats = [1.5, 2.5, 3.5, 4.5, 5.5]  # lista de floats
lista_booleanos = [True, False, True, False, True]  # lista de booleanos
lista_vacia = []  # lista vacia

print(lista_strings)  # imprime la lista completa
print(lista_strings[4])  # imprime el elemento en la posicion 4 de la lista
print(
    lista_strings[0:3]
)  # imprime los elementos de la lista desde la posicion 0 hasta la 3 (sin incluir la 3)
print(
    lista_strings[1:]
)  # imprime los elementos de la lista desde la posicion 1 hasta el final
print(
    lista_strings[:3]
)  # imprime los elementos de la lista desde el principio hasta la 3 (sin incluir la 3)
print(lista_strings[-1])  # imprime el ultimo elemento de la lista
print(
    lista_strings[::2]
)  # imprime los elementos de la lista desde el principio hasta el final, saltando de 2 en 2
print(len(lista_strings))  # imprime la cantidad de elementos de la lista
print(
    lista_strings.count("Juan")
)  # imprime la cantidad de veces que aparece "Juan" en la lista

i = 0

while i < len(lista_strings):
    print(lista_strings[i])
    i += 1 """

# Ejercicio Practico 6 ================================================================================

""" lista_frutas = ["manzana", "banana", "naranja", "pera", "uva"]

for i in lista_frutas:
    print(i)

lista_clientes = [
    ["Juan", "Pérez", 1],
    ["Pedro", "Gómez", 2],
    ["María", "López", 3],
    ["José", "Martínez", 4],
    ["Ana", "García", 5],
]

for cliente in lista_clientes:
    for i in range(len(cliente)):
        if i != 1:
            print(cliente[i]) """

# ======================================================================================================

""" clientes = ["juan", "pedro", "maría", "José", " ", "ANA", ""]

for i in range(len(clientes)):
    if clientes[i].strip() == "":
        print("Campo vacío")
    else:
        print(f"Cliente {i + 1} :{clientes[i].strip().capitalize()}") """

# Ejercicio Practico 7 ================================================================================

""" ingredientes = ["huevo", "leche", "harina", "azucar", "sal"]
print(ingredientes)

# "NOMBRE DE LA LISTA".index() # devuelve la posicion del primer elemento que coincida con el valor especificado
ingredientes.index("huevo")
print(ingredientes)

# "NOMBRE DE LA LISTA".append()  # agrega un elemento al final de la lista
ingredientes.append("manteca")
print(ingredientes)

# "NOMBRE DE LA LISTA".remove()  # elimina el primer elemento de la lista que coincida con el valor especificado
ingredientes.remove("sal")
print(ingredientes)

# "NOMBRE DE LA LISTA".insert()  # inserta un elemento en la lista en la posición especificada
ingredientes.insert(0, "manteca")  # inserta "manteca" al principio de la lista
print(ingredientes)

# "NOMBRE DE LA LISTA".count()  # cuenta la cantidad de veces que aparece un elemento en la lista
ingredientes.count("huevo")
print(ingredientes)

# "NOMBRE DE LA LISTA".pop()  # elimina el elemento en la posición especificada y lo devuelve
ingredientes.pop(0)
print(ingredientes)

# "NOMBRE DE LA LISTA".sort()  # ordena la lista de menor a mayor
ingredientes.sort()
print(ingredientes)

# "NOMBRE DE LA LISTA".reverse()  # invierte el orden de los elementos de la lista
ingredientes.reverse()
print(ingredientes)

# "NOMBRE DE LA LISTA".extend()  # agrega los elementos de otra lista al final de la lista
ingredientes.extend(["chocolate", "frutilla"])
print(ingredientes)

# "NOMBRE DE LA LISTA".clear()  # elimina todos los elementos de la lista
ingredientes.clear()
print(ingredientes)

ingredientes = tuple(ingredientes)  # convierte la lista en una tupla
ingredientes = list(ingredientes)  # convierte la tupla en una lista

sublista = ingredientes[0:3]  # crea una sublista con los elementos de la lista desde la posicion 0 hasta la 3 (sin incluir la 3)
print(sublista) """

""" 
del "NOMBRE DE LA LISTA"  # elimina la lista completa
del "NOMBRE DE LA LISTA"[0]  # elimina el primer elemento de la lista
del "NOMBRE DE LA LISTA"[-1]  # elimina el ultimo elemento de la lista
"""

""" ventas = []

while True:
    venta_diaria = int(input("Cuianto facturaste hoy? (INGRESE -1 PARA SALIR): "))

    if venta_diaria == -1:
        print("Fin de la carga de datos")
        break

    ventas.append(venta_diaria)

print(f"Las ventas del dia son: {ventas}")

venta_total = 0

for venta_diaria in ventas:
    venta_total += venta_diaria

print(f"La venta total es: {venta_total}") """

# ======================================================================================================

""" clientes = []

while True:
    nombre = str(input("Ingrese nombre del cliente (ingrese 'fin' para finalizar): ")).strip()
    if nombre.lower() == "fin":
        print("Fin de la carga de datos")
        break
    elif nombre == "":
        print("Campo vacío")
    else:
        clientes.append(nombre.capitalize())

clientes.sort()

print("Lista de clientes:")
for cliente in clientes:
    print(cliente) """

# Ejercicio Practico 8 ================================================================================

""" cliente = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 22,
    "signo": "Aries"
}

cliente["edad"] = "23"  # modifica el valor de la clave "nombre"
cliente["telefono"] = "123456789"  # agrega una nueva clave "telefono" con su valor

copia = cliente.copy()

cliente.pop('signo') # elimina la clave "signo" del diccionario
cliente.popitem() # elimina el ultimo elemento del diccionario
# cliente.clear()  # elimina todos los elementos del diccionario
cliente.update({"mana":1}) # actualiza el diccionario con una nueva clave "mana" y su valor 1

print(copia)

print(cliente)  # imprime el diccionario completo
print(cliente["nombre"])  # imprime el valor de la clave "nombre"
print(cliente.get("nombre"))  # imprime el valor de la clave "nombre"
print(cliente.get("nombre", "No existe"))  # imprime el valor de la clave "nombre" o "No existe" si no existe
print(cliente.keys())  # imprime las claves del diccionario
print(cliente.values())  # imprime los valores del diccionario
print(cliente.items())  # imprime las claves y valores del diccionario
print(len(cliente))  # imprime la cantidad de elementos del diccionario """

# ======================================================================================================

""" for clave, valor in cliente.items():
    print(f"{clave}: {valor}")  # imprime las claves y valores del diccionario en formato "clave: valor"

base_clientes = {
    123456: {
        "nombre": "Juan",
        "apellido": "Pérez",
        "edad": 22,
    },
    234567: {
        "nombre": "Pedro",
        "apellido": "Gómez",
        "edad": 30,
    },
    345678: {
        "nombre": "María",
        "apellido": "López",
        "edad": 25,
    }
}

base_clientes[123456]["edad"] = 20  # modifica la edad del cliente con DNI 123456

print(base_clientes[123456]["nombre"])  # imprime el nombre del cliente con DNI 123456

clientes = {}

modelo = { 
    "nombre": None,
    "apellido": None,
    "edad": None
}

while True:
    cliente = modelo.copy()

    dni = int(input("Ingresa el DNI del cliente (ingrese -1 para salir): "))

    if dni == -1:
        break

    cliente["nombre"] = input("ingrese un nombre: ")
    cliente["apellido"] = input("ingrese un apellido: ")
    cliente["edad"] = int(input("ingrese una edad: "))

    base_clientes.update({dni: cliente})

    print(f"{base_clientes}")  """

# Ejercicio Practico 9 ================================================================================
    
""" def saludo(nombre):
    print("Hola", nombre)

saludo("Jose")  # llama a la funcion saludo

def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    resultado = num1 - num2
    return resultado

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

resultado_suma = suma(num1, num2)  # llama a la funcion suma
resultado_resta = resta(num1, num2)  # llama a la funcion resta

print(resultado_suma)
print(resultado_resta) """

# ======================================================================================================

""" db_productos =[]

# Menu ===============================================================================================

def menu():

    print("\nBienvenido al sistema de gestión de productos.")
    print("Seleccione una opción:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

# Agregar Producto ===================================================================================

def agregar_producto():

    nombre = input("Ingrese el nombre del producto: ").strip()
    precio = float(input("Ingrese el precio del producto: ").strip())

    producto = [nombre, precio]
    db_productos.append(producto)

# Mostrar Productos ==================================================================================

def mostrar_productos(lista):

    for producto in lista:
        print(f"{producto[0]}\t{producto[1]}")

# Salir ==============================================================================================

def salir():

    print("Saliendo del sistema...")

# ======================================================================================================

while True:
    menu()
    opcion = input("Ingrese su opción: ")

    match opcion:
        case 1:
            agregar_producto()
        case 2:
            mostrar_productos(db_productos)
        case 3:
            buscar_producto()
        case 4:
            eliminar_producto()
        case 5:
            salir()
            break
"""

# Ejercicio Practico 10 ============================================================================

""" # funcion sin retorno
def mensaje_bienvenida(nombre):
    print("Bienvenido/a ", nombre)

# funcion con retorno
def calcular_precio_final(precio):
    impuesto = float(input("Ingrese el porcentaje de impuesto: "))
    return precio + (precio * impuesto / 100)

# funcion con varios retornos
def calcular_superficio_perimetro_rectangulo(base, altura):


    @params base: La base del rectángulo
    @params altura: La altura del rectángulo

    @return: superficie y el perímetro del rectángulo
    1. Superficie: tamaño del rectángulo (base * altura)
    2. Perímetro: tamaño del borde del rectángulo (2 * (base + altura))

    

    superficie = base * altura
    perimetro = 2 * (base + altura)
    return superficie, perimetro

superficie, perimetro = calcular_superficio_perimetro_rectangulo(5, 10)
print(f"Superficie: {superficie}, Perímetro: {perimetro}") """

# ======================================================================================================

from datetime import datetime

db_productos =[]

db_productos_vencidos =[]

# Menu ===============================================================================================

def menu():

    print("\nBienvenido al sistema de gestión de productos.")
    print("Seleccione una opción:")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

# Agregar Producto ===================================================================================

def agregar_producto():

    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    fecha = datetime.now()

    producto = [nombre, precio, fecha]
    return producto

# Mostrar Productos ==================================================================================

def mostrar_productos(lista):

    for producto in lista:
        print(f"Nombre: {producto[0]}\nPrecio: {producto[1]}\nFecha: {producto[2]}")

# Eliminar Producto ==================================================================================

def eliminar_producto(lista):

    nombre = input("Ingrese el nombre del producto a eliminar: ") 

    for index in range(len(lista)):
        if lista[index][0] == nombre:
            lista.remove(lista[index])
            print(f"Producto '{nombre}' eliminado.")
            return
    if not lista:
        print(f"Producto '{nombre}' no encontrado.")

# Buscar Producto ====================================================================================

def buscar_producto(lista):

    nombre = input("Ingrese el nombre del producto a buscar: ")

    for index in range(len(lista)):
        if lista[index][0] == nombre:
            print(f"Producto encontrado: {producto[0]}, Precio: {producto[1]}, Fecha: {producto[2]}")
            return
    print(f"Producto '{nombre}' no encontrado.")

# Salir ==============================================================================================

def salir():

    print("Saliendo del sistema...")

# ======================================================================================================

while True:
    menu()

    opcion = input("Ingrese su opción: ")

    match opcion:
        case "1":
            producto = agregar_producto()
            db_productos.append(producto)
        case "2":
            mostrar_productos(db_productos)
        case "3":
            buscar_producto(db_productos)
        case "4":
            eliminar_producto(db_productos)
        case "5":
            salir()
            break

# Ejercicio Practico 11 ============================================================================

""" def saludar(nombre: str):
    return f"Hola, {nombre}"

def suma(a: int, b: int):
    return a + b

if __name__ == "__main__":
    # Esto se ejecuta solo aca
    print(saludar("Jose"))
    print(suma(2,1)) """

# Ejercicio Practico 12 ============================================================================

