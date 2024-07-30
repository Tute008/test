#
dinero = float(input('Ingrese capital depositado:'))
porcentaje = float(round(((dinero*4)/100),2))
dinero += porcentaje
print('Su interes anual es de uun 4%')
print(f"El primer anio su capital sera de {round((dinero),2)}")
print(f"El segundo anio su capital sera de {round((dinero + porcentaje),2)}")
dinero += porcentaje
print(f"El segundo anio su capital sera de {round((dinero + porcentaje),2)}")