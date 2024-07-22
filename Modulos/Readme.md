# Averiguar sobre módulos y paquetes en python😧
## ¿Que son los módulos? 😵‍💫
Los módulos en python son archivos que contienen funciones, variables y clases que pueden ser utilizadas en otros programas. Los módulos permiten organizar y reutilizar códigos de manera eficiente,facilitando el desarrollo de aplicaciones más grandes y complejas.

Los módulos son simplemente ficheros de texto que contienen código Python y representan unidades con las que evitar la repetición y favorecer la reutilización.

**Ejemplo 😨:**
```python
# operaciones.py
def suma(a.b):
    return a+b

def resta(a-b):
    return a-b

# main.py 
import operaciones 
print(operaciones.suma(5,3)) # salida : 8
print(opeaciones.resta(10,6)) # Salida : 4
```
## ¿Que son los paquetes? 😵‍💫
Un paquete es simplemente una carpeta que contiene ficheros .py. Además permite tener una jerarquía con más de un nivel de subcarpetas anidadas.

Los paquetes en python son una forma de organizar módulos relacionados en una jerarquia de directorios. Un paquete es esencialmente un directorio que contiene uno o más moulos de python. junto con un archivo esencial llamado ```__init__.py```. Este archivo indica que el directorio debe tratarse como un paquete. Los paquetes permiten una estructura más organizada y modular en proyectos de python, facilitando la reutilización y distribución de código.

**Ejemplo😨:**
```python
matematica/
    |-- __init__.py
    |-- aritmetica.py
    |-- geometria.py

# Debe contener siempre un archivo __init__.py (por el momento vacío) para que Python entienda que se trata de un paquete y no de una simple carpeta. Así, podemos acceder a alguno de los módulos del paquete de la siguiente manera:

import matematica.aritmetica
print(matematica.aritmetica.sumar(7, 5))

# O bien de la siguiente:
from matematica import aritmetica
print(aritmetica.sumar(7, 5))

# También esta otra:
from matematica.aritmetica import sumar
print(sumar(7, 5))

```

# Averiguar diferencias entre módulos y paquetes 
## ¿Cuáles son las diferencias entre módulos y paquetes?🤔
- El módulo es un único archivo Python que se puede importar a otro módulo. Por el contrario, un paquete es una colección de módulos organizados en una jerarquía de directorios.
- Un paquete puede tener múltiples subpaquetes y módulos, y cada módulo y subpaquete tiene su propio espacio de nombres, mientras que cuando se importan módulos, su contenido se coloca dentro de un espacio de nombres.

## 😃 Módulo:
### Definición:
Puede ser un archivo python simple que contiene colleciones de funciones y variables globales.

### Objetivo:
Organización del código.

### Organización:
Código dentro de un solo archivo

### Cómo importar:
importar ```nombre_módulo```.

## 😃 Paquete:
### Definición:
Mientras que el paquete es una colección de diferentes módulos con un archivo `_init_.py.`.

### Objetivo:
Distribución y reutilización de códigos.

### Organización:
Módulos relacionados en una jerarquía de directorios.

### Cómo importar:
importar ```nombre_paquete.nombre_módulo```.


#### Main.py se le conoce como archivo de script y el codigo que está dentro de mi archivo se le conoce como script.