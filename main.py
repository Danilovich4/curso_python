"""
Pida al usuario un número n.
Use un bucle for para imprimir todos los números desde 1 hasta n.
Use un bucle while para calcular la suma de los números desde 1 hasta n.
Incluya un caso donde se use break para detener el bucle si se llega a un número específico (por ejemplo, 5).
"""
#Pedimos numero
num = int(input("Inserte un numero: "))

#Bucle for
for n in range(1, num):
    print(n)

#Bucle while
con = int(1)
while con <= num:
    print(f"Suma del contador: {con}")
    con += 1

#Caso break
for numero in range (1, 7):
    if numero == 5:
        print("Se detiene bucle")
        break
    else:
        print(numero)