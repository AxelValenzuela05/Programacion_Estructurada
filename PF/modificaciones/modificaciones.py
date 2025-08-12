from conexionBD import conexion, cursor
from funciones import borrarPantalla, esperarTecla

# Función para editar un producto existente
def editarProducto():
    borrarPantalla()
    try:
        id_producto = int(input("🆔 Ingresa el ID del producto a editar: "))
        nuevo_nombre = input("📦 Nuevo nombre del producto: ").strip()
        nuevo_precio = float(input("💵 Nuevo precio: "))
        nuevo_stock = int(input("📦 Nuevo stock: "))

        sql = "UPDATE productos SET nombre = %s, precio = %s, stock = %s WHERE id = %s"
        val = (nuevo_nombre, nuevo_precio, nuevo_stock, id_producto)
        cursor.execute(sql, val)
        conexion.commit()

        print("✅ Producto actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error al actualizar el producto: {e}")

def reabastecerStock():
    borrarPantalla()
    print("\n📦 --- Reabastecer Stock --- 📦")
    nombre = input("Nombre del producto: ").strip()

    # Verificar si existe
    try:
        cursor.execute("SELECT id, stock FROM productos WHERE nombre = %s", (nombre,))
        producto = cursor.fetchone()
        if not producto:
            print(f"❌ El producto '{nombre}' no existe.")
            esperarTecla()
            return

        stock_actual = producto[1]
        cantidad = int(input(f"Cantidad a agregar (stock actual: {stock_actual}): ").strip())

        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a cero.")
            esperarTecla()
            return

        nuevo_stock = stock_actual + cantidad
        cursor.execute("UPDATE productos SET stock = %s WHERE id = %s", (nuevo_stock, producto[0]))
        conexion.commit()
        print(f"✅ Stock actualizado: {nombre} ahora tiene {nuevo_stock} unidades.")

    except Exception as e:
        print(f"❌ Error al reabastecer stock: {e}")






