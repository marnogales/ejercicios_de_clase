print("Dime un número de la tabla de multiplicar:")
num=int(input())
indice=1
while(indice < 11):
    resultado=num*indice
    print(indice,"x",num,"=",resultado)
    indice=indice +1
print("fin")
