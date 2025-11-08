import os
import datetime
import math
import shutil


def obtener_tamanio_legible(bytes, suffix="B"):
    """
    Convierte un número de bytes a un formato legible (KB, MB, GB, etc.).
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f} {unit}{suffix}"
        bytes /= factor

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    current_path = os.getcwd()
    print("-" * (len(current_path) + 20))
    print(f"--- RUTA ACTUAL: {current_path} ---")
    print("-" * (len(current_path) + 20))
    print("##### MENÚ PRINCIPAL #####"
          "\n 1. Listar Contenido Actual"
          "\n 2. Crear un nuevo directorio"
          "\n 3. Crear un nuevo archivo de texto"
          "\n 4. Escribir texto en un archivo existente"
          "\n 5. Eliminar un archivo o directorio"
          "\n 6. Mostrar información detallada de archivo"
          "\n 7. Salir"
          )

def listar_contenido():
    pwd = os.getcwd()
    try:
        ls = os.listdir()
        print("-" * 30)
        print(f"Ruta actual:\n {pwd}")
        print("Contenido:")
        
        # Listar y clasificar Archivo/Carpeta
        for item in ls:
            item_path = os.path.join(pwd, item)
            if os.path.isdir(item_path):
                tipo = "Carpeta"
            elif os.path.isfile(item_path):
                tipo = "Archivo"
            else:
                tipo = "Otro"
            
            # Impresion alineada
            print(f"[{tipo.ljust(8)}] {item}")

        print("-" * 30)
    except OSError as e:
        print(f"Error al listar contenido: {e}")

def crear_directorio():
    while True:
        dir_name = input("Nombra el directorio o introduzca 0 para volver al menú : ").strip()
        
        if dir_name == "0":
            mostrar_menu()
            break

        elif dir_name:
            try:
                os.makedirs(dir_name)
                print(f"Directorio '{dir_name}' creado con éxito.")
                break

            except FileExistsError:
                print(f"Error: El directorio '{dir_name}' ya existe. Prueba otro nombre.")
            except OSError as e:
                print(f"Error del Sistema: No se pudo crear el directorio. \n{e}")

        else:
            print("No se detectó ningún nombre. Introduzca un nombre de directorio.")


def crear_archivo():
    while True:
        archivo_input = input("Nombra el archivo que quieres crear (se añadirá .txt) o seleccione 0 para volver al menú:").strip()

        if archivo_input == "0":
            mostrar_menu()
            break

        if not archivo_input:
            print("No se detectó ningún nombre. Introduzca un nombre de archivo.")
            continue

        # Aseguramos que el archivo termine en .txt
        if not archivo_input.endswith(".txt"):
            archivo = archivo_input + ".txt"
        else:
            archivo = archivo_input

        # Proceso de creación y escritura inicial
        try:
            # Verificar que existe
            if os.path.exists(archivo):
                raise FileExistsError
                
            contenido_inicial = input(f"Introduzca el contenido inicial para '{archivo}' (pulse Enter para terminar):\n")
            

            with open(archivo, "w") as f:
                f.write(contenido_inicial)

            print(f"Archivo '{archivo}' creado con éxito con contenido inicial.")
            break
        # Manejo de errores de archivo ya existente o errores de sistema
        except FileExistsError:
            print(f"Error: El archivo '{archivo}' ya existe. Prueba otro nombre.")
        except OSError as e:
            print(f"Error del Sistema: \n{e}")


def escribir_archivo():
    while True:
        archivo_a_editar_input = input("Indique el archivo que quiere editar o seleccione 0 para volver al menú: ").strip()

        if archivo_a_editar_input == "0":
            mostrar_menu()
            break

        if archivo_a_editar_input:
            try:
                with open(archivo_a_editar_input,"a") as a:
                    nuevo_contenido = input("Introduzca nuevos datos (pulse Enter para terminar):\n")
                    a.write("\n" + nuevo_contenido) 
                    print("Datos introducidos con éxito.")
                break

            # Manejo de errores básicos
            except FileNotFoundError:
                print(f"Error: No existe el archivo '{archivo_a_editar_input}'. Intentelo otra vez.")
            except IsADirectoryError:
                 print(f"Error: '{archivo_a_editar_input}' es un directorio, no un archivo.")
            except OSError as f:
                print(f"Error del Sistema: \n{f}")
        else:
            print("No se detectó ninguna entrada. Introduzca un nombre de archivo.")


def eliminar():
    while True:
        eliminar = input("Nombra el archivo o directorio a eliminar, o seleccione 0 para volver al menú: ").strip()
        
        if eliminar == "0":
            mostrar_menu()
            break

        if eliminar:
            try:
                if os.path.isfile(eliminar):
                    os.remove(eliminar)
                    print(f"Archivo '{eliminar}' eliminado con éxito.")
                    break
                
                elif os.path.isdir(eliminar):
                    os.rmdir(eliminar)
                    print(f"Directorio vacío '{eliminar}' eliminado con éxito.")
                    break
                
                else:
                    print(f"Error: '{eliminar}' no es un archivo ni un directorio válido.")

            except FileNotFoundError:
                print(f"Error: El archivo o directorio '{eliminar}' no existe.")
            except OSError as e:
                # Si no está vacío el directorio
                if "Directory not empty" in str(e) or "No es un directorio vacío" in str(e):
                     print(f"Error: El directorio '{eliminar}' no está vacío. No se puede eliminar con esta opción.")
                else:
                    print(f"Error del Sistema: \n{e}")
        else:
            print("No se detectó ninguna entrada.")


def mostrar_info():
    while True:
        archivo_info = input("Nombra el archivo del que quieres obtener información o seleccione 0 para volver al menú: ").strip()
        
        if archivo_info == "0":
            mostrar_menu()
            break

        if archivo_info:
            try:
                info = os.stat(archivo_info)
                
                # Para mejor legibilidad
                tamano_legible = obtener_tamanio_legible(info.st_size)
                
                tiempo_modificacion = datetime.datetime.fromtimestamp(info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                tiempo_acceso = datetime.datetime.fromtimestamp(info.st_atime).strftime('%Y-%m-%d %H:%M:%S')
                tiempo_creacion = datetime.datetime.fromtimestamp(info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

                # Determinar el tipo de objeto para mostrarlo
                if os.path.isdir(archivo_info):
                    tipo_objeto = "Carpeta"
                elif os.path.isfile(archivo_info):
                    tipo_objeto = "Archivo"
                else:
                    tipo_objeto = "Otro"

                print("-" * 40)
                print(f"INFORMACIÓN DETALLADA: '{archivo_info}'")
                print("-" * 40)
                print(f"Tipo de objeto: {tipo_objeto}")
                print(f"Tamaño: {tamano_legible} ({info.st_size} bytes)")
                print(f"Última Modificación: {tiempo_modificacion}")
                print(f"Último Acceso: {tiempo_acceso}")
                print(f"Tiempo de Creación (Metadatos): {tiempo_creacion}")
                print(f"Permisos (Modo): {oct(info.st_mode)}")
                print("-" * 40)
                break

            except FileNotFoundError:
                print(f"Error: El archivo o directorio '{archivo_info}' no existe. Prueba otro nombre.")
            except OSError as e:
                print(f"Error del Sistema al obtener información: \n{e}")
        else:
            print("No se detectó ningún nombre. Introduzca un nombre de archivo.")


def main():
    seleccion = 0
    while True:
        mostrar_menu()
        try:
            seleccion = int(input("Seleccione una opción del menú: "))
            
            if seleccion == 1:
                listar_contenido()
            elif seleccion == 2:
                crear_directorio()
            elif seleccion == 3:
                crear_archivo()
            elif seleccion == 4:
                escribir_archivo()
            elif seleccion == 5:
                eliminar()
            elif seleccion == 6:
                mostrar_info()
            elif seleccion == 7:
                print("Saliendo del programa...")
                break
            else:
                print("Debe ser un número entre 1 y 7, ambos inclusive")
                
        except ValueError:
            print("Entrada no válida. Debe introducir un número.")

if __name__ == "__main__":
    main()