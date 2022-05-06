#Programa para calcular el CDT
#Para el caso en el cual se cumplio el tiempo de más dos meses
#Entradas
print("Programa para Calcular El valor del CDT")
#variables
def CDT("AB1012",1000000,3)
usuario=input("Ingrese el nombre del usaurio :")
cantidad=int(input("Ingrese el capital de la cuenta :"))
tiempo=int(input("Ingrese el tiempo del CDT :"))
#Constante
#3%
porcentaje_de_interes=0.03
porcentaje_de_perdida=0.02
#condicionales y programa
if tiempo>=3:
#formulas para un tiempo mayor o igual a 3 meses
    valor_interes=(cantidad*porcentaje_de_interes*tiempo)/12
    valor_total=cantidad+valor_interes
    print("Para el usuario",usuario,"La cantidad de dinero a recibir, según el monto incial",cantidad,"para un tiempo de",tiempo,"meses es :",valor_total)
elif tiempo<=2:
    valor_a_perder=CDT*porcentaje_de_perdida
    valor_total_perdida=cantidad-valor_a_perder
    print("Para el usuario",usuario,"La cantidad de dinero a recibir, según el monto inicial",cantidad,"para un tiempo de",tiempo,"meses es :",valor_total_perdida)
else:
    print("Escribio algún valor erroneo")
    
    
    
