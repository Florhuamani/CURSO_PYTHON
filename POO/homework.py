#Crear una clase Banco.
#Sus atributos serán nombre,apellidos, DNI, número de cuenta y saldo inicial.
#Cómo método podremos hacer depósito, retirar dinero y ver estado de cuenta.
class Banco:
    def __init__(self, nombre, apellidos, dni, cuenta, saldo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.cuenta = cuenta
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad  # Tu versión del método
        print(f"Depósito realizado con éxito. Nuevo saldo: {self.saldo}")

    def retirar(self, cantidad):
        if self.saldo - cantidad >= 0:
            self.saldo =self.saldo -cantidad
            print(f"Retiro realizado con éxito. Nuevo saldo: {self.saldo}")
        
    def ver_saldo(self):
        print(f"Saldo actual: {self.saldo}")


cliente = Banco("Alvaro", "Salcedo", "79947584", "as894048-6", 250)
cliente.depositar(50)
cliente.retirar(40)
cliente.ver_saldo()

#Crear una clase Agencia.
# Sus atributos serán nombre, apellidos del pasajero, DNI,número de asiento y fecha de viaje.
# Sus métodos serán ingresar origen, ingresar destino, cancelar viaje y ver estado de pasaje.
class Agencia:
    def __init__(self, nombre, apellido, dni, numero_asiento, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_asiento = numero_asiento
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None

    def ingresar_origen(self, lugar):
        self.origen = lugar
        print("Origen del viaje: ", self.origen)

    def ingresar_destino(self, lugar):
        self.destino = lugar
        print("Destino del viaje: ", self.destino)

    def cancelar_viaje(self):
        self.origen = None
        self.destino = None
        print("Viaje cancelado")

    def ver_estado_de_pasaje(self):
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("DNI: ", self.dni)
        print("Número de asiento: ", self.numero_asiento)
        print("Fecha de viaje: ", self.fecha_viaje)

        if self.origen:
            print("Origen: ", self.origen)

        if self.destino:
            print("Destino: ", self.destino)

        if not self.origen and not self.destino:  
            print("Viaje no reservado")


ana = Agencia("ana", "reyes", 78848594, 2, "12/11/23")
ana.ingresar_origen("lima")
ana.ingresar_destino("nazca")
ana.ver_estado_de_pasaje()




