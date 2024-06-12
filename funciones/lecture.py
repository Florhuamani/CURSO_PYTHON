# Return devuelve valores que podré hacer uso.
## Crear una función que retorne el número 10, y muestre por terminal si es par.
# Siempre que el valor que retorne mi función se utilize en más sentencias u operaciones hacer uso de return.
def diez():
    return 10
if diez()%2==0:
    print("Es par")
else:
    print("Es impar")
# Print solo muestra por terminal.
# 
#
# # Return cuándo queremos que nuestra función devuelva o retorne un tipo de dato o un tipo de dato estructurado.
# Crear una función que me muestre el producto de dos números.
def producto(a,b):
    return a*b

# Crear una función que me retorne una lista de tres números.
def lista_números():
    return{2,3,4}

# Crear un función que por parámetro reciba un nombre y retorne un mensaje de bienvenida con el nombre.
def mensaje(nombre):
    print(f"hola, {nombre}, bienvenido") 

# Crear una función que reciba por parámetro una lista de números y me devuelva el número menor,mostrar 
# por terminal el valor retornando por la función.
lista=[4,3,6,8]
def min(l):
    minimo=1[0]
    for n in l:
        if n < minimo:
            minimo=n
        return minimo
print(min(lista))

# Crear una función que reciba como parámetro el nombre y la edad de una persona, mi función deberá retornar un diccionario con los datos ,luego 
# mostrar por terminal el valor de retorno de mi función.
nombre="Yuliza"
edad=19
def persona(nombre,edad):
    return{"nombre":nombre,
           "edad":edad
           }
print(persona(nombre,edad))
 
