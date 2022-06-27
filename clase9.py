##Diseñar un programa que ingresado un año, nos devuelva por consola si es un año bisiesto o no, repetir la accion hasta que el usuario ingrese un año que no sea bisiesto.

num=0
opcion=0

while opcion != 1:
    num=int(input("Ingrese un año: "))
    if( num%4 == 0 and num%100 != 0 or num%400 == 0 ):
        print(f"El año {num} es bisiesto")
    else:
        print(f"El año {num} no es bisiesto")
    opcion=int(input("Desea ingresar otro año? (0=yes/1=no): "))
