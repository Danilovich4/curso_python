class coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    def detalles (self):
        print(f"Este coche es {self.marca} del modelo {self.modelo} y del año {self.año}")

mi_coche = coche("Toyota", "Prius", 2019)

mi_coche.detalles()
