#9️⃣ Manipulación de nombres
    #Pide al usuario su nombre y apellido.
nombre = input(f"Introduzca su nombre: ")
apellido = input(f"Intrpduzca su apellido: ")
    #Convierte el nombre a minúsculas y el apellido a mayúsculas.
nombre = nombre.lower()
apellido = apellido.upper()
    #Genera un alias combinando las primeras 3 letras del nombre y del apellido.
Alias = nombre[:3] + apellido[:3]
    #Muestra el alias generado.
print(Alias)
