#Colas con listas
#estructura de datos tipo FIFO

cola=['Ariel','Osvaldo','Natalia']

#agregamos elementos al final de la cola
cola.append('Jose')
cola.append('Pedro')
print(cola)

#sacamos elementos de la cola
seRetira= cola.pop(0)
print(cola)
print(f'Atendido el cliente {seRetira}')
seRetira= cola.pop(0)
print(cola)
print(f'Atendido el cliente {seRetira}')


