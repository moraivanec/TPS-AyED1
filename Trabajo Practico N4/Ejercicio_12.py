'''
 Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla.
'''
def baraja_espaniola():
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Devuelve una lista de cadenas que representan los naipes de la baraja española.
    """
    palos = ["Oros", "Copas", "Espadas", "Bastos"]
    
    baraja = [f"{numero} {palo}" for palo in palos for numero in range(1, 13)]
    
    return baraja

def main() -> None:
    baraja = baraja_espaniola()
    print("Baraja española:")
    
    for naipe in baraja:
        print(naipe)

if __name__ == "__main__":
    main()