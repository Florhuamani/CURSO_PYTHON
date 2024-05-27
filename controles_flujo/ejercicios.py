# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad:int=int(input("ingrese su edad:"))
if edad >=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas .

contraseña="contraseñasegura123"
contraseña_usuario=input("ingresa tu contraseña:")

# Escribir un programa que pida al usuario un numero entero positivo y muestre por pantalla la cuenta atras desde ese numero hasta cero separados por comas.
numero=int(input("introduce un numero entero positivo:"))
if numero < 0:
    print("por favor, introduce un numero entero positivo.")
else:
    for i in range (numero, -1, -1 ):
        if i == 0 :
            print(i, end="")
        else:
            print(i, end=",")



# Crear un programa que me muestre la tabla de multplicar del 1 al 5.
for i in range(1,6):
    for j in range(1,13):
        print(f"{i} x {j}={i*j}")

          
# Crear un programa que pida un número y que muestre la tabla de multiplicar de ese numero
numero=int(input("Ingrese un numero:"))
print(f"Tabla de multiplicar de {numero}:")
for i in range(1,13):
    resultado=numero*i
    print(f"{numero}x{i}={resultado}")

# while
#condicion=True
#while condicion:
    #print("hola")
    #condicion=False5:
    #print (contador)
    #contador+=1
#print(f"valor final [contador]")
#nombre="josé"
#nombre.upper() #convierte el texto en mayusculas

#apellidos="ALVARES"
#print(apellidos.lower()")    # convierte el texto en minuscula
      

#segundo_nombre="luis"
#print(segundo_nombre.capitalize()) #convierte la primera letra en mayuscula