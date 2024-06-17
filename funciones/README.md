# FUNCIONES
Matemáticamente, una función es una operación que toma uno ó más valores llamados `Argumentos` y produce un valor denominado `Resultado`.
> [!NOTE]
> Todos los lenguajes de programación tienen funciones incorporadas (`funciones internas`), y funciones creadas por el usuarios(`funciones externas`).
En programación una función es un subprograma,es una estructura que nos permite agrupar códigos y sus principales objetivos son:
- `NO REPETIR` fragmentos de código.
- `REUTILIZAR` el código de distintos escenarios.
## Estructura de una función
Una función viene `definida`por un `nombre`, sus `parámetros` y su valor de `retorno`.
Una vez creada la función podremos solicitar su ejecución `invocando` la función por su `nombre`.
## Definir una función en python
Para definir una función en python, primero utilizaremos la palabra reservada `DEF` seguida por el `nombre` de la función . a continuación especificaremos los `parámetros` con `()` si es una función sin parámetros, `(a)` si es una función con parámetros irán separados por `,`, finalizaremos la línea con `:`, en la siguiente línea sin olvidar el identado, comenzará el `cuerpo` de la función (micro programa) que puede contener 1 ó más sentencias, finalmente deberá `retornar` un resultado con la palabra reservada `return`.
> [!TIP]
> Como retorno tambén se puede utilizar la`función interna`, `print()`, para depuración de código no es recomendable usarlo en producción.

### OBSERVACIÓN
print, dentro de una función, es una herramienta de depuración de código  para probar si mi función está cumpliendo realmente la tarea.
```python
def saludo():
    saludo ="Hola chivo"
    saludo_dos = "Cómo estás"
    return f"{saludo}, {saludo_dos}"
saludo()
```
## Invocar una función
Para invocar, llamar o ejecutar una función solo debemos escribir el `nombre` de la función, seguido por `()` paréntesis.
```python
def saludo():
    print("hola")
#Invocando la función
saludo()
```
## Retornar un valor
Las funciones pueden retornar o devolver un valor.
```python
def uno():
    return 1
    uno()
```
>[!WARNING]
> No confundir `print` con `return`, el valor retornado por `return` nos permite usarlo fuera de su contexto. Y `print()` solo mostrará el literal por terminal.
**Ejemplo**
*En el archivo lecture.py 
## Retornando múltiples valores
El secreto es hacerlo mediante un tipo de dato estructurado.
```python
def tupla():
    return 2,3,4
varios()
def lista():
    return["hola",45]
lista()
def dicc():
    return{"nombre":"Jose","edad":45}
    dicc()
```
## Parámetro y Argumentos.
Si una función no dispusiera de de valores de entrada estaría limitada en su actuación .
Es por ello que los `parámetros` no permiten variar los datos que consume una función para obtener distintos resultados.
**Ejemplo:**
* Crear una función que recibe un valor númerico y retorna su raiz cuadrada *
```python
def sqrt(valor):
    return valor**(1/2)
# Nota: En este caso, el valor 4 es un argumento de la función.
sqrt(4)
```
Cuándo llamamos a una función con `argumentos`. los valores de estos argumentos se copian en los correspondientes `parámetros` dentro de la función.
```python
def ejm(a,b,c):
    return a+b+c
ejm(2,4,5)
```
### Argumentos nominales
En esta aproximación los argumentos no son copiados en un orden específico sino que **se asignan por nombre a cada parámetro**. Ello nos permite evitar el problema de conocer o recordad cuál es el orden de los parámetros en la definición de la función.
Para utilizarlo, basta con realizar una asignación de cada argumento en la propia lllamada a la función.
**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f""" La cpu es de la familia {familia} con {num_core} cores y con ina frecuencia de {frecuencia}
    """)
# Haciendo uso de argumentos nominales,
build_cpu{num_core=4,familia="Intel",Frecuencia=2,7}
```
### Argumentos posicionales
Los argumentos son copiados en un orden específico, en este caso debemos conocer o recodar cuál es el orden de los argumentos.
**Ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f""" La cpu es de la familia {familia},
     con {num_core} cores 
     y con una frecuencia de {frecuencia}
    """)
# Haciendo uso de argumentos posicionales.
build_cpu("intel", 4, 2.7)
```
### Parámetros por defecto
Es posible especificar **valores por defecto** en los parámetros de una función, en el caso de que no se proporcione un valor al argumento en la llamada a la función, el parámetro correspondiente tomará el valor definido por defecto.
**Ejemplo**
```python
def alumnos(nom,app,estado="Aprobado"):
alumnos("Ruth","Castillo")
alumnos("Anthony","Cruces","Desaprobado")
```
## Desempaquetado/Empaquetado de argumentos(tarea)
El empaquetado y desempaquetado de argumentos en Python es una técnica fundamental que permite a los desarrolladores trabajar con un número variable de argumentos en una función, lo que proporciona una gran flexibilidad en el diseño y la implementación del código.

