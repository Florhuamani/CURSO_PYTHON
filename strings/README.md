# STRING
es una secuencia de caracteres encerrados entre comillas simples ('') o dobles (""). Las cadenas de texto se utilizan para representar palabras, frases, texto y cualquier otro tipo de información textual en un programa. Aquí te dejo un ejemplo de cómo se utiliza una cadena de texto en Python:

## Len:
 La longitud de una cadena de texto en Python se puede obtener utilizando la función len(). Por ejemplo, si tenemos una cadena 'cadena_texto' y queremos saber su longitud, podemos hacerlo de la siguiente manera:
> ejemplo:
```python
cadena_texto = "¡Hola, mundo!"
longitud = len(cadena_texto)
print("La longitud de la cadena es:", longitud)  # Esto imprimirá "La longitud de la cadena es: 13"
```
La función len() devuelve el número de caracteres en la cadena, incluidos espacios y signos de puntuación.

## Concatenación (+):
 Este operador se utiliza para unir dos cadenas de texto.
> Ejemplo:
```python
cadena1 = "Hola,"
cadena2 = " mundo!"
resultado_concatenacion = cadena1 + cadena2
print(resultado_concatenacion)  # Esto imprimirá "Hola, mundo!"
```

## Repetición `*`: 
Se utiliza para repetir una cadena un número determinado de veces.
> Ejemplo:
```python
cadena = "Python "
resultado_repeticion = cadena * 3
print(resultado_repeticion)  # Esto imprimirá "Python Python Python "
```

## Indexación `[]`: 
Permite acceder a caracteres individuales dentro de una cadena.
> Ejemplo:
```python
cadena = "Python"
primer_caracter = cadena[0]
print(primer_caracter)  # Esto imprimirá "P"
```

## Slicing ([start:stop:step]):
 Se utiliza para extraer partes específicas de una cadena.
> Ejemplo:
```python
cadena = "Python es genial"
subcadena = cadena[7:9]
print(subcadena)  # Esto imprimirá "es"
```