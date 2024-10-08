#Voy a calcular tu salario según el número de horas que trabajas
print("Dime la cantidad de horas que trabajas a la semana")
horas = int(input())
salario=float(9.50)
semanas= int(4)
salario_mensual = horas * salario  * semanas
print("Tu salario mensual es de", salario_mensual , "€")