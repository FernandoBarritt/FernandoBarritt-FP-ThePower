import os

def mostrar_menu():
    print("##### MENÚ PRINCIPAL #####"
          "\n 1. Listar Contenido Actual"
          "\n 2. Crear un nuevo directorio"
          "\n 3. Crear un nuevo archivo de texto"
          "\n 4. Escribir texto en un archivo existente"
          "\n 5. Eliminar un archivo o directorio"
          "\n 6. Mostrar información del archivo"
          "\n 7. Salir"
          )
    return

def listar_contenido():
    pwd = os.getcwd()
    ls = os.listdir()
    print(f"Ruta actual:\n {pwd}")
    print(f"Contenido:\n {ls}")
    return

def crear_directorio():
    while True:
        dir = input("Nombra el directorio: ").strip()
        if dir:
            try:
               os.mkdir(dir)
               print(f"Directorio {dir} creado con éxito")
               break

            #Errores de directorio ya existente o errores de sistema por incopatibilidad o permisos
            except FileExistsError:
                print(f"Error: El directorio {dir} ya existe. Prueba otro nombre")
            except OSError as e:
                print(f"Error del Sistema: \n{e}")
        else:
            print("No se detectó ningún nombre. Introduzca un nombre de dircetorio")


def crear_archivo():
    while True:
        archivo_input = input("Nombra el archivo que quieres crear:").strip()

        #Aseguramos que el archivo sea .txt
        if archivo_input.endswith(".txt"):
            archivo = archivo_input
        else:
            archivo = archivo_input + ".txt"

        #Proceso de creación de archivo
        if archivo:
            try:
               open(archivo, "x")
               print(f"Archivo {archivo} creado con éxito")
               break

            #Errores de archivo ya existente o errores de sistema por incopatibilidad o permisos
            except FileExistsError:
                print(f"Error: El archivo {archivo} ya existe. Prueba otro nombre")
            except OSError as e:
                print(f"Error del Sistema: \n{e}")
        else:
            print("No se detectó ningún nombre. Introduzca un nombre de directorio")


def escribir_archivo():
    while True:
        archivo_a_editar_input = (input("¿Qué archivo quieres editar?: ")).strip()

        if archivo_a_editar_input:
            try:
                #Buscamos donde esta el archivo exactamente
                archivo_a_editar = os.path.abspath(archivo_a_editar_input)
                #Proceso de escritura en archivo
                with open(archivo_a_editar,"a") as a:
                    a.write(input("Introduzca nuevos datos aquí:\n"))
                    print("Datos introducidos con éxito")
                break

            #Manejo de errores básicos
            except FileNotFoundError:
                print(f"No existe el archivo {archivo_a_editar_input}. Intentelo otra vez")
            except OSError as f:
                print(f"Error del Sistema: \n{f}")
        else:
            print("No se detectó ninguna entrada. Introduzca un nombre de archivo")



def main():
    seleccion = 0
    while True:
        mostrar_menu()
        try:
            seleccion =int(input("Seleccione una opción del menú: "))
            if seleccion == 1:
                listar_contenido()
            elif seleccion == 2:
                crear_directorio()
            elif seleccion == 3:
                crear_archivo()
            elif seleccion == 4:
                escribir_archivo()
            elif seleccion == 5:
                crear_directorio()
            elif seleccion == 6:
                crear_directorio()
            else:
                print("Debe ser un número entre 1 y 7, ambos inclusive")
        except ValueError:
                print("Debe ser un número")
        if seleccion == 7:
            print("Saliendo del programa...")
            break




main()