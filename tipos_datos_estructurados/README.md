# TIPOS DE DATOS ESTRUCTURADOS (TDA - Tipos de Datos Abstractos)
```
# Listas: Sus valores o elementos se pueden actualizar, eliminar.
listas=["Abel", 20, 2.5,  False, ["texto",.2]]                                             # Tanto la lista como la tupla
# Tupla: Sus valores o elememtos no pueden ser modificados o eliminados.
tupla=("Abel", 20, 5.2, False, [])
# Diccionarios(Se le conoce también como objetos.): Los diccionarios almacenan los datos con clave:valor
diccionario={"nombre":"Antonio", "Edad": 15, "sexo":False}
```
- [!TIP]
- - **OBSERVACIÓN:** 
- Los tipos de datos estructurados pueden almacenaren su interior otros tipos de datos estructurados.
```python
lista-alumnos=[
    {
        "nombre":"Abel",
    }
]


## Métodos para separar texto.
### 1. Convertir texto a lista:
```python
# Método list: Separa cada caracter en un elemento de una lista.
texto="hola"
list(texto)#["h","o","l","a"]

# Método split: Trosea texto en una lista a través de un limitador(",",".",etc)
texto="Hola, cómo están"
texto.split(",")

## Método para unir textos.
# Método join:
texto_largo="este es un texto largo"
nuevo_texto=texto_largo.split(" ")
print("".join(nuevo_texto))


### 2. Agregar elementos a una lista.
```python
# Método append: Es el método que me permite agregar elementos al final de una lista.
lista=["hola"]
lista.append("mundo")   # En JAVA SCRIPT es conocido como "push"
print(lista)

# Método insert: Permite agregar elementos en cualquier ubicación de la lista.
lista_nombres=["Edith","Ruth","Luz"]
lista nombres.insert(0, "Anthony")      # Depende del índice que se coloque se podrá insertar el elemento.

### 3. Eliminar elementos de una lista
```python
# Método pop: Elimina el último elemento de una lista.
lista_nombres=["Edith","Ruth","Luz"]
lista_nombres.pop()                 # Automaticamente se elimina el último elemento sin necesidad de que se indique.

## 1°manera:
### Método remove: Elimina el elemento que se pone por nombre.
ista_nombres=["Edith","Ruth","Luz"]
lista_nombres.remove("Ruth")
## 2° manera:
### Método pop(0): Elimina por índice 
ista_nombres=["Edith","Ruth","Luz"]
lista_nombres.pop(0)

### 4. Buscar un elemento en la lista.
# Método index:
```python
lista_nombres=["Edith","Ruth","Luz"]
indice=lista_nombres.index("Ruth")
print(lista_nombres[indice])

# Método pertenencia:
ista_nombres=["Edith","Ruth","Luz"]
pertenencias="Edith" in lista_nombres

### 5. Comparación de listas: Podemos hacer uso de los operadores de comparación para comparar listas.
**Ejem:*
```python
Comparar==[1,2,3]>[1,2,4]    # Se compara un elemento de la lista 1 con los elementos de la lista 2.
# El 1 no lo evalúa por que son iguales en ammbas listas.
# El dos no lo evalúa por que los elementos son iguales en ambas listas.
# El 3 si evalúa por que es menor que 4.
# Entonces la primera lista es menor que la segunda lista.
print(compara)
# Salida

### 6. Cuidado con las copias:
# Fe de erratas(actualizar lista):
```python
lista=[2,3,46,7]
lista[3]=4
print(lista)
```
```python
alumnos=[
    {
        "nombre":"Abel"
        "Edad":"17"
    },{
        "nombre":"Anthony"
        "Edad":25
    }
]
alumnos[0]["Edad"]=23           # Modificar un dato
alumnos[0]={"nombre":"Mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)
```