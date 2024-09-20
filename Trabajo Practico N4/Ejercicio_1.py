'''
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
'''
def es_capicua(cadena):
    """
    Precondiciones:
    - 'lista' no tiene que estar vacía.

    Postcondiciones:
    - Devuelve True si la cadena es capicúa.
    - Devuelve False si la cadena no es capicúa.
    """
    izquierda = 0
    derecha = len(cadena) - 1
    
    while izquierda < derecha:
        if cadena[izquierda] != cadena[derecha]: 
            return False 
        izquierda += 1  
        derecha -= 1  # Retrocede el índice desde el final
    return True 

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Solicita al usuario una cadena y verifica si es capicúa, imprimiendo el resultado.
    """
    cadena = input("Ingrese una cadena de caracteres: ")  # Solicita la cadena al usuario
    if es_capicua(cadena):
        print("\nLa cadena es capicúa.")  # Imprime si la cadena es capicúa
    else:
        print("\nLa cadena no es capicúa.")  # Imprime si la cadena no es capicúa

if __name__ == "__main__":
    main()
