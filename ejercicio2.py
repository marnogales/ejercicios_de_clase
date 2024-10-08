#Esto es un programa para calcular propinas
print("dime la cantidad de tu factura")
factura=int(input())
porcentaje=float(15.0)
#Realizamos la operación
propina = factura * (porcentaje / 100) 
print("la propina es", propina, "€")