# Crear una lista de alumnos
lista_alumnos = [
    {
    "nombre": "Ruth",
    "apellido": "Castillo",
    "edad": 18
    },{
    "nombre": "Flor", 
    "apellido": "Lucana", 
    "edad": 18
    },{
    "nombre": "Rocío", 
    "apellido": "Lobo", 
    "edad": 20
    },{
    "nombre": "Lucy", 
    "apellido": "Rivera", 
    "edad": 18
    },{
    "nombre": "Abel", 
    "apellido": "Rojas", 
    "edad": 27
    }
]

# Insertar los datos de Anthony al final de la lista
lista_alumnos.append({"nombre": "Anthony", "apellido": "Smith", "edad": 24})

# Eliminar los datos de Abel si existen en la lista
lista_alumnos.remove({
    "nombre":"Abel",
    "apellido":"Rojas",
    "edad":27
})
print(lista_alumnos)

# Mostrar el alumno en la posición 4 de la lista
indice=lista_alumnos.index({
    "nombre":"Lucy",
    "apellido":"Rivera",
    "edad":18
})
print(lista_alumnos[indice])

# Crear una lista con 4 diccionarios, donde tendrán los datos de sus mascotas(nombre, edad, sexo y raza)
# Mostrar la lista con los 4 diccionarios.
# Editar el tercer registro y cambiarle la eda sin modificar la lista original.
# Mostrar la lista original y luego el 3 registro modificado.

# SOLUCIÓN:
# Crear una lista con 4 diccionarios, donde tendrán los datos de sus mascotas(nombre, edad, sexo y raza)
Mascotas=[
    {
        "Nombre":"Luna",
        "Edad":2 ,
        "Sexo":"Hembra",
        "Raza":"Chihuahua"
    },{
        "Nombre":"Max",
        "Edad":3,
        "Sexo":"Macho",
        "Raza":"Labrador"
    },{
        "Nombre":"Bella",
        "Edad":5,
        "Sexo":"Hembra",
        "Raza":"Buldog"
    },{
        "Nombre":"Rocky",
        "Edad":1,
        "Sexo":"Macho",
        "Raza":"Pitbull"
    }
]
# Mostrar la lista con los 4 diccionarios.
print(Mascotas)
# Editar el tercer registro y cambiarle la eda sin modificar la lista original.
Mascotas_modificadas=Mascotas.copy()