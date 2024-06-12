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
## Funciones internas de python(tarea)
