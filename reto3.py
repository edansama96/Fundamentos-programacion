def Fidget_Spinner(vueltas:int=147,tiempo:int=640)->int:
    """Función que permite calcular la cantidad de vueltas que dara 
    un Fidget Spinner en un tiempo de 640 segundo o más o menos 10 minutos"""
    
    tiempo_a=60
    cantidad_vueltas=(vueltas*tiempo)/tiempo_a
    return int(cantidad_vueltas)
print("La cantidad de vueltas que puede hacer un Fidget Spinner son: ",Fidget_Spinner())
    