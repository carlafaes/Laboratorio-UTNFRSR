#Ejercicio de natematicas
#Para sacar la raiz cuadrada de un numero positivo
import math


numero=int(input("Digite un numero positivo: "))
while numero < 0:
    print("Error -> Deberia ser un numero positivo")
    numero= int(input("Digite un numero positivo: "))
print(f"\nSu raiz cuadrada es: {math.sqrt(numero)}")