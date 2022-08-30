#repaso de set o conjunto
#para definir un conjunto
conjunto= set()
#conjunto1={}##no se puede modificar con add xq ya se inicializo vacio
conjunto1={'string',}## se puede modificar porque ya contiene un elemento
conjunto2=set()
conjunto2.add(6)
conjunto.add(7)
conjunto.add('hola')
print(conjunto)
print(3 not in conjunto1)

#como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto)#nos devuelve como respuesta un booleano

#operaciones en conjuntos
conjunto3= conjunto1 | conjunto2 #la linea une los dos conjuntos
print(conjunto3)

conjunto3= conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3= conjunto1 - conjunto2 #asigna el valor que esta en el conjunto 1 y no en el conjunto2
print(conjunto3)

conjunto3=conjunto1 ^ conjunto2 #elementos que no se comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3= conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))#aqui preguntamos si un conjunto es un subconjunto dentro de otro

print(conjunto3.issuperset(conjunto1))#preguntamos si los elementos del conjunto1 estan dentro del conjunto3

#como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2))