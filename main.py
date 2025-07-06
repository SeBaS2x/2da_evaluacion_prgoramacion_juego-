import sys
from os import system
from funciones import *


def main() -> None:
    print("BIENVENIDO A --SUPER-QUIZ-- ")
    print("El juego favorito de tus SuperHeroe favorito!!")
    matriz, columnas = llamar_csv()
    opciones = input(
        "\ningrese la dificultad:" "\nFacil (1) " "\nNormal(2)" "\nDificil(3): "
    )
    preguntas = 7
    match (opciones):
        case "1":
            preguntas_filtradas = filtrar_por_dificultad(matriz, columnas, "fácil")
            for fila in preguntas_filtradas:
                input(fila[0])
        case "2":
            preguntas_filtradas = filtrar_por_dificultad(matriz, columnas, "normal")
            for fila in preguntas_filtradas:
                input(fila[0])
        case "3":
            preguntas_filtradas = filtrar_por_dificultad(matriz, columnas, "difícil")
            for fila in preguntas_filtradas:
                print(fila[0])


if __name__ == "__main__":
    sys.exit(main())
