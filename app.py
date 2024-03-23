numeros = []

for i in range(10):
    num = float(input("Ingresa el número " + str(i+1) + ": "))
    numeros.append(num)
if len(numeros) != 0:
    promedio = sum(numeros) / len(numeros)
    print("El promedio de los números ingresados es: " + str(promedio))

else:
     print("valor deber ser diferente de cero ")
    
    



