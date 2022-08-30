# Tipo set o conjunto
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
# Revisar si un elemento existe dentro de set
print('Marte' in planetas)  # retorna un booleano que devuelve True o False
print('Jupiter' not in planetas)

# Agregar un elemento al conjunto
planetas.add('Tierra')
print(planetas)

# Eliminar elementos, puede arrojar un error si el elemento no existe
planetas.remove('Jupiter')
print(planetas)
planetas.discard('Venus')
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
