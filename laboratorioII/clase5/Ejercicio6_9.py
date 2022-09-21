#Ejercicio 9: Mostrar una frase sin espaios y contar su longitud
#Hacer un programa donde el usuario ingrese una frase, se le devolvera la misma frase pero sin espacion en blanco, y ademas un contador de cuantos caracteres tiene la frase (sin contar los espacion en blanco)
#Ejemplo: frase= vivir por siempre en paz
#        frase final= vivirporsiemprenpaz
# nº de caracteres= 21

frase1= input("Digite un frase: ")
frase2= " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"Nº de caracteres= {len(frase1)}")