def costo_cel(costo:int=420,porcentaje_aumento:int=20)->float:
    """Función para poder calcular 
    el costo de un celular al tener que pagar un 20% más"""
    aumento_porcentaje=(costo*porcentaje_aumento)/100
    costo_aumentado=costo+aumento_porcentaje
    return costo_aumentado
print("El costo al día siguiente del celular es: ",costo_cel(),"Euros")
    