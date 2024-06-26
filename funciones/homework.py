# Crear una función que reciba por argumento n numeros y retorne una lista con los números pares.
# Forma clásica:
def numeros_pares(*args):
    pares=[]
    for n in args:
        if n%2==0:
           pares.append(n)
        return pares
# Por comprensión
    # return[n for n in args n%2==0]
print(numeros_pares(8,4,16,4,5,4))

# Crear 3 funciones para los siguientes casos:
# Calcular el número mayor
# Calcular el número menor
# Calcular la suma de todos los números
# Se le pasará por argumentos n numeros

def Min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def Max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor
def Sum(*args):
    suma=0
    for n in args:
        suma+=n
    return suma

valores=4,7,8,5,2,1
print(Min(*valores))
print(Max(*valores))
print(Sum(*valores))
 
# TAREA
# Crear una lista con los siguientes campos, nombre, apellido, edad, celular, email.
#1. Actualizar los registros con un campo mas todos tendrán el campo de programa de estudios de enfermería.
#2. Buscar el segundo registro y actualizar su edad a 50 años.

lista_alumnos=[
    {
        "nombre":"Abel",
        "apellido":"Jurado",
        "Edad":20,
        "Celular":956347356,
        "email":"abel@23"

    },{
        "nombre":"Ruth",
        "apellido":"Castillo",
        "Edad":18,
        "Celular":957875456,
        "email":"ruthl@05"

    },{
        "nombre":"Rocio",
        "apellido":"Lobo",
        "Edad":26,
        "Celular":956736566,
        "email":"loborocio@13"

    },{
        "nombre":"Alvaro",
        "apellido":"Canchos",
        "Edad":19,
        "Celular":9674638476,
        "email":"canchosalvaro@31"

    }
    
]

#1. Actualizar los registros con un campo mas todos tendrán el campo de programa de estudios de enfermería.
def objeto(e):
        e["programa_estudio"]="enfermeria"
        return [e]
    
lista_actualizados=list(map(objeto,lista_alumnos))
print(lista_actualizados)

#2. Buscar el segundo registro y actualizar su edad a 50 años.
def objeto(e):
        e["edad"]=50
        return [e]

lista_actualizada=list(filter(objeto,lista_alumnos))
print(lista_actualizados[1])