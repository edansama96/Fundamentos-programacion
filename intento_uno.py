def CDT(usuario,cantidad,tiempo):
    interes_promedio=0.03
    perdida_promedio=0.02
    promedio=cantidad*interes_promedio
    if tiempo>=3:
        valor_interes=(cantidad*interes_promedio*tiempo)/12
        valor_total=cantidad+valor_interes
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valor_total:.1f}"
    elif tiempo<=2:
        valor_a_perder=cantidad*perdida_promedio
        valor_total=cantidad-valor_a_perder
        return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {round(valor_total,1):.1}"
    else:
        print("Error")


print(CDT("AB1012",1000000,3))
