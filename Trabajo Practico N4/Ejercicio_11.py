'''
Escribir un programa que cuente cuántas veces se encuentra una subcadena dentro
de otra cadena, sin diferenciar mayúsculas y minúsculas. Tener en cuenta que los
caracteres de la subcadena no necesariamente deben estar en forma consecutiva
dentro de la cadena, pero sí respetando el orden de los mismos. Ejemplo:
'''
def contar_subcadena(cadena, subcadena):
    """
    Precondiciones:
    - 'cadena' y 'subcadena' tienen que ser cadenas de caracteres.

    Postcondiciones:
    - Devuelve un entero que representa la cantidad de veces que la subcadena
      se encuentra en la cadena, respetando el orden de los caracteres.
    """
    cadena = cadena.lower()  # convierte a minúsculas
    subcadena = subcadena.lower()  # convierte a minúsculas
    contador = 0
    longitud = len(subcadena)

    for i in range(len(cadena)):
        if cadena[i] == subcadena[0]:  
            indice_cadena = i
            for j in range(longitud):
                if indice_cadena < len(cadena) and cadena[indice_cadena] == subcadena[j]:
                    indice_cadena += 1
                else:
                    break
            if j == longitud - 1:  # si se encuentran todos los caracteres
                contador += 1

    return contador

def main() -> None:
    cadena = input("Ingrese la cadena principal: ")
    subcadena = input("Ingrese la subcadena a buscar: ")
    
    resultado = contar_subcadena(cadena, subcadena)
    print(f"\nLa subcadena '{subcadena}' se encuentra {resultado} veces en la cadena.")

if __name__ == "__main__":
    main()
