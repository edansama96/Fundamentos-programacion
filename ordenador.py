def ordenador_precio(precio_ordenador:int=660,descuento:int=10)->float:
    """Programa para calcular el valor de descuento de un elemento
    y con esto saber cuanto es el precio que se debe pagar"""
    valor_descuento=(precio_ordenador*descuento)/100
    valor=precio_ordenador-valor_descuento
    return valor,type(valor)
    
print("El valor del ordenador es: ",ordenador_precio()," Euros")