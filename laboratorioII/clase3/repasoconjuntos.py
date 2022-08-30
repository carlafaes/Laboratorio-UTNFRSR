# repaso de set o conjunto
# para definir un conjunto
conjunto = set()
# conjunto1={}##no se puede modificar con add xq ya se inicializo vacio
conjunto1 = {'string', }  # se puede modificar porque ya contiene un elemento
conjunto2 = set()
conjunto2.add(6)
conjunto.add(7)
conjunto.add('hola')
print(conjunto)
print(3 not in conjunto1)

# como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto)  # nos devuelve como respuesta un booleano

# operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # que elemento tienen en comun
print(conjunto3)

# asigna el valor que esta en el conjunto 1 y no en el conjunto2
conjunto3 = conjunto1 - conjunto2
print(conjunto3)

# elementos que no se comparten o que son diferentes entre ambos
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
# aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))

# preguntamos si los elementos del conjunto1 estan dentro del conjunto3
print(conjunto3.issuperset(conjunto1))

# como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))

# convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # esto hace que el conjunto sea totalmente inmutable
# no se puede agregar, modificar ni eliminar elementos

# Repaso diccionarios
diccionarioNuevo = {'azul': 'rojo', 'amarillo': 'rosa', 'verde': 'naranja'}

# como eliminar elemento
del (diccionarioNuevo['azul'])
print(diccionarioNuevo)
# los diccionarios aceptan diferentes tipos de elementos
diccionario2 = {'Ariel': {'edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia':[35,1.67]}
print(diccionario2)

seleccionArgentina={
    10:{'Nombre':'Lionel Messi', 'edad':35,'Altura':1.70,'precio':'50 millones'},
    11:{'Nombre':'Angel Di Maria', 'edad':34,'Altura':1.80,'precio':'30 millones'},
    24:{'Nombre':'Paulo Dybala', 'edad':28,'Altura':1.77,'precio':'40 millones'}
}
print(seleccionArgentina)

for key in seleccionArgentina:
    print(key)

#ejercicio 1: agregar elementos al diccionario
seleccionArgentina[25]={'Nombre':'Marcos Senesi','edad':25,'Altura':1.78,'precio':'17 millones'}
print(seleccionArgentina)
seleccionArgentina[6]={'Nombre':'German Pezzella','edad':31,'Altura':1.78,'precio':'5 millones'}
seleccionArgentina[8]={'Nombre':'Marcos Acuña','edad':30,'Altura':1.78,'precio':'18 millones'}
seleccionArgentina[3]={'Nombre':'Nicolas Tagliafico','edad':30,'Altura':1.78,'precio':'11 millones'}
print(seleccionArgentina)