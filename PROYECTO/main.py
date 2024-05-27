#Código de Reserva
grass = list()
reserva = f"""
```GRASS SINTÉTICO```
HORARIOS DISPONIBLES:
1. LUNES s/. 50: de 14 p.m a 16 p.m
2. MARTES s/. 20: de 16 p.m a 18 p.m
3. MIERCOLES s/. 30: de 15 p.m a 17 p.m
4. JUEVES s/. 20: de 10 a.m a 12 a.m
5. VIERNES s/. 50: de 13 p.m a 15 p.m
"""

opcion = input("Ingresar la opción del horario que desea reservar: ")


#Confirmación de Reserva
if opcion == "1":
    print("Su reserva del día LUNES fue exitosa🎉")
elif opcion == "2":
    print("Su reserva del día MARTES fue exitosa🎉")
elif opcion == "3":
    print("Su reserva del día MIÉRCOLES fue exitosa🎉")
elif opcion == "4":
    print("Su reserva del día JUEVES fue exitosa🎉")
elif opcion == "5":
    print("Su reserva del día VIERNES fue exitosa🎉")


#Verificación de Reserva
print("VERIFICACIÓN:")
if opcion == "1":
    print("Su reserva es para el día LUNES a las 14 p.m a 16 p.m y debe pagar S/. 50")
if opcion == "2":
    print("Su reserva es para el día MARTES a las 16 p.m a 18  p.m y debe pagar S/. 20")
if opcion == "3":
    print("Su reserva es para el día MIÉRCOLES a las 15 p.m a 17 p.m y debe pagar S/. 30")
if opcion == "4":
    print("Su reserva es para el día JUEVES a las 10 a.m a 12 a.m y debe pagar S/. 20")
if opcion == "5":
    print("Su reserva es para el día VIERNES a las 13 p.m a 15 p.m y debe pagar S/. 50")