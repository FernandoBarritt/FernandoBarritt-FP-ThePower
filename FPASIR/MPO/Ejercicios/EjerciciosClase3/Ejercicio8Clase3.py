#8️⃣ Verificación de nombres en listas
    #Pide al usuario su nombre.
nombre = input("Introduzca su nombre: ")
    #Verifica si su nombre está en una lista de invitados predefinida.
    # #Si está en la lista, muestra su posición.
lista_nombres = ["Alejandro", "Beatriz", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", "Ignacio", "Lucía"]
if nombre in lista_nombres:
    print("Su nombre está en la lista, en la posición", (lista_nombres.index(nombre)+1))
else:
    print("Su nombre no está en la lista")

