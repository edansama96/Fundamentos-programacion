#Programa para calcular el CDT
#Para el caso en el cual se cumplio el tiempo de más dos meses
#Entradas
print("Programa para Calcular El valor del CDT")
#variables
usuario="AB1012"
capital=1000000
tiempo=3
#Constante
#3%
porcentaje_de_interes=0.03
#Formulas
valor_intereses=(capital*porcentaje_de_interes*tiempo)/12
valor_total=valor_intereses+capital
#Resultado
print("Para el usuario",usuario,"La cantidad de dinero a recibir,según el monto inicial",capital,"para un tiempo de",tiempo,"meses es:",valor_total)

#Para el caso en el cual no se cumplio el tiempo  minimo mayor de dos meses 
#Variables
usuario_cero= "ER3366"
capital_cero=650000
tiempo_cero=2
#Constantes de
#2%
porcentaje_de_perdida=0.02
#Formulas
valor_perder=capital_cero*porcentaje_de_perdida
valor_total_perdida=capital_cero-valor_perder
#Resultados 
print("Para el usuario",usuario_cero,"La cantidad de dinero a recibir, según el monto inicial",capital_cero,"para un tiempo de",tiempo_cero,"meses es :",valor_total_perdida)


