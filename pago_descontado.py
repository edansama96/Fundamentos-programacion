def pago_descuento(precio_pagado:int=34,descuento_hecho:int=15):
    porcentaje=100
    porcentaje_pago=porcentaje-descuento_hecho
    precio_original=(precio_pagado*porcentaje)/porcentaje_pago
    
    return precio_original
print("El precio origianl era de :",pago_descuento(),"Euros")