'''
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
'''

def num_mayor(a, b, c):
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
        
    mayor_unico = (mayor != a) + (mayor != b) + (mayor != c)
    if mayor_unico == 2:
        return mayor
    else:
        return -1


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
    
resultado = num_mayor(a, b, c)
if resultado == -1:
    print("\nNo se encuentra un mayor estricto.")
else:
    print(f"\nEl número mayor es: {resultado}.")
        

        