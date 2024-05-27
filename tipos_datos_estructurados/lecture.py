lista=["Abel","Anthony","Miguel"]
diccionario={"nombre":"Antonio", "Edad":15, "sexo":False}
print(diccionario["Edad"])
# MÉTODOS PARA SEPARAR TEXTOS
# Método list: Separa cada caracter en un elemento de una lista.
texto="hola"
lista_texto=list(texto)
lista2=[e for e in texto]
print(lista2)

# Método .split: Trosea texto en una lista a través de un limitador(",",".",etc)
texto_largo="Hola cómo están bienvenidos al salón"
nueva_lista=texto_largo.split(" ")
print(nueva_lista)

texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split(" ")
print(nuevo_texto)

# METODOS PARA UNIR TEXTOS:
# Método join: Une los textos 
texto_largo="loquitas_.mp4"
nuevo_texto=texto_largo.split("_")  # Lo que se encuentra dentro de .split sse elimina en el texto impreso.
print("".join(nuevo_texto))  # .Join sirve para unir los textos,lo que se encuentra entre las comillas es como se quiere que el texto esté separado.

texto_largo="este es un texto largo"
nuevo_texto=texto_largo.split(" ")
print("".join(nuevo_texto))