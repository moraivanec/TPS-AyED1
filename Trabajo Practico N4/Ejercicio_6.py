'''
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento
de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la
subcadena que comienza en la posición 25 y tiene 9 caracteres, resultando la subcadena
"4356-7890". Escribir una función para cada uno de los siguientes casos:
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
    - Devuelve la subcadena extraída utilizando rebanadas.
    """
    if posicion < 0:
        posicion = 0  # Asegura que la posición mínima sea 0
    if cantidad < 0:
        cantidad = 0  # Asegura que la cantidad mínima sea 0
    if posicion + cantidad > len(cadena):
        cantidad = len(cadena) - posicion  # Ajusta la cantidad si excede el tamaño de la cadena
    
    return cadena[posicion:posicion + cantidad]

def sin_rebanadas(cadena, posicion, cantidad):
    """
    Precondiciones:
    - 'cadena' debe ser una cadena que no esté vacía.
    - 'posicion' debe ser un número entero válido dentro de la longitud de la cadena.
    - 'cantidad' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve la subcadena extraída sin utilizar rebanadas.
    """
    subcadena = "" 
    for i in range(posicion, posicion + cantidad):  
        if i < len(cadena):  # Verifica que el índice no exceda la longitud de la cadena
            subcadena += cadena[i]  
    return subcadena

cadena = "El número de teléfono es 4356-7890"
posicion = 25
cantidad = 9

print(f"Subcadena con rebanadas: {con_rebanadas(cadena, posicion, cantidad)}") 
print(f"Subcadena sin rebanadas: {sin_rebanadas(cadena, posicion, cantidad)}")  

