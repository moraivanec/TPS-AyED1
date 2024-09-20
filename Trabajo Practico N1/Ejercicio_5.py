'''
Escribir funciones lambda para:
a. Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo
6 es oblongo porque resulta de multiplicar 2 * 3.
b. Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecutivos
comenzando desde 1. Por ejemplo 10 es un número triangular porque se obtiene
sumando 1+2+3+4.
Ambas funciones lambda reciben como único parámetro el número a evaluar y devuelven
True o False. No se permite utilizar ayudas externas a las mismas.
'''

numeros = [6, 10, 23, 28, 32]

"""
Precondiciones:
- 'x' debe ser un número entero positivo.
- No se permiten números negativos, ni 0.

Postcondiciones:
- Devuelve True si 'x' es un número oblongo.
- Devuelve False si 'x' no es un número oblongo
"""
oblongo = lambda x: (lambda k: False if k * (k + 1) > x else True if k * (k + 1) == x)

"""
Precondiciones:
- 'x' debe ser un número entero positivo.
- No se perimiten números negativos, ni 0.

Postcondiciones:
- Devuelve True si 'x' es un número triangular.
- Devuelve False si 'x' no es un número triangular.
"""
triangular = lambda x: (lambda k: False if k * (k + 1) // 2 > x else True if k * (k + 1) // 2 == x)

for numero in numeros:
    print(f"El número {numero} es oblongo: {oblongo(numero)}")
    print(f"El número {numero} es triangular: {triangular(numero)}")

# No se cómo terminar de resolver este ejercicio :(
    
