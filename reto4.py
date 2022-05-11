from math import ceil


def refrescos(cajas:int=9, cantidad:int=24, invitados:int=56)->int:
    """Programa para calcular la cantidad exacta de refrescos a tomar"""
    cantidad_total=cajas*cantidad
    cantidad_a_dar=int(cantidad_total/invitados)
    cantidad_a_usar=invitados*cantidad_a_dar
    sobrantes=cantidad_total-cantidad_a_usar
    return  cantidad_a_dar
print("La cantidad exacta que por cada uno de los invitados de refresco que se debe tomar es:  ",refrescos())
    