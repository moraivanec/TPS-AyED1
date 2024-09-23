'''
Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha,
considerando que la ocupación del camión no debe ser inferior al 80%; en caso
contrario el camión no serán despachado por su alto costo.
'''

import random as rn

def peso_naranja():
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Retorna un número entero aleatorio entre 150 y 350 que representa el peso de
    la naranja en gramos.
    """
    peso_aleatorio = rn.randint(150, 350)
    return peso_aleatorio

def clasificar_naranjas(cantidad_naranjas):
    """
    Precondiciones:
    - 'cantidad_naranjas' tiene que ser un número entero positivo.
    
    Postcondiciones:
    - Devuelve la cantidad de cajones llenos, naranjas para jugo y sobrantes.
    """
    cajones = 0
    naranjas_jugo = 0
    peso_total = 0

    for _ in range(cantidad_naranjas):
        peso = peso_naranja()
        if 200 <= peso <= 300:
            peso_total += peso
            if peso_total >= 50000:  
                cajones += 1
                peso_total = 0
        else:
            naranjas_jugo += 1

    sobrantes = cantidad_naranjas - (cajones * 100) - naranjas_jugo
    return cajones, naranjas_jugo, sobrantes

def calcular_camiones(cantidad_naranjas):
    """
    Precondiciones:
    - 'cantidad_naranjas' tiene que ser un número entero positivo.
    
    Postcondiciones:
    - Devuelve la cantidad de camiones necesarios.
    """
    peso_total = cantidad_naranjas * 200  # Asumiendo un promedio de 200 gramos por naranja
    camiones_necesarios = peso_total / 500000  
    camiones_necesarios = (camiones_necesarios // 1) + (1 if camiones_necesarios % 1 > 0 else 0)

    if camiones_necesarios * 500000 < 0.8 * peso_total:
        return 0  # No se despacha el camión si no ocupa al menos el 80%
    return camiones_necesarios

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Imprime la cantidad de cajones llenos, naranjas para jugo, sobrantes y
    camiones necesarios.
    """
    cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    cajones, naranjas_para_jugo, sobrantes = clasificar_naranjas(cantidad_naranjas)
    
    print(f"\nCajones llenos: {cajones}")
    print(f"Naranjas para jugo: {naranjas_para_jugo}")
    print(f"Sobrantes de naranjas: {sobrantes}")
    
    camiones_necesarios = calcular_camiones(cantidad_naranjas)
    if camiones_necesarios > 0:
        print(f"Camiones necesarios para transportar la cosecha: {camiones_necesarios}")
    else:
        print("No se despacharán camiones por su alto costo.")

if __name__ == "__main__":
    main()
