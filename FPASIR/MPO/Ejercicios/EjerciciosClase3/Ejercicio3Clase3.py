import math
#3️⃣ Cálculo de descuentos
    #Pide al usuario el precio de un producto.
precio_de_producto = input("Introduzca el precio del producto: ")
precio_de_producto = float(precio_de_producto)
    #Aplica un 15% de descuento.
precio_final = precio_de_producto - (precio_de_producto * 0.15)
print("Con un 15% de descuento: ",precio_final)
    #Muestra el precio final con dos decimales.
precio_decimales = format(precio_final, ".2f")
print("El precio final a la centésima:", precio_decimales)
    #Muestra el precio redondeado hacia arriba.
precio_redondeado = math.ceil(precio_final)
print("El precio final redondeado hacia arriba:", precio_redondeado)
