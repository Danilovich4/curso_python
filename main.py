"""
Crea una clase base llamada Vehiculo.

Atributos: marca, modelo, año.
Método: detalles, que imprime:
css
Copiar código
Este vehículo es un [marca] [modelo] del año [año].
Crea dos clases hijas: Coche y Moto.

Sobrescribe el método detalles para añadir información adicional:
Coche: "Es un coche con 4 ruedas."
Moto: "Es una moto con 2 ruedas."
Crea una función llamada mostrar_vehiculo que reciba un objeto de tipo Vehiculo y llame a su método detalles.

Prueba:

Crea objetos de las clases Coche y Moto.
Usa la función mostrar_vehiculo para mostrar los detalles de ambos.
"""
class vehiculo:
    def __init__ (self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def detalles(self):
        print(f"Este vehículo es un {self.marca} {self.modelo} del año {self.año}.")

class coche(vehiculo):
    def detalles(self):
        super().detalles()  # Llama al método 'detalles' de la clase base
        print("Es un coche con 4 ruedas")

class moto(vehiculo):
    def detalles(self):
        super().detalles()  # Llama al método 'detalles' de la clase base
        print("Es una motodo con 2 ruedas")

def mostrar_vehiculo (vehiculo):
    vehiculo.detalles

# Pruebas
mi_coche = coche("Toyota", "Corolla", 2020)
mi_moto = moto("Honda", "CBR", 2019)

mostrar_vehiculo(mi_coche)
mostrar_vehiculo(mi_moto)