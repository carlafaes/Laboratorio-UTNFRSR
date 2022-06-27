##Diseñar un programa que ingresado un año, nos devuelva por consola si es un año bisiesto o no, repetir la accion hasta que el usuario ingrese un año que no sea bisiesto.

# num=0
# opcion=0

# while opcion != 1:
#     num=int(input("Ingrese un año: "))
#     if( num%4 == 0 and num%100 != 0 or num%400 == 0 ):
#         print(f"El año {num} es bisiesto")
#     else:
#         print(f"El año {num} no es bisiesto")
#     opcion=int(input("Desea ingresar otro año? (0=yes/1=no): "))



##Calcular la suma de "N" primeros numeros

# N=int(input("Digite la cantidad de numeros: "))
# suma=0
# while N > 0:
#     num=int(input("Digite el numero: "))
#     suma+=num
#     N-=1
# print(f"La suma de los numeros es: {suma}")

#Ejercicio 3: Leer 10 numeros e imprimir cuantos son positivos, #cuantos son negativos y cuantos son neutros(cero).

i=10
conteo_positivo=0
conteo_negativo=0
conteo_neutros=0

num=int(input("Digite un numero: "))

while i > 0:
    if num > 0:
        conteo_positivo+=1
    elif num < 0:
        conteo_negativo+=1
    else:
        conteo_neutros+=1
    i-=1
    num=int(input("Digite un numero: "))

print(f"Los numeros positivos son: {conteo_positivo}")
print(f"Los numeros negativos son: {conteo_negativo}")
print(f"Los numeros neutros son: {conteo_neutros}")