# Ejercicio 2: Propiedades y manipulación de cadenas
# 📌 Objetivo: Trabajar con cadenas y métodos integrados de Python.
# Crea una cadena con una frase corta.
from itertools import count

frase_corta = "Me gustan las patatas"
# Muestra cuántos caracteres tiene la cadena.
print(len(frase_corta))
# Convierte toda la cadena a mayúsculas y minúsculas.
print("Frase en mayúscula:",frase_corta.upper())
print("Frase en minúscula:",frase_corta.lower())
# Cuenta cuántas veces aparece una letra específica en la cadena.
letra = input("¿Qué letra quieres contar?:")
print(frase_corta.count(letra))
