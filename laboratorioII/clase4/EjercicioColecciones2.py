#Ejercicio 2: operaciones de conjuntos con lista
#Escriba un programa que tenga 2 listas y que a continuacion cree las siguientes listas(en las que  no debe haber elementos repetidos)
#1- Lista de palabras que aparecen en las listas
#2-lista de palabras que aparecen en la primera lista, pero no en la segunda
#3- lista de palabras que aparecen en la segunda lista, pero no en la primera
#4-lista de palabras que aparecen en ambas listas

lista1= [1,2,3,4,5,5,6,7,1,2,3]
lista2=[8,8,8,8]

#eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1=set(lista1)
conjunto2=set(lista2)

union= list(conjunto1 | conjunto2)
soloLista1= list(conjunto1 - conjunto2)
soloLista2= list(conjunto2 - conjunto1)
interseccion = list(conjunto1 & conjunto2)

print(f"Lista de palabras que aparecen en las listas: {union}")
print(f"lista de palabras que aparecen en la primera lista, pero no en la segunda: {soloLista1}")
print(f"lista de palabras que aparecen en la segunda lista, pero no en la primera: {soloLista2}")
print(f"lista de palabras que aparecen en ambas listas: {interseccion}")