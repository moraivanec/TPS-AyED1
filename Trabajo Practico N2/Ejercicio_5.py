'''
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.
'''

def lista_ordenada(lista):
    if len(lista) <= 1:
        return True
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def menu():
    lista_1 = [1, 2, 3]
    lista_2 = ['b', 'a']
    
    print(f"Lista: {lista_1} = {lista_ordenada(lista_1)}")
    print(f"Lista: {lista_2} = {lista_ordenada(lista_2)}")
    
menu()

