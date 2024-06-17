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
 