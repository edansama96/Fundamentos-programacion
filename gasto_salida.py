def gasto(nombre:str="Carmen",dinero_salida:float=23,dinero_llegada:float=12.75)->float:
    """Función para poder calcular el dinero que se tiene como resultado de una 
    salidad, se urilizan variables flotantes y se optiene una variable flotante"""
    residuo=dinero_salida - dinero_llegada

    return f"La cantidad de dinero que {nombre} gasto es: {residuo} Euros"
print(gasto())
