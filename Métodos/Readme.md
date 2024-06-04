# Métodos de python: 
Son herramientas que nos ofrece python para manejar o modificar 
## Números
- Len:
```python
len(15446237)
# Devuelve la cantidad de dígitos
# 8
```
- Range: Función que genera una sucesión de numeros enteros de forma personalizada.


## Textos
- Len:
```python
len("hola mundo")
# Devuelve la cantidad de caracteres .
# El espacio cuenta también como un caracter
# 10
```
- Str.join: Une todos los elementos de una iteracióncon un específico string.
```python
print("y".join(["a","b","c"]))    # a y b y c
```
- Str(string): Función que devuelve la representación de cadena de un número. 
```python
str=str(input("variable:"))
# Almacena la información de una variable(INPUT)

```python
for i in range(5):
    print(i)
#salida. 0,1,2,3,4.
```
## Listas
```python
len(["h","o","l","a"])
# Devuelve la cantidad de elementos.
# El espacio cuenta también como un caracter.
# 4
```
- Append: Añade un elemento al final de la lista.
```python
frutas=["manzana","Pera","Cereza"]
frutas.append("Mango")
```
- Clear: Remueve todos los elementos de la lista.
```python
Ropa=["Blusa","Jeans","Camisas"]
Ropa.clear()
```
- Copy: Realiza una copia de la lista.
```python
Frutas=["manzana","Pera","Cereza"]
x = Frutas.copy()
```
- Count: Devuelve el número de elementos con el valor especificado.
```python
puntos=[1,2,3,3,4,]
x=puntos.count(3)
```
- Index: Devuelve el índice del primer elemento con el valor especificado.
```python
frutas=["manzana","naranja"."plátano"]
x=frutas.index("plátano")
```
- Insert: Añade un elemento en la posición especificada.
```python
frutas=["manzana","naranja","plátano"]
frutas.insert(1, "fresa")
```
- Remove: Elimina el primer item con el valor especifícado.
```python
frutas=["manzana","naranja","plátano"]
frutas.remove("plátano")
```
- Sort: Ordena la lista
```python
Vehiculos=["ford","BMW","Toyota"]
Vehiculos.sort()
```

## Tuplas
- Count: Devuelve el número de veces que aparece un valor especificado en una tupla.
```python
tupla=(1,2,3,54,54,3)
x=tupla.count(54)
print(x)
```
- Index: Busca en la tupla el valor especificado y devuelve la posición donde se encontró.
```python
tupla=(1,2,3,54,54,3)
x=tupla.index(1)
print(x)
```
## Diccionarios
- clear: remueve todos los elementos del diccionario.
```python
auto={
    "marca":"ford",
    "modelo":"mustang",
    "año":1964
}
auto.clear()
print(auto)
```
- items: Devuelve una lista que contiene una tupla para cada clave-valoren el diccionario.
```python
auto={
     "marca":"ford",
    "modelo":"mustang",
    "año":1964
}
x = auto.items()
print(x)
```
- Copy: Devuelve una copia del diccionario original.
```python
auto={
     "marca":"ford",
    "modelo":"mustang",
    "año":1964
}
x=auto.copy()
print(x)
```