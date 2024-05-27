# ejemplo de for
# imprimir los números pares 
# entre el 1 - 20

for n in range (1 , 21):
    if n%2==0:
        print(n)

#crear un programa que me imprima las 5 vocales :
vocales ="aeiou"
for n in range(0,5):
    print(vocales[n])
 #crear un programa que me muestre los primeros 8 numeros pares:
contador=0
for n in range(1,17):
    if n%2==0:
        contador+=1
        print(f"{n} es par numero {contador}")
   
# crear un programa que pida al usuario escribir una oración y mostrar por terminal la cantidad de vocales "a" que tiene esa oración.
#OJO: SOLO LAS "a" MINÚSCULAS.
oracion:str=input("escriba una oracion:")
contador:int=0
for n in range(0,len(oracion)):
    if oracion[n]=="a":
        contador+=1
print(f"la cantidad de letras a que tengo es {contador}")

#crear un programa que me cuente la cantidad de comas y me muestre sus índices.
#OJO: Tienes que pedir al usuario.
oración:str=input("escriba una oración:")
contador:int=0
for indice,letra in enumerate(oración):
    if letra==",":
        print(f"su indice es {indice}")
        contador+=1
print(f"la cantidad de comas es {contador}")
          
## Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido.
edad:int=int(input("ingrese su edad:"))
for i in range(1, edad+1):
    print("Año",i, "cumplido")


## crear un programa que me pida el nombre de tres personas y guarde en una variable global las ultimas letras de sus nombres
### Mostrar por pantalla la variable global con las tres ultimas letras del nombre de cada persona.
ultimas_letras=""
for i in range(3):
    nombre:str=input("Escribe tu nombre:")
    last_lettter:str=nombre[-1]
    ultimas_letras+=last_lettter
print(ultimas_letras)

## Crear un programa que muestre por terminal la siguiente figura:
#a
#ee
#iii
#oooo
#uuuuu

for i in range(5):
    vocal:str=input("Escribir las vocales:")
    repeticiones=["1","2","3","4","5"]
for i in range(len(vocales)):
    print(vocal [i]*repeticiones[i])





# ejemplo de if - else 
edad:int=int(input("escribe tu edad:"))
if edad>=18:
    print("eres mayor")
else:
    print("eres menor de edad")

edad_dos:int=int(input("escribe tu edad:"))
respuesta:str="eres mayor" if edad_dos>=18 else "eres menor"
print(respuesta)

#  Ejemplo de while
#condicion=True
#while condicion:
    #print("hola")
    #condicion=False

#condicion=True
#while condicion:
    #eval=input("desea continuar [S/N]:")
    #if eval=="S":
        #print("continuas en el bucle")
        #continue
    #else:
        #print("se terminó el programa")
        #condicion=False
        #break

#ejercicios de while
# Crear un programa que pida la cantidad de notas que se debe registrar luego pedirá las notas e imprimirá el promedio.

