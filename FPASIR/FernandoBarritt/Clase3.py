nombre = "Fernando"
#print("Longitud del nombre: " , len(nombre))

#2. Upper y Lower para convertir de minúsculas y mayúsculas
#print("Quiero tener mi nombre en mayúsculas: ", nombre.upper())
#print("Quiero tener mi nombre en mayúsculas: ", nombre.lower())

#3. Slicing. Extraer partes de una cadena o String
    #Los tres primeros caracteres de mi nombre desde el principio
#print("Los primeros tres caracteres de mi nombre: ", nombre[:3])

    #Los cuatro primeros caracteres de mi nombre desde el principio
#print("Los últimos 4 caracteres de mi nombre: ", nombre[-4:])

#4. Reemplazar palabras en un string
frase = "Me encanta Java"
#print("Quiero cambiar una palabra", frase.replace("Java", "Python"))

#5. Verificar si una cadena tiene o contiene a otra
print("Python" in frase) #False
nueva_frase = "Me encanta Python"
print("Python" in nueva_frase) #True
