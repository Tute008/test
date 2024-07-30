# 
precio_pan = float(3.49)
descuento = float(0.6)
barras_viejas = int(input('Ingrese la cantidad de barras de ayer: '))
print(f"El precio de una barra del dia es {precio_pan}")
print(f"El precio de una barra vieja es {round((precio_pan * 0.6),2)}")
print(f"Todas las barras viejas tienen un coste de {round(((precio_pan*0.6)*barras_viejas),2)}")