#Ejercicio 8: Menu interactivo - Cajero automatico
#Hacer un programa que simule un cajero automatico con un saldo
#Inicial de $1000 y tendra el siguiente menu de opciones:
# 1-Ingresar dinero en la cuenta
# 2- Retirar dinero de la cuenta
# 3- Mostrar dinero de la cuenta
# 4-Salir
saldo=1000
while True:
    print("\t.:MENU;.")
    print("1-Ingresar dinero en la cuenta")
    print("2- Retirar dinero de la cuenta")
    print("3- Mostrar dinero de la cuenta")
    print("4-Salir")
    opcion= int(input("Digite un opcion de menu: "))
    print()
    if opcion == 1:
        extra=float(input("Cuanto dinero desea ingresar? ->"))
        saldo+=extra
        print(f"Su saldo actual es: {saldo}")
    elif opcion == 2:
        retirar= float(input("Cuanto dinero desear retirar? -> "))
        if retirar > saldo:
            print("No tienes esa cantidad de dinero en tu cuenta")
        else:
            saldo = saldo - retirar
            print(f"Su saldo actual es: {saldo}")
    elif opcion == 3:
        print(f"Su saldo actual es de: {saldo}")
    elif opcion == 4:
        print("Gracias por utilizar su cajero automatico,hasta pronto!")
        break
    else:
        print("Error, la opcion elegida no existe")
        print()