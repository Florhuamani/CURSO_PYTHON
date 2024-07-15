# crear dos archivos.
# un archivo tendrá una importación directa del otro archivo
# 5 variables y una función
#Archivo 1: archivo1.py*

# Definición de variables
variable1 = 10
variable2 = 20
variable3 = "Hola"
variable4 = [1, 2, 3, 4, 5]
variable5 = {"a": 1, "b": 2, "c": 3}

# Definición de función
def resta(a, b):
    """funcion de la resta"""
    return a - b

# Importación directa del archivo2
import archivo2

print("Importación directa desde archivo1:")
print(archivo2.variable6)
print(archivo2.variable7)
print(archivo2.multiplicacion(5, 3))


