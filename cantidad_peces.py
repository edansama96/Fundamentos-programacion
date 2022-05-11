def num_peces(peces_azules:int=163,peces_rojos:int=284):
    """Función para determinar la cantidad de peces en una pesera
    con colores azules y rojos, por lo cual se utiliza una variable 
    para cada pez de diferente color."""
    adicion= peces_azules+peces_rojos
    return adicion
print("La cantidad de peces son: ",num_peces())