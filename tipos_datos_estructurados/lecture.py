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

# Dato primitivo:
nombre="Abel"
otro_nombre=nombre
print(id(nombre))
print(id(otro_nombre))

# Datos estructurados:
lista_original=[1,2,3,4]
copia_lista=lista_original
lista_original[-1]=15
print(copia_lista)

# Crear un programa que reciba una lista desordenada y muestre por terminal una lista ordenada y la lista original.
lista_desordenada=[3,5,34,6]
lista_ordenada=lista_desordenada.copy()
lista_desordenada.sort()
print(lista_desordenada)
print(lista_ordenada)



alumnos=[
    {
        "nombre":"Abel",
        "Edad":17
    },{
        "nombre":"Anthony",
        "Edad":25
    }
]
alumnos[0]["Edad"]=23           # Modificar un dato
alumnos[0]={"nombre":"Mafer","edad":15}
alumnos[1]["sexo"]="por definir"
print(alumnos)