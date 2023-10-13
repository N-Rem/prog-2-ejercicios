# Escribe un programa que solicite al usuario ingresar las calificaciones de un grupo de estudiantes. El programa debe permitir al usuario ingresar calificaciones una por una, y debe detenerse cuando el usuario ingrese un valor negativo o cuando se hayan ingresado 10 calificaciones, lo que ocurra primero.

# Una vez que se hayan ingresado las calificaciones, el programa debe calcular y mostrar lo siguiente:

# La cantidad de calificaciones ingresadas.
# El promedio de las calificaciones ingresadas.
# Cuántas calificaciones están por encima del promedio y cuántas están por debajo del promedio.

lista_notas = []


def ingresar_notas(notas):
    for i in range(5):
        while True:
            try:
                nota = int(input("Ingrese la nueva nota: "))
                if nota > 10:
                    print("Dato mal ingresado, ingrese un numero entre el 1 y el 10")
                else:
                    break
            except ValueError:
                print("Ingrese un valor valido numerico entero..")
        if (nota < 0):
            break
        notas.append(nota)

def calcula_promedio(lista, cant_item):
    sumatoria = 0
    for i in lista:
        sumatoria += i
    prom = sumatoria/cant_item
    return prom

def compara_promedio(lista, promedio):
    list_menor_prom = []
    list_mayor_prom = []
    for i in lista:
        if i > promedio:
            list_mayor_prom.append(i)
        else:
            list_menor_prom.append(i)
    return list_menor_prom, list_mayor_prom

ingresar_notas(lista_notas)
print(lista_notas)

cant_notas = len(lista_notas)
print(f"la cantidad de notas ingresas fue: {cant_notas}")

prom_notas = calcula_promedio(lista_notas, cant_notas)

print(f"El promedio de las notas es: {prom_notas}")

menor_prom, mayor_prom=compara_promedio(lista_notas,prom_notas)

print(f"Las notas mayores al promedio {prom_notas} fue: {mayor_prom}. \nLas notas menores la promedio fueron {menor_prom}")
