def decorador(funcion):
    def nueva_funcion(*args, **kwargs):
        print("Inicio de la funcion")
        result = funcion(*args, **kwargs)
        print("Fin de la funcion")
        return result
    return nueva_funcion

@decorador
def sumar(a, b):
    suma = a + b
    print(f"La suma es: {suma}")

sumar(5, 3)
