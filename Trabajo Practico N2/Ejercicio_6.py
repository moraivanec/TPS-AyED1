'''
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
'''
def normalizar_lista(lista):
    """
    Precondiciones:
    - 'lista' debe contener al menos un número entero positivo.

    Postcondiciones:
    - Devuelve una nueva lista donde cada elemento es el resultado de dividir el elemento
    original por la suma total de la lista.
    """
    lista_normalizada = []
    suma_total = 0
    
    for elemento in lista:
        suma_total += elemento
    
    for elemento in lista:
        valor_normalizado = elemento / suma_total
        lista_normalizada.append(valor_normalizado)
        
    return lista_normalizada

def main():
    """
    Precondiciones:
    - La lista debe tener al menos un elemento entero positivo.

    Postcondiciones:
    - Se imprime la lista original, la lista normalizada y la suma de la lista normalizada.
    """
    lista_original = [1, 1, 2]
    print(f"Lista original: {lista_original}")
    
    lista_normalizada = normalizar_lista(lista_original)
    print(f"\nLista normalizada: {lista_normalizada}")

    # Verificar que la suma de los elementos sea 1.0
    suma_normalizada = 0
    for elemento in lista_normalizada:
        suma_normalizada += elemento
    print(f"\nSuma de la lista normalizada: {suma_normalizada}")

if __name__ == "__main__":
    main()
