def precio_verificado(peso_producto:int=100,precio_producto:float=5.95,peso_gramos:int=1000)->float:
    """Función que permite re calcular el precio de un producto al saber la cantidad de gramos, el precio del 
    producto y la cantidad de gramos"""
    precio_real=(precio_producto*peso_gramos)/peso_producto
    return precio_real
print("El precio real del producto es:", precio_verificado())