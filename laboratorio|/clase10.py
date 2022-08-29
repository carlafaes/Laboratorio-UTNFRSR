##Ejercicio 5:
numero= int(input("Ingrese un numero: "))
factorial=1
if numero != 0:
    for i in range(1,numero+1):
        factorial=factorial*i
    print("El factorial de",numero,"es:",factorial)

##Ejercicio 6:
# num=0
# suma_pares=0
# conteo_pares=0
# suma_impares=0
# conteo_impares=0
# promedio_impares=float(0)

# listaNumeros=[]
# num=int(input("Ingrese un numero: "))
# listaNumeros.append(num)
# decision= input("Desea ingresar otro numero? (s/n): ")
# while decision=="s" or decision == "S":
#     num=int(input("Ingrese otro numero: "))
#     listaNumeros.append(num)
#     decision= input("Desea ingresar otro numero? (s/n): ")

# for i in listaNumeros:
#     if i%2 == 0:
#         suma_pares += i
#         conteo_pares += 1
#     else:
#         suma_impares += i
#         conteo_impares += 1
#     i += 1
# promedio_impares=suma_impares/conteo_impares
# if conteo_pares:
#     print("El conteo de los pares es:", conteo_pares)
#     print("La suma de los pares es:", suma_pares)
# else:
#     print("No se han digitado numeros pares")
# if conteo_impares:
#     print("El conteo de los impares es:", conteo_impares)
#     print("El promedio de los impares es:", promedio_impares)
# else:
#     print("No se han digitado numeros impares")




#Ejercicio 7:
# i=1
# horas=0
# tarifa=float(0)
# salario=float(0)
# suma=float(0)



# while i <= 5:
#     horas=int(input("Ingrese el numero de horas trabajadas: "))
#     tarifa=int(input("Ingrese la tarifa por hora: "))
#     salario=horas*tarifa
#     print("El salario es: ",salario)
#     suma+=salario
#     i+=1

# print("El total de salarios es: ",suma)