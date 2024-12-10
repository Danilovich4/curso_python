"""
Pregunte al usuario un número y determine si es:
Positivo.
Negativo.
Cero.
Pregunte al usuario una calificación (0-100) y clasifique:
>=90: Excelente.
>=70: Bueno.
>=50: Regular.
<50: Insuficiente.
Usa elif y else para manejar las condiciones.
"""
#Pedirmos al usuario numero
num = int(input("Añade un número: "))

#Condicionales
if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Cero")

#Pedimoc calificacion
cal = int(input("Calificacion del 0-100"))

if cal >= 90 and cal < 100:
    print("Excelente")
elif cal >=70 and cal < 90:
    print("Bueno")
elif cal >=50 and cal < 70:
    print("Regular")
elif cal < 50 and cal >=0:
    print("Insuficiente")
else:
    print("Error al introducir calificacions")