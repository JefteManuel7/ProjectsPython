
import modulo as m

inventario = m.Inventario()
producto_fisico = m.ProductoFisico('caja', 10, 4, 20, (4, 5 , 5))
producto_digital = m.ProductoDigital('foto', 100, 10, 40)

inventario.agregar_productos(producto_fisico)
inventario.agregar_productos(producto_digital)

# Mostrar productos
for producto in inventario.productos:
    print(producto.nombre)
    print(producto.cantidad)


# Actualizar producto
inventario.actualizar_cantidad_productos('caja', 20)

for producto in inventario.productos:
    print(producto.nombre)
    print(producto.cantidad)