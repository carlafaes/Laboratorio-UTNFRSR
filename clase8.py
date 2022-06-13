#ciclo while 
contador = 0
while contador < 3:
    print('Ejecutamos neustro ciclo while ',contador)
    contador += 1
else:
    print('Fin del ciclo while')


#imprimir numeros del 0 al 5 con el cilo while
maximo = 5
contador = 0
while contador <= maximo:
    print(contador)
    contador += 1

#imprimir numeros del 5 al 0 con el cilo while
minimo = 1
contador = 5
while contador >= minimo:
    print(contador)
    contador -= 1


#Ciclo for
cadena = 'Hello'
for letra in cadena:
    print(letra)
else:
    print('Fin del ciclo for')

#break
for letra in 'Alemania':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break
    else:
        print('fin del ciclo for')