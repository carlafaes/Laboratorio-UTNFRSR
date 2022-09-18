seleccionArgentina={
    10:{'Nombre':'Lionel Messi', 'edad':35,'Altura':1.70,'precio':'50 millones'},
    11:{'Nombre':'Angel Di Maria', 'edad':34,'Altura':1.80,'precio':'30 millones'},
    24:{'Nombre':'Paulo Dybala', 'edad':28,'Altura':1.77,'precio':'40 millones'},
    19:{'Nombre':'Nicolas Otamendi','edad':34,'Altura':1.83,'precio':'3.5 millones'},
    1:{'Nombre':'Franco Armani','edad':35,'Altura':1.89,'precio':'3.5 millones'}
}

#recorremos diccionario con ciclo for

for i in seleccionArgentina:
    print(f"{i} -> {seleccionArgentina[i]}")