# Ejercicio 4: Extracción de caracteres en una cadena
# 📌 Objetivo: Extraer partes de una cadena utilizando índices y slicing.
# Define una cadena con una palabra o nombre.
cadena = input("Introduzca una palabra:")
# Extrae y muestra los tres primeros caracteres.
print("Las tres primeras letras son:",cadena[:3])
# Extrae y muestra los tres últimos caracteres.
print("Las tres últimas letras son:",cadena[-3:])
# Extrae los caracteres en posiciones impares de la cadena.
print("Los caracteres en posiciones impares son: ", cadena[1::2])
