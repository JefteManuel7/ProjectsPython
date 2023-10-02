# Modulo que contienen las funciones  para manejar software de control de inventario

#
class Producto:
    """
    Clase abstracta que representa un producto en un inventario.

    Atributos: 
        Nombre (str): Nombre del producto.
        precio (float): Precio del producto.
        cantidad (int): Cantidad de unidades en el inventario.

    """
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad


class ProductoFisico(Producto):
    """
        Clase abstracta derivada de Producto que representa un producto fisico

        Atributos:
            Peso (float)           : Peso del producto en kilogramos 
            Dimensiones (tuple)    : Dimensiones del producto en centimetros.(alto, ancho)
    """
    def __init__(self, nombre, precio, cantidad, peso, dimensiones):
        super().__init__(nombre, precio, cantidad)
        self.peso = peso
        self.dimensiones = dimensiones
    

class ProductoDigital(Producto):
    """
        Clase abstracta derivada de Producto que representa un producto digital

        Atributos:
            tamanio (float) : Tamaño del producto en megabytes
    """
    def __init__(self, nombre, precio, cantidad, tamanio):
        super().__init__(nombre, precio, cantidad)
        self.tamanio = tamanio



class Inventario:
    """
        Clase que representa un inventario de productos
        Atributos:
            Productos (lista): Lista de productos en el inventario.
    """

    def __init__(self):
        self.productos = []

    def agregar_productos(self, producto):
        """
        Agregar producto al inventario.
        Atributos:
            Producto(str): Nombre del producto a agregar.
        """
        self.productos.append(producto)

    def actualizar_cantidad_productos(self, nombre, cantidad):
        """
        Actualiza la cantidad de productos en el inventario
        Atributos:
            Nombre(str): Nombre del producto a actualizar
            Cantidad(int): cantidad de producto a actualizar
        """
        producto = self.buscar_producto(nombre)
        if producto is not None:
            producto.cantidad = cantidad


    def eliminar_productos(self, nombre):
        """
        Elimina el producto en el inventario
        Atributos:
            Nombre(str): Nombre del producto a eliminar
        """
        productos = self.buscar_producto(nombre)
        if productos is not None:
            productos.remove(nombre)

    def buscar_producto(self, nombre):
        """
        Busca  el producto en el inventario
        Atributos:
            Nombre(str): Nombre del producto a buscar
        """
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None
    

    #def listar_product(self):
        """
        Listar los producto en el inventario
        Atributos:
            Nombre(str): Nombre del producto a buscar
        """
        #for producto in Inventario.productos:
        
        
    