def matriz_a(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    for i in range(tamanio):
        fila = [0] * tamanio
        if i < 3:  
            fila[i] = 2 * i + 1  # Para las filas 0, 1 y 2, asigna 1, 3, 5
        elif i == 3:  
            fila[-1] = 7  # # Para la fila 3, asigna 7 a la última columna
        matriz.append(fila)
    return matriz

def matriz_b(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    for i in range(tamanio):
        fila = [0] * tamanio # Inicia una fila de 0
        if (i == 0) and (tamanio > 0):
            fila[-1] = 27 # Asigna el número 27 a la última columna de l aprimera fila
        elif (i == 1) and (tamanio > 1):
            fila[-2] = 9 # Asigna el número 9 a la anteúltima columna de la segunda fila
        elif (i == 2) and (tamanio > 2):
            fila[1] = 3 # Asignsa el número 3 a la segunda columna de la tercera fila
        elif (i == tamanio - 1) and (tamanio > 0):
            fila[0] = 1 # Asigna el número 1 a la primera columna de la última fila
        matriz.append(fila)
    return matriz

def matriz_c(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    for i in range(tamanio):
        fila = [0] * tamanio
        for j in range(tamanio):
            if i + j < tamanio: # Rellena la fila según el patrón
                fila[j] = tamanio - i
        matriz.append(fila)
    return matriz

def matriz_d(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    for i in range(tamanio, 0, -1):
        fila = [i] * tamanio # cada fila tiene el mismo número
        matriz.append(fila)
    return matriz

def matriz_e(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    for i in range(tamanio):
        fila = [0] * tamanio
        for j in range(tamanio):
            fila[j] = (i * 2 + j) % tamanio # Asigna valores según el patrón
        matriz.append(fila)
    return matriz

def matriz_f(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    valor = 1
    for j in range(tamanio - 1, -1, -1): # Recorre las columnas de atrás hacia adelante
        fila = []
        for i in range(tamanio - 1, -1, -1): # Recorre las filas de atrás hacia adelante
            if i + j >= tamanio - 1: 
                fila.append(valor)
                valor += 1 # Incrementa el valor para la próxima posición
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

def matriz_g(tamanio):
    """
    Precondiciones:
    - 'tamanio' debe ser un número entero positivo.

    Postcondiciones:
    - Devuelve una matriz de enteros de tamaño 'tamanio' x 'tamanio' con un patrón específico.
    """
    matriz = []
    valor = 1
    for i in range(tamanio):
        fila = [0] * tamanio
        for j in range(tamanio):
            if i % 2 == 0:
                fila[j] = valor # Si la fila es par, llena de izquierda a derecha
            else:
                fila[tamanio - j - 1] = valor # Si la fila es impar, llena de derecha a izquierda
            valor += 1
        matriz.append(fila)
    return matriz

def main() -> None:
    tamanio = 4  # Cambio el tamaño de la matriz como sea necesario
    
    print("Matriz A:")
    print(matriz_a(tamanio))
    
    print("\nMatriz B:")
    print(matriz_b(tamanio))

    print("\nMatriz C:")
    print(matriz_c(tamanio))

    print("\nMatriz D:")
    print(matriz_d(tamanio))

    print("\nMatriz E:")
    print(matriz_e(tamanio))

    print("\nMatriz F:")
    print(matriz_f(tamanio))

    print("\nMatriz G:")
    print(matriz_g(tamanio))
    
if __name__ == "__main__":
    main()
