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

# tuplas
# definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(cocina)
print(len(cocina))

# acceder a un elemento de la tupla
print(cocina[0])
# acceder a un rango
print(cocina[0:1])
# sale en consola ('cuchara',)
# porque necesita una coma para ser considerado una tupla, de otra manera se consideraria un string

# recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar)
    # en lugar de q imprima un salto de linea luego del elemento, imprime un espacio
    print(cocinar, end=' ')

# como modificar una tupla
# se debe hacer un conversion de tupla a lista, modficacion, y nuevamente de lista a tupla,(de todas maneras, no es buena practica el modificar una tupla)
cocinaModificada = list(cocina)
cocinaModificada[0] = 'Plato'
cocina = tuple(cocinaModificada)
print(cocina)

#para eliminar la tupla
del cocina