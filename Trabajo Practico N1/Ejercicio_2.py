'''
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función
'''

def es_bisiesto(anio):
    """
    Precondiciones:
    - 'anio' es un número entero positivo.
    
    Postcondiciones:
    - Devuelve True si el año es bisiesto según las reglas del calendario.
    - Devuelve False si el año no es bisiesto.
    """
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def validar_fecha(dia, mes, anio):
    """
    Precondiciones:
    - 'dia', 'mes' y 'anio' son números enteros positivos.
    
    Postcondiciones:
    - Devuelve True si la fecha es válida según el calendario.
    - Devuelve False si la fecha no es válida.
    """
    dias_del_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Cambio la cantidad de días de Febrero de 28 a 29, en el caso de que el año sea bisiesto
    if es_bisiesto(anio):
        dias_del_mes[1] = 29
    if (dia < 1 or dia > dias_del_mes[mes - 1]) or (mes < 1 or mes > 12) or (anio < 1800 or anio > 3000):
        return False
    return True

def main() -> None:
    """
    Precondiciones:
    - Ninguna.
    
    Postcondiciones:
    - Solicita al usuario que ingrese un día, mes y año.
    - Llama a la función 'validar_fecha' con los valores ingresados.
    - Muestra si la fecha es válida o no.
    """
    dia = int(input("Ingrese un día del mes: "))
    mes = int(input("Ingrese un mes del año: "))
    anio = int(input("Ingrese un año: "))
    
    if validar_fecha(dia, mes, anio):
        print("\nFecha válida.")
    else:
        print("\nFecha no válida.")

if __name__ == "__main__":
    main()
