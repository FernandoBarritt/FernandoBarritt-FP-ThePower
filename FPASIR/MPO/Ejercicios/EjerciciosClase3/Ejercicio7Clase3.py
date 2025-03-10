import random
import string
#7️⃣ Generador de contraseñas aleatorias
    #Pide al usuario su nombre.
nombre = input("Ingrese su nombre: ")
    #Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
letras = random.choice(string.ascii_letters)
números = random.randint(80000,10000000)
simb_especial = random.choice(string.punctuation)
contraseña = letras.upper() + str(números) + simb_especial
    #Muestra la contraseña generada.
print("Hola",nombre,", tu contraseña segura es:", contraseña)