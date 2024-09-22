def cargar_matriz(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros.
    """
    matriz = []
    for i in range(tamanio):
        fila = []
        for j in range(tamanio):
            num = int(input(f"Ingrese el número en la posición ({i}, {j}): "))
            fila.append(num)
        matriz.append(fila)
    return matriz

def ordenar_filas(matriz):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas con números enteros.

    Postcondiciones:
    - Las filas de la matriz se ordenan de forma ascendente.
    """
    for fila in matriz:
        for i in range(len(fila)):
            for j in range(len(fila) - 1):
                if fila[j] > fila[j + 1]:
                    fila[j], fila[j + 1] = fila[j + 1], fila[j]

def intercambiar_filas(matriz, fila1, fila2):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas.
    - 'fila1' y 'fila2' deben ser índices válidos.

    Postcondiciones:
    - Las filas indicadas son intercambiadas en la matriz.
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def intercambiar_columnas(matriz, col1, col2):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas.
    - 'columna1' y 'columna2' deben ser índices válidos.

    Postcondiciones:
    - Las columnas indicadas son intercambiadas en la matriz.
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]

def transponer_matriz(matriz):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas.

    Postcondiciones:
    - La matriz es transpuesta.
    """
    tamanio = len(matriz)
    for i in range(tamanio):
        for j in range(i + 1, tamanio):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

def promedio_fila(matriz, fila):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas.
    - 'fila' debe ser un índice válido.

    Postcondiciones:
    - Devuelve el promedio de los elementos de la fila indicada.
    """
    total = 0
    contador = 0
    
    for elemento in matriz[fila]:
        total += elemento  
        contador += 1  
    if contador > 0:
        return total / contador  
    return 0  # Si no hay elementos, devuelve 0

def porcentaje_impares_columna(matriz, columna):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas.
    - 'columna' debe ser un índice válido.

    Postcondiciones:
    - Devuelve el porcentaje de elementos impares en la columna indicada.
    """
    total = 0
    impares = 0
    
    for fila in matriz:
        if columna < len(fila):  
            total += 1  
            if fila[columna] % 2 != 0:  
                impares += 1
    if total > 0:
        porcentaje = (impares * 100) / total  
        return porcentaje
    else:
        return 0  # Si no hay elementos, devuelve 0

def simetrica_principal(matriz):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas cuadrada.

    Postcondiciones:
    - Devuelve True si la matriz es simétrica respecto a su diagonal principal.
    - Devuelve False si la matriz no es simétrica respecto a su diagonal principal.
    """
    tamanio = len(matriz)
    for i in range(tamanio):
        for j in range(tamanio):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def simetrica_secundaria(matriz):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas cuadrada.

    Postcondiciones:
    - Devuelve True si la matriz es simétrica respecto a su diagonal secundaria.
    - Devuelve False si la matriz no es simétrica respecto a su diagonal secundaria.
    """
    tamanio = len(matriz)
    for i in range(tamanio):
        for j in range(tamanio):
            if matriz[i][j] != matriz[tamanio - 1 - j][tamanio - 1 - i]:
                return False
    return True

def columnas_palindromas(matriz):
    """
    Precondiciones:
    - 'matriz' debe ser una lista de listas.

    Postcondiciones:
    - Devuelve una lista de índices de columnas que son palíndromas.
    """
    palindromas = []
    tamanio = len(matriz)
    for columna in range(tamanio):  
        es_palindromo = True
        for i in range(tamanio // 2):  # Solo itero hasta la mitad
            if matriz[i][columna] != matriz[tamanio - 1 - i][columna]:
                es_palindromo = False
                break
        if es_palindromo:
            palindromas.append(columna + 1)  # +1 para mostrar la columna en base 1
    return palindromas

def main() -> None:
    """
    Precondiciones:
    - Ninguna.

    Postcondiciones:
    - Ejecuta el programa principal para manejar la matriz.
    """
    tamanio = int(input("Ingrese el tamaño de la matriz (N x N): "))
    matriz = cargar_matriz(tamanio)
    
    print(f"\n{matriz}")
    ordenar_filas(matriz)
    print(f"\n{matriz}")

    fila1 = int(input("\nIngrese el número de la primera fila a intercambiar: ")) - 1
    fila2 = int(input("Ingrese el número de la segunda fila a intercambiar: ")) - 1
    intercambiar_filas(matriz, fila1, fila2)
    print(f"\n{matriz}")

    columna1 = int(input("\nIngrese el número de la primera columna a intercambiar: ")) - 1
    columna2 = int(input("Ingrese el número de la segunda columna a intercambiar: ")) - 1
    
    if (columna1 < 0 or columna1 >= tamanio) or (columna2 < 0 or columna2 >= tamanio):
        print("\nError! Uno o ambos índices de columna están fuera de rango.")
        return

    intercambiar_columnas(matriz, columna1, columna2)
    print(f"\n{matriz}")

    transponer_matriz(matriz)
    print(f"\n{matriz}")

    fila_promedio = int(input("\nIngrese el número de la fila para calcular el promedio: ")) - 1
    promedio = promedio_fila(matriz, fila_promedio)
    print(f"El promedio de la fila {fila_promedio + 1} es: {promedio}")
    
    if (fila1 < 0 or fila1 >= tamanio) or (fila2 < 0 or fila2 >= tamanio):
        print("\nError! Uno o ambos índices de fila están fuera de rango.")
        return

    columna_porcentaje = int(input("\nIngrese el número de la columna para calcular el porcentaje de impares: ")) - 1
    
    if (columna_porcentaje < 0) or (columna_porcentaje >= tamanio):
        print("\nError! El índice de la columna está fuera de rango.")
        return

    porcentaje_impares = porcentaje_impares_columna(matriz, columna_porcentaje)
    print(f"\nEl porcentaje de elementos impares en la columna {columna_porcentaje + 1} es: {porcentaje_impares:.2f}%")

    resultado_simetrica_principal = simetrica_principal(matriz)
    print(f"La matriz es simétrica respecto a su diagonal principal: {resultado_simetrica_principal}")

    resultado_simetrica_secundaria = simetrica_secundaria(matriz)
    print(f"La matriz es simétrica respecto a su diagonal secundaria: {resultado_simetrica_secundaria}")

    resultado_columnas_palindromas = columnas_palindromas(matriz)
    print(f"Las columnas que son palíndromas son: {resultado_columnas_palindromas}")

if __name__ == "__main__":
    main()
