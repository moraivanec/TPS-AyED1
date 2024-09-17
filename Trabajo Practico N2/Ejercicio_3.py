'''
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10
valores de la lista.
'''

def generar_cuadrados(n):
    cuadrados = []
    for i in range(1, n + 1):
        cuadrados.append(i ** 2)
    return cuadrados

def imprimir_valores(lista):
    # Imprimo los últimos 10 valores de la lista
    cantidad = 10
    if len(lista) < cantidad:
        cantidad = len(lista)
    print("\nÚltimos 10 valores: ")
    for i in range(len(lista) - cantidad, len(lista)):
        print(lista[i])
        
def menu():
    n = int(input("Introduzca el valor de n: "))
    
    lista_cuadrados = generar_cuadrados(n)
    print(f"\nLista de cuadrados: {lista_cuadrados}")
    
    imprimir_valores(lista_cuadrados)
    
menu()
    
    