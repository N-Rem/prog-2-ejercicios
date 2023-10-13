# Crea un programa que permita llevar un registro de estudiantes y sus calificaciones. El programa debe permitir al usuario realizar las siguientes operaciones:

# Agregar estudiantes y sus calificaciones al registro.
# Buscar la calificación de un estudiante en particular.
# Mostrar todas las calificaciones almacenadas en el registro.
# Calcular y mostrar el promedio de calificaciones de todos los estudiantes.
# Salir del programa.

alumnos = []

def creaAlumnos(alum_lis):
    validar = True
    name = input("ingrese el nombre del alumno: ")

    while (True):
        nota = input("ingrese la nota del alumno: ")
        es_num, nota=validaNumero(nota)
        if es_num:
            print("La nota debe ser un valor numerico..")
        elif validaNota(nota):
            print("La nota debe ser del 1 al 10..")
        else: 
            break
    id = input("Ingrese el legajo: ")
    while (validar_id(id)):
        print("Ingrese solo 3 caracteres: ")
        id = input("Ingrese el legajo: ")

    alumno = {
        'name': name,
        'nota': nota,
        'id': id,
    }
    alum_lis.append(alumno)

def muestra_alum(alumList, ind):
    print(f"Nombre: {alumList[ind]['name']}\nNota: {alumList[ind]['nota']}\nLegajo: {alumList[ind]['id']}")

def muestra_calificaciones(alumList):
    for i, e in enumerate(alumList):
        muestra_alum(alumList, i)

def calcula_prom(alumList):
    for i, e in enumerate(alumList):
        contN = + e['nota']
    prom = contN / int(len(alumList))
    print(f"El promedio de todas las nota de los alumnos es: {prom}")

def validaNota(nota):
    if nota < 1 or nota > 10:
        return True
    else:
        return False

def validaNumero(n):
    try:
        nota = int(n)
        return False, nota
    except ValueError:
        return True
def validar_id(id):
    if len(id) > 3:
        return True
    else:
        return False

creaAlumnos(alumnos)
muestra_calificaciones(alumnos)
calcula_prom(alumnos)

