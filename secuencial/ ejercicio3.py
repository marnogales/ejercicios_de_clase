#Esto es un programa para el cálculo del IMC
print("Dime cuál es tu peso en kilogramos")
peso = float(input())
print("Genial, ahora dime tu altura en metros")
altura = float(input())
#Realizamos la operación
IMC = peso / (altura * altura) 
print("Tu IMC es", IMC, "kg/m")
