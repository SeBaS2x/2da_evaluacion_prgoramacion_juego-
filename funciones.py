import sys

sys.stdout.reconfigure(encoding="utf-8")


def crear_matriz(cantidad_f: int, cantidad_c: int, valor) -> list:
    """Crea matriz vacia, pasar cantidad de filas, columnas y el valor

    Args:
        cantidad_f (_type_): Cantidad de filas
        cantidad_c (_type_): Cantidad de columnas
        valor (_type_): valor de inicializacion

    Returns:
        list: Una matriz Vacia
    """
    matriz = []
    for i in range(cantidad_f):
        fila = [valor] * cantidad_c
        matriz += [fila]
    return matriz


def llamar_csv():
    """LLama el archivo .csv y lo carga en una matriz vacia

    Returns:
        _type_: Devuelve Columnas: primera fila con el valor de las columnas.
                devuelve Matriz : Matriz cargada con el csv
    """
    with open("preguntas_superheroes.csv", "r", encoding="utf-8") as archivo:
        linea = archivo.readline()
        columnas = []
        valor = ""
        for c in linea:
            if c == "\n" or c == ",":
                columnas += [valor]
                valor = ""
            else:
                valor += c
        filas = archivo.readlines()
        num_filas = len(filas)
        num_columnas = len(columnas)
        matriz = crear_matriz(num_filas, num_columnas, None)
        for i in range(num_filas):
            linea = filas[i]
            valor = ""
            col = 0
            for c in linea:
                if c == "," or c == "\n":
                    if valor.isdigit():
                        matriz[i][col] = int(valor)
                    else:
                        matriz[i][col] = valor
                    valor = ""
                    col += 1
                else:
                    valor += c
        return matriz, columnas


def mostrar_matriz(matriz: list):
    """Muestra la Matriz que se le pase

    Args:
        matriz (_type_): Matriz a mostrar
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")


def filtrar_por_dificultad(matriz: list, columnas: list, dificultad: str) -> list:
    """Muestra toda la fila de la dificultad que se le pase

    Args:
        matriz (_type_): Matriz en la que se tiene que buscar
        columnas (_type_): Primera fila del archivo .csv
        dificultad (_type_): Dificultad a filtrar

    Returns:
        _type_: LISTAS con las filas filtradas
    """
    indice_dificultad = -1
    for i in range(len(columnas)):
        if columnas[i] == "dificultad":
            indice_dificultad = i
            break

    filtradas = []
    for i in range(len(matriz)):
        if matriz[i][indice_dificultad] == dificultad:
            filtradas += [matriz[i]]
    return filtradas


def filtrar_columna_clave(lista_ya_filtrada, columnas: list, palabra_clave) -> list:
    inidice_preguntas = -1
    for i in range(len(columnas)):
        if columnas[i] == palabra_clave:
            inidice_preguntas = i
            break
    preguntas = []

    for i in range(len(lista_ya_filtrada)):
        preguntas += [lista_ya_filtrada[i][inidice_preguntas]]
    return preguntas


def capitalizar_primera_letra(texto: str) -> str:
    
    inicio = 0
    while inicio < len(texto) and texto[inicio] == " ":
        inicio += 1
    
    fin = len(texto) - 1
    while fin >= 0 and texto[fin] == " ":
        fin -= 1
  
    if inicio > fin:
        return ""
    texto_sin_espacios = texto[inicio : fin + 1]
    
    primera = texto_sin_espacios[0]
    codigo = ord(primera)
    if 97 <= codigo <= 122:  # a-z
        primera = chr(codigo - 32)
    return primera + texto_sin_espacios[1:]


def respuestas_correctas(matriz: list) -> list:
    respuestas = []
    for fila in matriz:
        respuestas += [fila[2]]
    return respuestas


def calcular_puntaje(matriz: list, respuestas_usuario: list) -> int:
    total = 0
    for i in range(len(matriz)):
        if respuestas_usuario[i].strip().lower() == matriz[i][2].strip().lower():
            total += matriz[i][4]
    return total
def validar_respuesta(respuesta: str, opciones: list) -> bool:      
    """Valida si la respuesta del usuario es correcta

    Args:
        respuesta (str): Respuesta del usuario
        opciones (list): Lista de opciones correctas

    Returns:
        bool: True si la respuesta es correcta, False si no lo es
    """
    opciones_separadas = opciones.split("|")
    return respuesta.strip().lower() in [opcion.strip().lower() for opcion in opciones_separadas]
    

# matriz, columnas = llamar_csv()
# facil = filtrar_por_dificultad(matriz, columnas, "fácil")
# # # mostrar_mariz(matriz)
# # # for i in range(len(facil)):
# # #     print(facil[i])
# preguntas = filtrar_columna_clave(facil, columnas,"opciones")
# for i in range(len(preguntas)):
#     print(preguntas[0])
