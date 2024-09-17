'''
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
'''

def calcular_cambio(total, dinero_recibido):
    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    cambio = dinero_recibido - total
    
    denominaciones = []
    cantidades = []
    
    for billete in billetes:
        cantidad = cambio // billete
        if cantidad > 0:
            denominaciones.append(billete)
            cantidades.append(cantidad)
            cambio %= billete
    
    if cambio < 0:
        return -1
    if cambio != 0:
        return -2
    
    return denominaciones, cantidades

total = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

resultado = calcular_cambio(total, dinero_recibido)

if resultado == -1:
    print("\nEl dinero recibido es insuficiente.")
elif resultado == -2:
    print("\nEl cambio no puede entregarse debido a falta de billetes con denominaciones adecuadas.")
else:
    denominaciones, cantidades = resultado
    for i in range(len(denominaciones)):
        print(f"\nBilletes a entregar: {cantidades[i]} billetes de ${denominaciones[i]}.")
            
