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
