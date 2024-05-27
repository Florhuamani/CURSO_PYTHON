. Validar si un número ingresado por el usuario es positivo, negativo o cero.
ingrese_numero:int=int(input("ingrese numero:"))
#usamos los operadores de comparacion
print("numero ingresado es positivo:", ingrese_numero>=0)
print("numero ingresado es negativo:", ingrese_numero<0)
print("numero ingresado es 0:", ingrese_numero==0)
#comparamos el valor usamos bool
#comparacion:bool=ingrese_numero >= 0 and ingrese_numero < 0

Determinar si un año ingresado por el usuario es anterior al año actual.
#ingrese año usuario
año_del_usuario:int=int(input("ingrese año: "))
#ingrese año actual
año_actual=2024
#determinar año anterior usando operadores de comparacion
mensaje=año_del_usuario < año_actual
print("¿es TRUE o FALSE que el año introducido es anterior al actual?")
print(mensaje)

1. Validar si un número ingresado por el usuario es primo o no.
#ingresar numero usuario
numero_usuario:int=int(input("ingrese numero: "))
if numero_usuario %2==0:
	print("no es primo")
if numero_usuario %2==1:
	print("si es primo")
	
	#Utilizando operadores de comparación, determina si un numero introducido por el usuario tiene una longitud mayor o igual que 3 y a su vez es menor que 10
#entrada de datos
numero_usuario:str=input("ingresa un numero: ")
longitud:int=len(numero_usuario)
#proceso de datos
comparacion:bool=longitud >= 3 and longitud < 10
#salida de datos
print(comparacion)
