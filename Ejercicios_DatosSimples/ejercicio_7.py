# EJERCICIO 7 - CALCULO MASA CORPORAL
peso = int(input('Ingrese su peso en Kg: '))
altura = float(input('Ingrese su altura en metros: '))
print(f"Su indice de masa corporal 'IMC' es: {round(peso/(altura*altura),2)}")