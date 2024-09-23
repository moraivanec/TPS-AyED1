'''
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla.
'''
import random as rn

def numeros_aleatorios(cantidad):
    """
    Precondiciones:
    - 'cantidad' tiene que ser un número entero positivo.

    Postcondiciones:
    - Devuelve una lista de números enteros aleatorios entre 1 y 100.
    """
    numeros_aleatorios = [rn.randint(1, 100) for _ in range(cantidad)]
    return numeros_aleatorios

def filtrar_impares(numeros):
    """
    Precondiciones:
    - 'numeros' tine que ser una lista de números enteros.

    Postcondiciones:
    - Devuelve una lista de números impares filtrados de la lista original.
    """
    numeros_filtrados = list(filter(lambda x: x % 2 != 0, numeros))
    return numeros_filtrados

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Genera una lista de números aleatorios, filtra los impares y muestra ambas listas.
    """
    cantidad = 20  # Por ejemplo, genera 20 números aleatorios
    numeros = numeros_aleatorios(cantidad)
    impares = filtrar_impares(numeros)

    print(f"Números aleatorios: {numeros}")
    print(f"Números impares: {impares}")

if __name__ == "__main__":
    main()
