#solo cuento lestras de nombre
nombre = str(input('ingrese su nombre: '))
nombre = nombre.upper()
print("EL nombre",nombre, "tiene", (len(nombre)), "letras")

#descuento los espacios para saber cantidad de letras del nombre completo
nombre_completo = str(input('ingrese su nombre completo: '))
nombre_completo = nombre_completo.upper()
contador = nombre_completo.count(" ")
contador_total = ((len(nombre_completo)) - contador)
print(contador)
print("EL nombre",nombre_completo, "tiene", contador_total, "letras")