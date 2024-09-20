'''
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repita.
Imprimir la matriz por pantalla
'''

import random as rn

def numero_aleatorio(n, numeros_usados):
    """
    Precondiciones:
    - 'n' debe ser un entero positivo.
    - 'numeros_usados' es una lista que contiene los números ya generados.

    Postcondiciones:
    - Devuelve un número aleatorio no utilizado.
    """
    while True:
        num = rn.randint(0, n ** 2 - 1)
        if num not in numeros_usados:
            return num

def matriz_aleatoria(n):
    """
    Precondiciones:
    - 'n' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz n x n llena de números aleatorios únicos.
    """
    matriz = []
    numeros_usados = []
    for i in range(n): # Recorre las filas
        fila = []
        for j in range(n): # Recorre las columnas
            numero = numero_aleatorio(n, numeros_usados)
            fila.append(numero)
            numeros_usados.append(numero)
        matriz.append(fila)
    return matriz

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Crea una matriz aleatoria y la imprime en pantalla.
    """
    n = int(input("Ingrese el tamaño de la matriz (n x n): "))
    matriz = matriz_aleatoria(n)
    print("\nMatriz con números aleatorios: ")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    main()
