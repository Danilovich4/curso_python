"""Crea una clase CuentaBancaria.

Atributos: _saldo (protegido), _titular (protegido).
Define un @property para:
Obtener el saldo (saldo).
Modificar el saldo (saldo.setter), asegurando que no sea negativo.
Define un @property para:
Obtener el nombre del titular (titular), que será de solo lectura.
Prueba:

Crea un objeto CuentaBancaria con un saldo inicial de 1000 y titular "Dani".
Modifica el saldo a 1500 y verifica el valor.
Intenta asignar un saldo negativo y verifica que lanza un error.
Imprime el nombre del titular."""

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo_inicial

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El valor saldo no puede ser negativo")
        self._saldo = valor

    @property
    def titular(self):
        return self.titular

# Pruebas
cuenta = CuentaBancaria("Dani", 1000)
print(cuenta.saldo)
cuenta.saldo = 1500
print(cuenta.saldo)
cuenta.saldo = -500  # Esto debe generar un error
print(cuenta.titular)
