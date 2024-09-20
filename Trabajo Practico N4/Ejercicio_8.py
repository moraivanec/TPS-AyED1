'''
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
'''
def ultimos_caracteres(cadena, n):
    """
    Precondiciones:
    - 'cadena' debe ser una cadena que no esté vacía.
    - 'n' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una subcadena con los últimos 'n' caracteres de la cadena.
    """
    if n < 0:  # Si n es negativo, devuelve una cadena vacía
        return ""
    
    return cadena[-n:]

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Imprime la subcadena con los últimos 'n' caracteres.
    """
    cadena = "El número de teléfono es 4356-7890"
    n = 9  

    resultado = ultimos_caracteres(cadena, n)
    
    print(f"Cadena original: {cadena}")
    print(f"\nÚltimos {n} caracteres: {resultado}")

if __name__ == "__main__":
    main()
