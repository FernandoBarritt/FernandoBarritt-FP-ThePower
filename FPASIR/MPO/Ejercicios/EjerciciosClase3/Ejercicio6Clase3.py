import math
#6️⃣ Creación de mensajes personalizados
#Pide al usuario su nombre, edad y ciudad.
Nombre = input("Introduzca su nombre: ")
Edad = int(input("Introduzca su edad: "))
Ciudad = input("Introduzca su ciudad: ")
    #Muestra un mensaje con toda la información.
print("Información recogida: "
      "Nombre:",Nombre,
      "Edad:",Edad,
      "Ciudad:",Ciudad)
    #Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad.
if Edad < 18:
    nueva_edad = math.ceil(Edad/18)*18
    print("Hola", Nombre, ". Tienes", Edad, "años y vives en", Ciudad, ".La edad mínima adulta es:", nueva_edad)
else:
    print("Hola",Nombre,". Tienes",Edad,"años y vives en",Ciudad,". Cumples la edad mínima adulta.")


#No le veo el sentido al último apartado de este ejercicio Mario, iba a poner nueva_edad = 18 porque la mayoría de edad
#siempre va a ser 18. He puesto el cálculo de redondear que incluyes en las soluciones, pero es un poco raro dividir
#entre 18 y luego multiplicar por 18.

