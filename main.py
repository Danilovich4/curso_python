"""
Defina tres funciones:
Una para calcular el cuadrado de un número.
Una para calcular el cubo de un número.
Una para verificar si un número es par o impar.
Use las funciones en un programa principal (main()).
Pida al usuario un número y:
Muestre su cuadrado.
Muestre su cubo.
Indique si es par o impar.
"""

#Primera funcion
def cuadrado_funcion(num):
    return num**2
#Segunda funcion
def cubo_funcion(num):
    return num**3
#Tercera funcion
def verificar (num):
    par_impar = num % 2
    if par_impar == 0:
        print("Es par")
    else:
        print("Es impar")
#Funcion main
def main():
    numero = int(input("Indica numero para hacer operaciones"))
    print(cuadrado_funcion(numero))
    print(cubo_funcion(numero))
    print(verificar(numero))
#Resultados
main()