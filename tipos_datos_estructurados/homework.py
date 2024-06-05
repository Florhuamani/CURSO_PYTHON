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
# Editar el tercer registro y cambiarle la edad sin modificar la lista original.
## Crear una copia para que la lista no se vea afectada directamente.
Mascotas_modificadas=Mascotas.copy()
# Editar la edad del 3 registro:
Mascotas_modificadas[2]["Edad"]=3
# Mostrar la lista original:
print("Lista original:")
print(Mascotas)
# Mostrar el 3 registro modificado
print("Tercer registro modificado:")
print(Mascotas_modificadas[2])

# Un empresario de alquiler de autos desea guardar en una base de datos la información de sus vehículos, proceso que desea automatizar con un sistema informático,las acciones
# que puedo realizar el empresario son :
# Ver la lista de autos que tiene.
# Podrá también actualizar la lista y agregar un nuevo vehículo.
# Usando casos de uso.

## CASOS DE USO:
# Yo como empresario 
# Quiero guardar la información en una base de datos.
# Para ver la lista de autos que tengo

lista_autos=[
    {
        "Marca":"Honda",
        "Precio":456.00,
        "Color":"Negro"
    },{
        "Marca":"Susuki",
        "Precio":520.00,
        "Color":"Blanco"
    },{
        "Marca":"Toyota",
        "Precio":1000.00,
        "Color":"Rojo"
    }
]

print(lista_autos)

# Yo como empresario
# Quiero agregar un nuevo vehiclo 
# Para ver la lista actualizada.
def agregar_nuevo_vehiculo(autos, marca, modelo, año, disponible):
    nuevo_auto = {'marca': "Mercedes_benz","precio":1500.00,"Color":"Griss"}
    autos.append(nuevo_auto)


# Crear una lista de los primeros 20 números primos haciendo uso de comprensión.
números_primos = [num for num in range(2, 100) if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1) if num != i)]
primos = [num for num in números_primos][:20]
print(primos)