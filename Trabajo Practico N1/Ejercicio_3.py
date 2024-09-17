'''
Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas
decrecientes (detalladas en la tabla de abajo) se solicita desarrollar una función que
reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un programa para
verificar el comportamiento de la función.
'''

def calcular_gastos(viajes):
    # Valor actualizado de tarifa: $650
    tarifa = 650
    if viajes >= 1 and viajes <= 20:
        costo_total = tarifa * viajes
    elif viajes >= 21 and viajes <= 30:
        tarifa_con_descuento = tarifa * 0.80 # 20% de descuento
        costo_total = tarifa_con_descuento * viajes
    elif viajes >= 31 and viajes <= 40:
        tarifa_con_descuento = tarifa * 0.70 # 30% de descuento
        costo_total = tarifa_con_descuento * viajes
    elif viajes > 40:
        tarifa_con_descuento = tarifa * 0.60 # 40% de descuento
        costo_total = tarifa_con_descuento * viajes
    else:
        costo_total = 0
    return costo_total
        
viajes = int(input("Ingrese la cantidad de viajes que realizó en el mes: "))
if viajes < 0:
    print("\nNúmero de viajes no válido.")
else:
    gasto_total = calcular_gastos(viajes)
    print(f"\nGasto total del mes: ${gasto_total:.2f}.")
        
