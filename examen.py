class Producto:
    def __init__(self, id_producto, nombre_producto, precio, cantidad_stock):
        self.id_producto = id_producto
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.cantidad_stock = cantidad_stock

    def verificar_stock(self, cantidad):
        if self.cantidad_stock >= cantidad:
            return True
        else:
            raise ValueError(f"No hay suficiente stock para {self.nombre_producto}")

    def actualizar_stock(self, cantidad):
        if cantidad > self.cantidad_stock:
            raise ValueError(f"No hay suficiente stock para actualizar {self.nombre_producto}")
        self.cantidad_stock -= cantidad


class Cliente:
    def __init__(self, nombre, telefono, direccion):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    def realizar_pedido(self, pedido):
        print(f"{self.nombre} ha realizado un pedido.")
        pedido.procesar_pedido()


class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = []
        self.estado = "Pendiente"

    def agregar_producto(self, producto, cantidad):
        self.productos.append((producto, cantidad))

    def calcular_total(self):
        total = sum([producto.precio * cantidad for producto, cantidad in self.productos])
        return total

    def procesar_pedido(self):
        try:
            for producto, cantidad in self.productos:
                producto.verificar_stock(cantidad)
                producto.actualizar_stock(cantidad)
            self.estado = "Procesado"
            print("Pedido procesado exitosamente.")
        except ValueError as e:
            print(f"Error: {e}")
            self.estado = "Error"
        finally:
            print(f"Estado del pedido: {self.estado}")
            self.notificar_cliente()

    def notificar_cliente(self):
        print(f"Notificando a {self.cliente.nombre} que su pedido está {self.estado}.")


class ControlDeProductos:
    def __init__(self, productos_disponibles):
        self.productos_disponibles = productos_disponibles

    def verificar_stock(self, producto, cantidad):
        for p in self.productos_disponibles:
            if p.id_producto == producto.id_producto:
                return p.verificar_stock(cantidad)
        raise ValueError(f"Producto {producto.nombre_producto} no encontrado en el inventario.")

    def actualizar_stock(self, producto, cantidad):
        for p in self.productos_disponibles:
            if p.id_producto == producto.id_producto:
                p.actualizar_stock(cantidad)
                return
        raise ValueError(f"Producto {producto.nombre_producto} no encontrado en el inventario.")


class Cocina:
    def __init__(self):
        self.estado_pedido = "Pendiente"

    def preparar_pedido(self, pedido):
        self.estado_pedido = "Preparando"
        print("Cocina está preparando el pedido.")

    def notificar_preparacion(self, pedido):
        self.estado_pedido = "Listo"
        print(f"Pedido {pedido.id_pedido} está listo para ser entregado.")


# Ejemplo de uso:

producto1 = Producto(1, "Pizza", 10.0, 5)
producto2 = Producto(2, "Pasta", 8.0, 3)

control = ControlDeProductos([producto1, producto2])
cliente = Cliente("Juan", "123456789", "Calle Ficticia 123")
pedido = Pedido(1, cliente)

pedido.agregar_producto(producto1, 2)
pedido.agregar_producto(producto2, 1)

cliente.realizar_pedido(pedido)
