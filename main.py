# Ejercicio Practico 11 ============================================================================

""" import ejercicios_practicos

mensaje = ejercicios_practicos.saludar("Carlos")
print(mensaje)

resultado = ejercicios_practicos.suma(5, 2)
print(resultado)

from ejercicios_practicos import saludar

mensaje = saludar("Pedro")
print(mensaje)

import random

print(round(random.random()*100, 2))
print(random.randint(1,10))

from datetime import datetime

ahora = datetime.now()
print(ahora)
print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.strftime("%d de %B de %Y"))

texto = "28/11/1986"
fecha = datetime.strptime(texto,"%d/%m/%Y")
print(fecha)

import colorama
colorama.init()

print(colorama.Fore.RED + "Hola" + colorama.Style.RESET_ALL)
print(colorama.Back.YELLOW + "Hola" + colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + "Hola" + colorama.Style.RESET_ALL)

input(f"{colorama.Fore.RED}Ingresa un producto: {colorama.Fore.LIGHTGREEN_EX}") """

# Ejercicio Practico 13 ============================================================================

import sqlite3

# Crea la conexion
conexion = sqlite3.connect("DataBase/baseDatos.db")
print("Conexion establecida")

#Define el cursor
cursor = conexion.cursor()

#crea la tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS baseDatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio INTERGER NOT NULL
    )
""")

# Insertar datos
#cursor.execute("""
#    INSERT INTO baseDatos (nombre, categoria, precio) VALUES (?,?,?)
#""", ("tomate","fruta",50))

# Consultar datos
#cursor.execute("SELECT * FROM baseDatos")
#baseDatos = cursor.fetchall()
#print(baseDatos)

# Actualizar datos
#nuevo_precio = 100
#id_baseDatos = 1
#cursor.execute("UPDATE baseDatos SET precio = ? WHERE id = ?", (nuevo_precio, id_baseDatos))

# Eliminar datos
#id_baseDatos = 1
#cursor.execute("DELETE FROM baseDatos WHERE id = ?" , (id_baseDatos,))

conexion.commit()
conexion.close()