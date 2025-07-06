import sys
from os import system
from funciones import *


def main() -> None:
    print("BIENVENIDO A --SUPER-QUIZ-- ")
    print("El juego de tus SuperHeroe favorito!!\n")
    print("Facil (1) " "\nNormal(2)" "\nDificil(3) ")
    print("El juego de tus SuperHeroe favorito!!\n")
    print("Facil (1) " "\nNormal(2)" "\nDificil(3) ")
    matriz, columnas = llamar_csv()
    opciones = input("ingrese la dificultad: ")
    preguntas = 7
    match (opciones):
        case "1":
            matriz_filtrada_dificultad = filtrar_por_dificultad(
                matriz, columnas, "fácil"
            )
            opciones = filtrar_columna_clave(
                matriz_filtrada_dificultad, columnas, "opciones"
            )
            preguntas = filtrar_columna_clave(
                matriz_filtrada_dificultad, columnas, "pregunta"
            )
            for i in range(len(preguntas)):
                print("\n" + preguntas[i])
                opciones_separadas = opciones[i].split("|")
                for j in range(len(opciones_separadas)):
                    print(f"{j+1}. {opciones_separadas[j]}")
                input("Elige una opción: ")
        case "2":
            matriz_filtrada_dificultad = filtrar_por_dificultad(
                matriz, columnas, "normal"
            )
            opciones = filtrar_columna_clave(
                matriz_filtrada_dificultad, columnas, "opciones"
            )
            preguntas = filtrar_columna_clave(
                matriz_filtrada_dificultad, columnas, "pregunta"
            )
            for i in range(len(preguntas)):
                print("\n" + preguntas[i])
                opciones_separadas = opciones[i].split("|")
                for j in range(len(opciones_separadas)):
                    print(f"{j+1}. {opciones_separadas[j]}")
                input("Elige una opción: ")
        case "3":
            matriz_filtrada_dificultad = filtrar_por_dificultad(
                matriz, columnas, "difícil"
            )
            opciones = filtrar_columna_clave(
                matriz_filtrada_dificultad, columnas, "opciones"
            )
            preguntas = filtrar_columna_clave(
                matriz_filtrada_dificultad, columnas, "pregunta"
            )
            for i in range(len(preguntas)):
                print("\n" + preguntas[i])
                opciones_separadas = opciones[i].split("|")
                for j in range(len(opciones_separadas)):
                    print(f"{j+1}. {opciones_separadas[j]}")
                input("Elige una opción: ")


if __name__ == "__main__":
    sys.exit(main())
