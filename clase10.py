##Ejercicio 5:
# numero= int(input("Ingrese un numero: "))
# factorial=1
# if numero != 0:
#     for i in range(1,numero+1):
#         factorial=factorial*i
#     print("El factorial de",numero,"es:",factorial)

##Ejercicio 6:
n_elementos= int(input("Ingrese el numero de elementos: "))
i=1
num=0
suma_pares=0
conteo_pares=0
suma_impares=0
conteo_impares=0
promedio_impares=float(0)

for i in range(1,n_elementos+1):
    num=int(input("Ingrese un numero: "))
    if num%2==0:
        suma_pares+=num
        conteo_pares=conteo_pares+1
    else:
        suma_impares+=num
        conteo_impares=conteo_impares+1
    i=i+1
    if conteo_pares==0:
        print("El conteo de los pares es:", conteo_pares)
        print("La suma de los pares es:", suma_pares)
    else:
        print("No se han digitado numeros pares")
    if conteo_impares==0:
        print("El conteo de los impares es:", conteo_impares)
        promedio_impares=suma_impares/conteo_impares
        print("El promedio de los impares es:", promedio_impares)
    else:
        print("No se han digitado numeros impares")