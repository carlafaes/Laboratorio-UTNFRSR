# DICCIONARIOS
# esta compuesto por key:value
diccionario = {
    'IDE': 'Integrated Development Environment',
    'POO': 'Programacion Orientada a Objetos',
    'SABD': 'Sistema de Administracion de Base de Datos'
}
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer elementos del conjunto
for termino in diccionario:  # devuelve key
    print(termino)

for termino, valor in diccionario.items():  # devuelve key:valor
    print(termino, valor)

for termino in diccionario.keys():  # devuelve key
    print(termino)

for valor in diccionario.values():  # devuelve solo el value
    print(valor)

# comprobar la existencia de un elemento
print('IDE' in diccionario)  # devuelve un booleano
print('IDE' not in diccionario)  # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# quitamos un elemento
diccionario.pop('PK')
print(diccionario)

# vaciar un diccionario
diccionario.clear()

# eliminar diccionario
del diccionario
