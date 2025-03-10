import math
import random
#1️⃣ Generador de nombres de usuario
    #1 Pide al usuario su nombre y apellido.
print("A continuación, introduzca primero su nombre y luego sus apellidos: ")
nombre_de_usuario = input("Nombre: ")
apellido_de_usuario = input("Apellidos: ")
    #2 Genera un nombre de usuario en minúsculas, sin espacios.
usuario_generado = (nombre_de_usuario.lower() + apellido_de_usuario.lower()).replace(" ", "")
    #3 Añade un número aleatorio al final.
usuario_generado += str(random.randint(1,999))
    #4 Muestra el nombre de usuario generado
print("Su usuario es:",usuario_generado)
