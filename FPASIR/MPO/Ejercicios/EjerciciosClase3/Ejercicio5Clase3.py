#5️⃣ Conversión de tipos y manipulación de listas
    #Pide al usuario una lista de números separados por comas.
input_numeros = (input("Introduzca una lista de números separadas por comas: "))
    #Convierte cada número a entero.
lista_numeros = list(map(int,input_numeros.split(",")))
    #Elimina los números repetidos.
sin_repetidos = set(lista_numeros)
sin_repetidos_ordenados = sorted(sin_repetidos)
    #Muestra la lista ordenada sin duplicados.
print(sin_repetidos_ordenados)

