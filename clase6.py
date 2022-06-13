#Ejercicio calcular la estacion del año
mes = int(input('Digite un mes del año (1 - 12') )
estacion= None

if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion == 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion= 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:
    estacion = 'Error no hay numero para ese mes'

print(f'Para el mes {mes} la estacion es:{estacion}')

#Ejercicio Etapas de vida segun la edad
edad=int(input('Digite su edad: '))
mensaje = None

if 0 <= edad < 10: #sintaxis simplificada
    mensaje= 'La infancia es increible y bella'
elif 10 <= edad < 20:
    mensaje = 'Tienes muchos cambios,mucho que estudiar'
elif 20 <= edad < 30:
    mensaje='Amor y comienza el trabajo'
else:
    mensaje='Erro estapa de vida no reconocida'

print(f'Tu edad es: {edad}, {mensaje}')

#Ejercicio: sistema de calificaciones
calificacion= int(input('Digite una calificacion entre 0  y 10 :'))

if 9 <= calificacion <= 10:
    print('A')
elif 8 <= calificacion < 9:
    print('B')
elif 7 <= calificacion < 8:
    print('C')
elif 6 <= calificacion < 7:
    print('D')
elif 0 <= calificacion < 6:
    print('F')
else:
    print('Valor incorrecto')
