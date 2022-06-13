miVariable= 3
print(miVariable)
miVariable='Hola a todos'
print(miVariable)
miVariable=3.5
print(miVariable)
x= 10
y=2
z=x + y
print(id(x))
#Las literales se escriben x528, la variable y=x272, la variable z = x592
print(id(y))

print(id(z))

#Manejo de cadenas 
miGrupoFavorito= 'The letter black'
print("Mi grupo favorito es " + miGrupoFavorito)

numero1= "7"
numero2= "8"
print(int(numero1) + int(numero2))

#Tipos de booleanos
miBool= 21 < 23
print(miBool)

if miBool:
    print('El resultado es verdadero')
else:
    print('El resultado es falso')

#Procesar la entrada del usuario
resultado = input("Digite un numero") #regresa un dato tipo string
print(resultado)

#Copnversion de la entrada de datos
numero1_=int(input('Escribe el primer numero: '))
numero2_=int(input('Escribe el segundo numero: '))
resultado= numero1_ + numero2_
print('El resultado de la suma es ', resultado)