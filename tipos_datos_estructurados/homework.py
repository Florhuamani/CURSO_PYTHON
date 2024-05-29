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
    "nombre":"Pablo",
    "apellido":"Córdova",
    "edad":21
})
print(lista_alumnos[indice])

# Crear una lista con 3 diccionarios, donde tendrán los datos de sus mascotas(nombre, edad, sexo y raza)
# Mostrar la lista con los 4 diccionarios.
# Editar el tercer registro y cambiarle la eda sin modificar la lista original y luego el 3 registro modificado.
Mascotas=[
    {
        "Nombre":"Luna",
        "Edad":2 ,
        "Sexo":"Hembra"
        "Raza":"Chihuahua"
    }]