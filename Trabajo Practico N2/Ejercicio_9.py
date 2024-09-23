'''
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado. 
'''

def generar_multiplos(a, b):
    """
    Precondiciones:
    - 'a' y 'b' tienen que ser números enteros, y 'a' debe ser menor que 'b'.

    Postcondiciones:
    - Devuelve una lista de múltiplos de 7 entre 'a' y 'b' que no son múltiplos de 5.
    """
    multiplos = [num for num in range(a, b + 1) if num % 7 == 0 and num % 5 != 0]
    return multiplos

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Solicita al usuario los valores de 'a' y 'b', y genera e imprime una lista de múltiplos de 7 
      entre 'a' y 'b' que no son múltiplos de 5.
      """
    a = int(input("Ingrese el valor de a: "))
    b = int(input("Ingrese el valor de b: "))
    
    if a >= b:
        print("\nError! 'a' debe ser menor que 'b'.")
        return
    
    resultado_multiplos = generar_multiplos(a, b)
    print(f"\nLos múltiplos de 7 entre {a} y {b} que no son múltiplos de 5 son: {resultado_multiplos}")

if __name__ == "__main__":
    main()
