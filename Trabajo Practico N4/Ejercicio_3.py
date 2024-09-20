'''
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
'''

def obtener_claves(clave_maestra):
    """
    Precondiciones:
    - 'clave_maestra' debe ser una cadena que no esté vacía.

    Postcondiciones:
    - Devuelve dos cadenas: 'clave1' con los dígitos en posiciones pares y 'clave2' con los dígitos en posiciones impares.
    """
    clave1 = ""  # Clave construida con dígitos en posiciones pares
    clave2 = ""  # Clave construida con dígitos en posiciones impares
    
    for i in range(len(clave_maestra)): 
        digito = clave_maestra[i] 
        if i % 2 == 0:
            clave1 += digito  
        else:
            clave2 += digito  
            
    return clave1, clave2  

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Solicita al usuario una clave maestra y muestra las claves separadas.
    """
    clave_maestra = input("Ingrese la clave maestra: ") 
    clave1, clave2 = obtener_claves(clave_maestra)  
    print(f"\nClave 1: {clave1}")  
    print(f"Clave 2: {clave2}")  

if __name__ == "__main__":
    main()
