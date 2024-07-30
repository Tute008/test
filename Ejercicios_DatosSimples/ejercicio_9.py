# EJERCICIO 9
inversion = int(input('Cuanto dinero quieren invertir? '))
anos = int(input('Cuantos anos quieres invertir tu dinero? '))
print(f"Con un interes anual de 1.5% dentro de {anos} tendras {round(((((1.5*inversion)/100)*anos)+inversion),2)}")