Empaquetado de Argumentos:
El empaquetado de argumentos se refiere a la capacidad de pasar un número variable de argumentos a una función. Esto se logra utilizando tuplas o listas para empaquetar los argumentos y luego desempaquetarlos dentro de la función. Por ejemplo, al definir una función, se puede utilizar el operador de asterisco (*) para empaquetar los argumentos en una tupla, lo que permite que la función maneje una cantidad variable de argumentos.

```python
def sumar_numeros(*args):
    total = 0
    for num in args:
        total += num
    return total

*Llamada a la función con diferentes cantidades de argumentos*
resultado1 = sumar_numeros(1, 2, 3)
resultado2 = sumar_numeros(1, 2, 3, 4, 5)
```

En este ejemplo, el operador *args permite empaquetar un número variable de argumentos en una tupla llamada args, lo que facilita la suma de todos los números pasados a la función.

Desempaquetado de Argumentos:
El desempaquetado de argumentos implica tomar una estructura de datos, como una lista o una tupla, y utilizar sus elementos como argumentos individuales en una función. Esto es útil cuando se necesita pasar múltiples argumentos a una función de una manera más dinámica. Para desempaquetar argumentos, se utiliza el operador de asterisco (*) junto con la lista o tupla que contiene los argumentos.

```python
def saludar(nombre, apellido):
    return f"Hola, {nombre} {apellido}!"

*Desempaquetado de argumentos desde una lista*
informacion = ["John", "Doe"]
saludo = saludar(*informacion)
```

En este caso, la función saludar espera dos argumentos, pero al pasar una lista con los nombres, el operador de asterisco desempaqueta los elementos de la lista y los pasa como argumentos individuales a la función.

El empaquetado y desempaquetado de argumentos en Python proporciona una forma poderosa de trabajar con un número variable de argumentos de manera eficiente y flexible, lo que es especialmente útil en situaciones donde el número exacto de argumentos no es conocido de antemano. Esta técnica es comúnmente utilizada en muchas bibliotecas y marcos de trabajo de Python para proporcionar flexibilidad en la interfaz de las funciones


## Funciones internas de python(tarea)
Las funciones internas en Python, también conocidas como funciones incorporadas o funciones predefinidas, son un conjunto de funciones que están disponibles para su uso sin necesidad de ser definidas previamente. Estas funciones son proporcionadas por el propio lenguaje y abarcan una amplia gama de operaciones comunes.

Python proporciona un número importante de funciones internas que pueden ser utilizadas sin necesidad de tener que definirlas previamente. Estas funciones incluyen operaciones matemáticas, manipulación de cadenas, gestión de listas, operaciones de archivos, entre otras funcionalidades fundamentales para el desarrollo de aplicaciones en Python [𝟏].

Algunos ejemplos de funciones internas comunes en Python incluyen print() para imprimir en la consola, len() para obtener la longitud de una secuencia, type() para obtener el tipo de un objeto, range() para generar secuencias de números, y muchas otras funciones que son esenciales en el día a día de la programación en Python.

En resumen, las funciones internas de Python son un conjunto de funciones y tipos que están siempre disponibles para su uso, lo que proporciona a los desarrolladores una base sólida y consistente para construir sus aplicaciones.

Ejemplo para cada una de las funciones internas de Python :

1. sum():
   - Ejercicio: Calcular la suma de los números del 1 al 10.
     python
     numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
     resultado = sum(numeros)
     print(resultado)  # Output: 55
     

2. min():
   - Ejercicio: Encontrar el número más bajo en una lista.
     python
     numeros = [5, 3, 8, 2, 10]
     menor = min(numeros)
     print(menor)  # Output: 2
     

3. max():
   - Ejercicio: Encontrar el número más alto en una lista.
     python
     numeros = [10, 20, 15, 30, 25]
     mayor = max(numeros)
     print(mayor)  # Output: 30
     

4. range():
   - Ejercicio: Imprimir los números pares del 1 al 10.
     python
     pares = list(range(2, 11, 2))
     print(pares)  # Output: [2, 4, 6, 8, 10]
     

5. round():
   - Ejercicio: Redondear un número decimal al entero más cercano.
     python
     numero_decimal = 3.7
     redondeado = round(numero_decimal)
     print(redondeado)  # Output: 4
     

6. hex():
   - Ejercicio: Convertir un número entero a su representación hexadecimal.
     python
     numero_entero = 16
     hexadecimal = hex(numero_entero)
     print(hexadecimal)  # Output: 0x10
     

7. abs():
   - Ejercicio: Obtener el valor absoluto de un número.
     python
     numero = -5
     absoluto = abs(numero)
     print(absoluto)  # Output: 5
     

8. id():
   - Ejercicio: Obtener el identificador único de un objeto en Python.
     python
     objeto = 'Hola'
     identificador = id(objeto)
     print(identificador)  # Output: Identificador único de 'Hola'
     
## Tipos de funciones:
### Funciones anónimas(FUNCIONES LAMBDA)
Una función que no tiene nombre.
`lambda:"Hola"`
### Funciones closure
### Funciones callback

## Programación funcional