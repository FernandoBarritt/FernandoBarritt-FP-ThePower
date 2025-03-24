# Ejercicio 5: Conversión de tipos y evaluación booleana
# 📌 Objetivo: Convertir entre tipos básicos y analizar valores booleanos.
# Convierte un número en una cadena y muestra el tipo de dato.
while True:
    try:
        num = int(input("Introduzca un número: "))
        print("El tipo de variable es: ",type(num))
        #también podría poner literalmente print("El tipo de variable es int") porque el while me asegura que va a ser int
        break
    except ValueError:
        print("Eso no es un número, no es tan complicado por Dios. Intentalo otra vez")

str_num = str(num)
print("Ahora el tipo de variable es: ", type(str_num))
# Convierte una cadena numérica en un número entero y muestra el tipo.

# Convierte diferentes valores ("", "Texto", 0, 1, -1, None) a booleanos y muestra los resultados.