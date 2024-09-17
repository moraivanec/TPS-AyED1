'''
Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:
a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
'''

import random as rn

def cargar_lista():
    cantidad = rn.randint(10, 99)
    lista = []
    for i in range(cantidad):
        num = rn.randint(1000, 9999)
        lista.append(num)
    return lista

def calcular_producto(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_valor(lista, valor):
    indice = 0
    while indice < len(lista):
        if lista[indice] == valor:
            lista.pop(indice)
        else:
            indice += 1
    return lista

def es_capicua(lista):
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda < derecha:
        if lista[izquierda] != lista[derecha]:
            return False
        izquierda += 1
        derecha -= 1
    return True

def menu():
    lista = cargar_lista()
    print(f"Lista con número al azar de 4 dígitos: {lista}")
    
    producto = calcular_producto(lista)
    print(f"\nEl producto de todos los elementos de la lista es: {producto}")
    
    valor_a_eliminar = int(input("\nIngrese el valor que desee eliminar de la lista: "))
    lista = eliminar_valor(lista, valor_a_eliminar)
    print(f"\nLista actualizada: {lista}")
    
    lista_capicua = [50, 17, 91, 17, 50]
    if es_capicua(lista_capicua):
        print(f"\nLa lista: {lista_capicua} es capicúa.")
    else:
        print(f"\nLa lista: {lista_capicua} no es capicúa.")
        
menu()
