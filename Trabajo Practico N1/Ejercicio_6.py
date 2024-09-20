'''
6. Desarrollar una función que reciba como parámetros dos números enteros positivos
y devuelva como valor de retorno el número que resulte de concatenar ambos
parámetros. Por ejemplo, si recibe 1234 y 567 debe devolver 1234567. No se permite
utilizar facilidades de Python no vistas en clase.
'''

def concatenar_numeros(a, b):
    """
    Precondiciones:
    - 'a' y 'b' deben ser números enteros positivos.

    Postcondiones:
    - Devuelve un entero que es la concatenación de 'a' y 'b'.
    """
    digitos_b = 1
    valor_b = b
    while b >= 10: # Itera hasta llegar al primer dígito y así poder contar cuántos dígitos tiene 'b'
        b //= 10
        digitos_b += 1
        
    resultado = a * (10 ** digitos_b) + valor_b # Mueve a 'a' a la izquierda para dejarle espacio a los dígitos de 'b'
    return resultado

def main() -> None:
    """
    Precondiciones:
    - El usuario debe escribir entradas válidas.
    
    Postcondiciones:
    - Se imprime en pantalla el resultado de concatenar los 2 números ingresados.
    - El resultado es un número entero.
    """
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))

    resultado = concatenar_numeros(a, b)
    print(f"\nEl número resultante de concatenar {a} y {b} es: {resultado}.")


if __name__ == "__main__":
    main()