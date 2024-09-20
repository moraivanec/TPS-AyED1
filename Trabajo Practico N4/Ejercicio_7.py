'''
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''

def con_rebanadas(cadena, posicion, cantidad):
    """
    Precondiciones:
    - 'cadena' debe ser una cadena que no esté vacía.
    - 'posicion' debe ser un número entero válido dentro de la longitud de la cadena.
    - 'cantidad' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve la cadena resultante después de eliminar la subcadena.
    """
    if posicion < 0:  # Asegura que la posición mínima sea 0
        posicion = 0
    if cantidad < 0:  # Asegura que la cantidad mínima sea 0
        cantidad = 0
    if posicion + cantidad > len(cadena):  # Ajusta la cantidad si excede el tamaño de la cadena
        cantidad = len(cadena) - posicion

    return cadena[:posicion] + cadena[posicion + cantidad:]

def sin_rebanadas(cadena, posicion, cantidad):
    """
    Precondiciones:
    - 'cadena' debe ser una cadena que no esté vacía.
    - 'posicion' debe ser un número entero válido dentro de la longitud de la cadena.
    - 'cantidad' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve la cadena resultante después de eliminar la subcadena.
    """
    resultado = "" 
    for i in range(len(cadena)):
        if (i < posicion) or (i >= posicion + cantidad):  # Solo añade caracteres fuera de la subcadena
            resultado += cadena[i]
    return resultado

cadena = "El número de teléfono es 4356-7890"
posicion = 25
cantidad = 9

print(f"Subcadena eliminada con rebanadas: {con_rebanadas(cadena, posicion, cantidad)}") 
print(f"Subcadena eliminada sin rebanadas: {sin_rebanadas(cadena, posicion, cantidad)}")  
    