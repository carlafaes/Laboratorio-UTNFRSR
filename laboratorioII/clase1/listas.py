# lista: Ariel,Liliana,Natalia,Osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)  # imprime toda la lista
print(nombres[0])  # imprime el primer elemento
print(nombres[-1])  # imprime ultimo elemento
print(nombres[0:2])  # muestra desde el indice cero hasta el 2 sin incluirlo
print(nombres[:3])  # muestra desde el indice cero hasta el 3,sin incluirlo
# modificamos un valor
nombres[2] = 'Pedro'
print(nombres)
# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('se terminaron los elementos de la lista')

# preguntamos cuantos elementos tiene la lista
print(len(nombres))
# agregamos un elemento al final de la lista
nombres.append('Car')
nombres.append([1, 2, 3, 4])  # crearia una lista anidada
nombres.append({'dato1': 'valor1', 'dato2': 'valor2'})
print(nombres)
# insertar un elemento en un indice especifico de la lista
nombres.insert(2, 'Juan')
print(nombres)
# eliminar el ultimo elemento
nombres.pop()
print(nombres)
# eliminar un elemento de un indice especifico
del nombres[2]
print(nombres)
# eliminar o limpiar todos los elementos de la lista
nombres.clear()
print(nombres)
# eliminar la lista
del nombres
# print(nombres)

# Concatenamos listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = lista1 + lista2
print(lista3)

lista3.extend([7, 8, 9])
print(lista3)

# buscar el indice de un elemento
lista4 = ['dato1', 'dato2', 'dato3', 'dato1']
print(lista3.index(5))  # devuelve 5
print(lista4.index('dato2'))  # devuelve 1

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista4.count('dato1'))#devulve 2

#Para poner al reves una lista
lista4.reverse()
print(lista4)

#para que una lista se multiplique repitiendo sus elementos
lista4=lista4 * 2
print(lista4)

#para ordenar una lista
##ordenar ascendentemente
lista3.sort()
print(lista3)
##ordenar descendentemente
lista3.sort(reverse=True)
print(lista3)
