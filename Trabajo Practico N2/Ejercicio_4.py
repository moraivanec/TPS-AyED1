'''
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
'''

def eliminar_valores(lista_original, lista_a_eliminar):
    """
    Precondiciones:
    - 'lista_original' y 'lista_a_eliminar' deben ser listas.

    Postcondiciones:
    - Modifica 'lista_original' para que no contenga los elementos de 'lista_a_eliminar'.
    - No devuelve ningún valor, pero imprime la lista resultante.
    """
    print(f"Lista original: {lista_original}")
    print(f"\nLista de valores a eliminar: {lista_a_eliminar}")
    
    for valor in lista_a_eliminar:
        while valor in lista_original: # Si encuentra el mismo valor, lo elimina
            lista_original.remove(valor)
    
    print(f"\nLista resultante: {lista_original}")

def main() -> None:
    """
    Precondiciones:
    - Las listas deben ser válidas.

    Postcondiciones:
    - Imprime la lista original, la lista de valores a eliminar y la lista resultante.
    """
    lista_original = [1, 2, 3, 4, 2, 5, 2]
    lista_a_eliminar = [2, 4]

    eliminar_valores(lista_original, lista_a_eliminar)

if __name__ == "__main__":
    main()
