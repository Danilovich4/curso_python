class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto {self.nombre}, Precio: {self.precio}€, Cantidad: {self.cantidad}"

    def __add__(self, otro_producto):
        # Verifica que los nombres coincidan
        if self.nombre == otro_producto.nombre:
            # Suma las cantidades y retorna un nuevo objeto Producto
            return Producto(self.nombre, self.precio, self.cantidad + otro_producto.cantidad)
        else:
            raise ValueError("No se pueden sumar productos con nombres diferentes.")

# Pruebas
p1 = Producto("Manzana", 0.5, 10)
p2 = Producto("Manzana", 0.5, 15)

print(p1)
print(p2)

p3 = p1 + p2
print(p3)
