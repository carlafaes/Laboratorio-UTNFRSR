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

# para eliminar la tupla
del cocina

