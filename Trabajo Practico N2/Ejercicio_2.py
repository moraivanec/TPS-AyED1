'''
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
'''

import random as rn

def cargar_lista():
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Devuelve una lista de números aleatorios del 1 al 100.
    """
    cantidad = rn.randint(10, 99)
    lista = []
    for i in range(cantidad):
        num = rn.randint(1000, 9999)
        lista.append(num)
    return lista

def detectar_repetidos(lista):
    """
    Precondiciones:
    - 'lista' debe ser una lista con números.

    Postcondiciones:
    - Devuelve True si la lista contiene elementos repetidos.
    - Devuelve False si la lista no contiene elementos repetidos.
    """
    for i in range(len(lista)):
        # Comparo el elemento actual con los que siguen
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False

def elementos_unicos(lista):
    """
    Precondiciones:
    - 'lista' debe ser una lista con números.

    Postcondiciones:
    - Devuelve una nueva lista con los elementos únicos de la lista original.
    """
    lista_unica = []
    for elemento in lista:
        encontrado = False
        # Recorro la lista única para ver si el elemento ya se encuentra ahí
        for item in lista_unica:
            if item == elemento:
                encontrado = True
                break
        if not encontrado:
            lista_unica.append(elemento)
    return lista_unica

def main() -> None:
    """
    Precondiciones:
    - El usuario debe ingresar un número entero positivo para la cantidad de elementos.

    Postcondiciones:
    - Se imprime en pantalla la lista generada, si contiene repetidos y la lista de elementos únicos.
    """
    lista = cargar_lista()
    print(f"Lista generada: {lista}")
    
    repetidos = detectar_repetidos(lista)
    if repetidos:
        print(f"\nLa lista contiene elementos repetidos.")
    else:
        print("\nLa lista no contiene elementos repetidos.")
        
    lista_unicos = elementos_unicos(lista)
    print(f"\nLista con elementos únicos: {lista_unicos}")

if __name__ == "__main__":
    main()