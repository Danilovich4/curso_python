"""
1. Use una lista para almacenar 5 números y:
Agregue un sexto número.
Elimine el tercer número.
Imprima los números en orden inverso.
2.Use un diccionario para almacenar información de una persona (nombre, edad, ciudad) y:
Agregue una clave para la profesión.
Elimine la clave ciudad.
Imprima todos los valores del diccionario.
"""

#Lista
numeros = [1,2,3,4,5]
numeros.append(6)
numeros.remove(3)
print(numeros.reverse)

#Diccionario
persona = {"nombre": "Jon", "edad": 15, "ciudad": "Barna"}
persona["profesion"] = "PO"
del persona ["ciudad"]
print(persona)