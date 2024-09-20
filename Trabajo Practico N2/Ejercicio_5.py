'''
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.
'''

def lista_ordenada(lista):
    """
    Precondiciones:
    - 'lista' debe ser una lista que tenga elementos comparables.

    Postcondiciones:
    - Devuelve True si la lista está ordenada en forma ascendente.
    - Devuelve False si la lista no está ordenada en forma ascendente.
    """
    if len(lista) <= 1:
        return True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def main() -> None:
    """
    Precondiciones:
    - Las listas a verificar deben contener elementos comparables.

    Postcondiciones:
    - Se imprimen los resultados de la verificación de las listas.
    """
    lista_1 = [1, 2, 3]
    lista_2 = ['b', 'a']
    
    print(f"Lista: {lista_1} = {lista_ordenada(lista_1)}")
    print(f"Lista: {lista_2} = {lista_ordenada(lista_2)}")

if __name__ == "__main__":
    main()

