"""
1. Solicite al usuario dos números (a y b).
2. Use una función para realizar las operaciones: suma, resta, multiplicación y división.
3. Maneje los siguientes errores:
   - Entrada inválida (ValueError).
   - División entre cero (ZeroDivisionError).
4. Asegúrate de mostrar un mensaje de error adecuado para cada caso.
"""

# Solicitar números al usuario con manejo de errores
def sol_num():
    try:
        a = int(input("Introduce un número a: "))
        b = int(input("Introduce un número b: "))
        return a, b
    except ValueError:
        print("Error: Debes introducir un número válido.")
        return None

# Realizar operaciones matemáticas
def operaciones(a, b):
    try:
        suma = a + b
        resta = a - b
        multi = a * b
        div = a / b
        print(f"Resultados:\nSuma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div}")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

# Función principal
def main():
    numeros = sol_num()
    if numeros:  # Verifica si `sol_num()` devolvió una tupla válida
        a, b = numeros
        operaciones(a, b)
        print (numeros)

main()
