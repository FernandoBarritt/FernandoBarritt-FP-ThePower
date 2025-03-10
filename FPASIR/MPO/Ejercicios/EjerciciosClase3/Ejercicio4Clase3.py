import random
#4️⃣Generador de etiquetas de productos
    #Pide el nombre de un producto y su precio.
nombre_de_producto = input("Introduzca el nombre del producto: ")
precio_del_producto = input("Introduzca el precio del producto: ")
precio_del_producto = float(precio_del_producto)
    #Convierte el nombre del producto a mayúsculas.
nombre_de_producto = nombre_de_producto.upper()
    #Muestra el precio con dos decimales.
print("El precio del producto, con dos decimales, es: ", format(precio_del_producto, ".2f"))
    #Genera un código basado en el valor ASCII de la primera letra del producto.
primera_letra = nombre_de_producto[0]
codigo_ASCII = ord(primera_letra) + random.randint(100000000,5000000000)
print("El código basado en el valor ASCII de la primera letra del producto es:",codigo_ASCII)


