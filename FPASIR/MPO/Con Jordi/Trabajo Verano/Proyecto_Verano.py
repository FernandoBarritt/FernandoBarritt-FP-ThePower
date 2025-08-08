# --- SECCIÓN 1: CONFIGURACIÓN Y DATOS ---

# Las preguntas
def cargar_preguntas():
    return [
        {
            "pregunta": " 1- Qué número llevaba Messi cuando jugaba en el Barcelona",
            "opciones": ["A. 1", "B. 54", "C. 10", "D. 30"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": " 2- Cuál es el río más largo de España",
            "opciones": ["A. Tajo", "B. Ebro", "C. Guadalquivir", "D. Tinto"],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": " 3- ¿Cuál es la capital de Australia?",
            "opciones": ["A. Sídney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": " 4- ¿Quién escribió 'Cien años de soledad'?",
            "opciones": ["A. Mario Vargas Llosa", "B. Gabriel García Márquez", "C. Julio Cortázar", "D. Isabel Allende"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": " 5- ¿Qué planeta es el más cercano al Sol?",
            "opciones": ["A. Venus", "B. Mercurio", "C. Marte", "D. Tierra"],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": " 6- ¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["A. 1935", "B. 1937", "C. 1939", "D. 1941"],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": " 7- ¿Cuál es el resultado de 9 x 8?",
            "opciones": ["A. 72", "B. 81", "C. 64", "D. 70"],
            "respuesta_correcta": "A"
        }
    ]

# Para que funcione aunque añada o quite preguntas del listado. Se usará para la evaluación final
numero_de_preguntas = int(len(cargar_preguntas()))


# --- SECCIÓN 2: FUNCIONES AUXILIARES ---

# Pedimos el nombre del usuario para guardar su puntuación luego
def pedir_nombre_usuario():
    nombre = input("Introduce tu nombre: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Introduce tu nombre: ").strip()
    return nombre

# Muestra una pregunta con sus opciones
def mostrar_pregunta(una_pregunta):
    print("\n" + una_pregunta["pregunta"])
    for opcion in una_pregunta["opciones"]:
        print(opcion)

# Pide una respuesta válida: A, B, C o D
def obtener_respuesta():
    while True:
        respuesta = input("Tu respuesta (A, B, C, D) es: ")
        respuesta = respuesta.strip().upper()
        if respuesta in ["A", "B", "C", "D"]:
            return respuesta
        else:
            print("Opción no válida. Inténtelo de nuevo.")

# Devuelve True si el usuario acierta, si no, le dice la correcta
def comprobar_respuesta(respuesta_usuario, respuesta_correcta):
    if respuesta_usuario == respuesta_correcta:
        print(" ✅ Correcto, pero ha sido suerte")
        return True
    else:
        print(f" ❌ Incorrecto, inútil. La respuesta correcta era: {respuesta_correcta}\n")
        return False

# Al final del test, muestra los resultados y valoración
def resultados_finales():
    print("\n### RESULTADOS FINALES ###")
    print(f"Número de aciertos: {aciertos}")
    print(f"Número total de preguntas: {numero_de_preguntas}")
    porcentaje = int((aciertos / numero_de_preguntas) * 100)
    print(f"Porcentaje de aciertos: {porcentaje}%")
    if porcentaje >= 80:
        print("🔥 Estás hech@ una bestia, ¡bien hecho! 🔥")
    elif porcentaje >= 50:
        print("🤷🏻‍♂️ Bueno, no está mal. Podría estar mejor, pero podría estar mucho peor 🤷🏻‍♂️")
    else:
        print("🤡 Vuelve a primaria por el bien de la sociedad, por favor 🤡")

# Guarda en archivo el nombre y la puntuación final
def guardar_resultado(nombre, aciertos, total):
    with open("ranking.txt", "a") as f:
        f.write(f"{nombre}, {aciertos}/{total}\n")


# --- SECCIÓN 3: LÓGICA PRINCIPAL DEL CUESTIONARIO ---

# Función principal que ejecuta el cuestionario
def empezar_cuestionario(nombre_usuario):
    global aciertos  # Se usa global para poder mostrarlo después en resultados_finales
    aciertos = 0
    preguntas = cargar_preguntas()
    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta = obtener_respuesta()
        if comprobar_respuesta(respuesta, pregunta["respuesta_correcta"]):
            aciertos += 1
    resultados_finales()
    guardar_resultado(nombre_usuario, aciertos, numero_de_preguntas)


# --- SECCIÓN 4: MENÚ PRINCIPAL Y EJECUCIÓN ---

# Función principal que muestra el menú al usuario y gestiona la elección de opciones
def menu():
    while True:
        print("### MENU ###")
        print("1. Empezar Cuestionario")
        print("2. Ranking")
        print("3. Salir")
        try:
            seleccion_menu = int(input("Seleccione una de las opciones del menú indicando su número: "))
        except ValueError:
            print("Entrada no válida. Solo se aceptan números")
            continue  # Si da error, vuelve a mostrar el menú
    #Funcionalidad de las opciones del menú
        if seleccion_menu == 1:
            nombre_usuario = pedir_nombre_usuario()  # Guardo nombre antes de empezar para el ranking
            empezar_cuestionario(nombre_usuario)
        elif seleccion_menu == 2:
            try:
                with open("ranking.txt", "r") as ranking_archivo:
                    ranking_archivo = ranking_archivo.read()
                    #Si el archivo está vacío o solo hay espacios
                    if not ranking_archivo.strip():
                        print("El archivo está vacío. ¡Juega para añadir el primer resultado! \n")
                    else:
                        print("### RANKING HISTÓRICO ###")
                        print(ranking_archivo)
            #Si no existe el archivo
            except FileNotFoundError:
                print("El ranking no se ha creado todavía. Juegue para inicializar el ranking")




        elif seleccion_menu == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Solo se permite 1 o 2")

# Arranca el programa desde aquí
menu()