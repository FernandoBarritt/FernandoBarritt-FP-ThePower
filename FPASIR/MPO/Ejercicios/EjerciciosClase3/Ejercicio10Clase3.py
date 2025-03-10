#🔟 Formatear y mostrar datos matemáticos
import math
#Pide al usuario un número decimal.
numero = float(input("Introduzca un número decimal: "))
#Muestra el número redondeado a dos decimales.
numero_redondeado = round(numero,2)
print("El número redondeado a dos decimales es:",numero_redondeado)
#Calcula y muestra su cuadrado.
cuadrado = numero **2
print("El número al cuadrado es:",cuadrado)
#Calcula y muestra su raíz cuadrada.
raiz = numero **0.5
print("La raíz cuadrada del número es",raiz)

