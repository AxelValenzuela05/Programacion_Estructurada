from funciones import *
from conexionBD import conexion, cursor
from datetime import datetime

def agregarProducto():
    borrarPantalla()
    print("\n📦 --- Agregar Nuevo Producto --- 📦")
    nombre = input("Nombre del producto: ").strip()

    # Validar nombre vacío
    if not nombre:
        print("❌ Nombre inválido.")
        esperarTecla()
        return

    # Verificar si ya existe el producto
    try:
        cursor.execute("SELECT id FROM productos WHERE nombre = %s", (nombre,))
        if cursor.fetchone():
            print(f"⚠️ El producto '{nombre}' ya existe. Operación cancelada.")
            esperarTecla()
            return
    except Exception as e:
        print(f"❌ Error al verificar existencia: {e}")
        esperarTecla()
        return

    # Pedir precio y stock
    try:
        precio = float(input("Precio: ").strip())
        stock = int(input("Stock inicial: ").strip())
    except ValueError:
        print("❌ Precio o stock inválido.")
        esperarTecla()
        return

    # Insertar nuevo producto
    try:
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)",
            (nombre, precio, stock)
        )
        conexion.commit()
        print(f"✅ Producto '{nombre}' agregado con éxito.")
    except Exception as e:
        print(f"❌ Error al agregar producto: {e}")



    try:
        sql = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
        val = (nombre, precio, stock)
        cursor.execute(sql, val)
        conexion.commit()
        print("✅ Producto agregado exitosamente.")
    except Exception as e:
        print(f"❌ Error al agregar producto: {e}")
    

def registrarVenta():
    borrarPantalla()
    print("\n🛒 --- Registrar Nueva Venta --- 🛒")

    productos_vendidos = []
    total_venta = 0

    while True:
        id_producto = input("ID de producto (deja vacío para terminar): ").strip()
        if not id_producto:
            break

        try:
            cantidad = int(input("Cantidad: ").strip())
        except ValueError:
            print("Cantidad inválida.")
            continue

        # Consulta producto para precio y stock
        cursor.execute("SELECT nombre, precio, stock FROM productos WHERE id = %s", (id_producto,))
        producto = cursor.fetchone()

        if not producto:
            print("Producto no encontrado.")
            continue

        nombre, precio, stock = producto

        if cantidad > stock:
            print(f"No hay suficiente stock. Disponible: {stock}")
            continue

        subtotal = precio * cantidad
        total_venta += subtotal
        productos_vendidos.append((id_producto, cantidad, precio))

        print(f"Agregado: {nombre} x{cantidad} = ${subtotal:.2f}")

    if not productos_vendidos:
        print("No se agregó ningún producto a la venta.")
        esperarTecla()
        return

    # Insertar la venta
    fecha_venta = datetime.now().date()
    cursor.execute("INSERT INTO ventas (fecha, total) VALUES (%s, %s)", (fecha_venta, total_venta))
    id_venta = cursor.lastrowid

    # Insertar detalle_venta y actualizar stock
    for id_prod, cant, precio_unit in productos_vendidos:
        cursor.execute(
            "INSERT INTO detalle_venta (id_venta, id_producto, cantidad, precio_unitario) VALUES (%s, %s, %s, %s)",
            (id_venta, id_prod, cant, precio_unit)
        )
        # Actualizar stock
        cursor.execute("UPDATE productos SET stock = stock - %s WHERE id = %s", (cant, id_prod))

    conexion.commit()
    print(f"\n✅ Venta registrada con total: ${total_venta:.2f}")
    