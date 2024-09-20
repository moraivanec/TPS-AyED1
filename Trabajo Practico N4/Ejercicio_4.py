'''
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
'''

def convertir_a_romano(numero):
    """
    Precondiciones:
    - 'numero' debe ser un número entero entre 0 y 3999.

    Postcondiciones:
    - Devuelve una cadena que representa el número en formato romano.
    - Devuelve un mensaje de error si el número está fuera de rango.
    """
    if numero < 0 or numero >= 4000:
        return "Número fuera de rango."

    valores_romanos = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    resultado = ""
    for valor, romano in valores_romanos:
        while numero >= valor:
            resultado += romano 
            numero -= valor # Resta el valor correspondiente del número
    
    return resultado

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Solicita al usuario un número entero y muestra su representación en números romanos.
    """
    numero = int(input("Ingrese un número entre 0 y 3999: "))
    numero_romano = convertir_a_romano(numero)
    print(f"\nNúmero romano: {numero_romano}")

if __name__ == "__main__":
    main()
