#2️⃣Analizador de frases
#Pide al usuario que ingrese una frase.
frase = input("Ingrese una frase: ")
#Muestra la cantidad de caracteres de la frase.
print("Cantidad de caracteres", len(frase))
#Indica si la frase contiene la palabra "Python".
print("python" in frase.lower())
#Convierte la frase a mayúsculas.
print(frase.upper())
#Muestra la frase invertida.
frase_invertida = frase[::-1]
print(frase_invertida)