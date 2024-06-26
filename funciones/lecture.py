# # Return devuelve valores que podré hacer uso.
# ## Crear una función que retorne el número 10, y muestre por terminal si es par.
# # Siempre que el valor que retorne mi función se utilize en más sentencias u operaciones hacer uso de return.
# def diez():
#     return 10
# if diez()%2==0:
#     print("Es par")
# else:
#     print("Es impar")
# # Print solo muestra por terminal.
# # 
# #
# # # Return cuándo queremos que nuestra función devuelva o retorne un tipo de dato o un tipo de dato estructurado.
# # Crear una función que me muestre el producto de dos números.
# def producto(a,b):
#     return a*b

# # Crear una función que me retorne una lista de tres números.
# def lista_números():
#     return{2,3,4}

# # Crear un función que por parámetro reciba un nombre y retorne un mensaje de bienvenida con el nombre.
# def mensaje(nombre):
#     print(f"hola, {nombre}, bienvenido") 

# # Crear una función que reciba por parámetro una lista de números y me devuelva el número menor,mostrar 
# # por terminal el valor retornando por la función.
# #lista=[4,3,6,8]
# #def min(l):
#     #minimo=1[0]
#     #for n in l:
#         #if n < minimo:
#             #minimo=n
#         #return minimo
# #print(min(lista))

# # Crear una función que reciba como parámetro el nombre y la edad de una persona, mi función deberá retornar un diccionario con los datos ,luego 
# # mostrar por terminal el valor de retorno de mi función.
# nombre="Yuliza"
# edad=19
# def persona(nombre,edad):
#     return{"nombre":nombre,
#            "edad":edad
#            }
# print(persona(nombre,edad))
 
# # Ejemplos de lambda
# saludo=lambda n:f"hola, {n}, {a}"
# print(saludo("Ruth","Castillo"))

# # Crear un programa anónimo que reciba como parámetro una lista de 5 números y retorne dos listas, una con los números pares y otra con números impares.
# lista=[6,64,4,4,3,5,5]
# separar_pares=lambda lista:[num for num in lista if n%2==0]
# separar_impares=lambda lista:[num for num in lista if n%2!=0]
# print(separar_pares(lista))
# print(separar_impares(lista))

# def mensaje(m):
#     print(m)
# def pedir_nombre():
#     nombre=input("Ingrese su nombre")
#     return nombre
# mensaje(pedir_nombre())

# Segunda forma de solución.
lista=[5,5,435,6,345,4]
separar_pares, separar_impares = lambda lista: [num for num in lista if num % 2 == 0], lambda lista: [num for num in lista if num % 2 != 0]
print(separar_pares(lista), separar_impares(lista))

# MAP
lista=[4,7,8,5,2]
nueva_lista=list(map(lambda x:x+1,lista)) # Por defecto retorna una lista
print(nueva_lista)
# Tengo una lista de alumnos que todos ellos aprobaron y pasan al tecer semestre.
# Problema
# En mi lista todos están con el segundo semestrepor lo que tendremos que crear una solución que cambie el campo de semestre de 2 a 3.
lista_alumnos=[
    {
        "nombre":"Abel",
        "edad":36,
        "semestre":2
    },{
        "nombre":"Anthony",
        "edad":40,
        "semestre":2
    },{
        "nombre":"Edith",
        "edad":40,
        "semestre":2
    }

]
def objeto(e):
    if"semestre" in e:
        e["semestre"]=e["semestre"]+1
    return [
        e
    ]
semestre_actualizados=list(map(objeto,lista_alumnos))
print(semestre_actualizados)

def objeto(e):
    if"semestre" in e:
        e["semestre"]=e["semestre"]+1
    e["especialidad"]="APSTI"
    return [
        e
    ]
semestre_actualizados=list(map(objeto,lista_alumnos))
print(semestre_actualizados)

# FILTER (Busca, encuentra y devuelve)
# Devolver los números pares de una lista.     
lista=[2,3,5,5,6,7,83,5]
nueva_lista=list(filter(lambda x:x%2==0, lista))
print(nueva_lista)
lista_alumnos=[
    {
        "nombre":"Abel",
        "edad":36,
        "semestre":2
    },{
        "nombre":"Anthony",
        "edad":40,
        "semestre":2
    },{
        "nombre":"Edith",
        "edad":50,
        "semestre":2
    }

]
menores_50=list(filter(lambda x:x["edad"]<50,lista_alumnos))
print(menores_50)



