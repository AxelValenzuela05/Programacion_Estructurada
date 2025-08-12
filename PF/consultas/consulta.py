from conexionBD import conexion, cursor
from funciones import borrarPantalla, esperarTecla
def consultarVentasPorProducto():
    borrarPantalla()
    print("📦 --- Ventas por Producto --- 📦")

    nombre_producto = input("🔍 Ingresa el nombre del producto: ").strip()

    try:
        sql = """
            SELECT v.id_venta, v.fecha, p.nombre, dv.cantidad, dv.precio_unitario, 
                   (dv.cantidad * dv.precio_unitario) AS total
            FROM detalle_venta dv
            INNER JOIN productos p ON dv.id_producto = p.id
            INNER JOIN ventas v ON dv.id_venta = v.id_venta
            WHERE p.nombre LIKE %s
            ORDER BY v.fecha DESC, v.id_venta DESC
        """
        cursor.execute(sql, (f"%{nombre_producto}%",))
        resultados = cursor.fetchall()

        if resultados:
            # Encabezado de la tabla con bordes
            print("+" + "-"*8 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")
            print("| {:^6} | {:^10} | {:^20} | {:^8} | {:^12} | {:^12} |".format(
                "ID", "Fecha", "Producto", "Cant.", "Precio Unit.", "Total"
            ))
            print("+" + "-"*8 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")

            # Filas de la tabla
            for id_venta, fecha, nombre, cantidad, precio, total in resultados:
                print("| {:^6} | {:^10} | {:<20} | {:^8} | ${:>10.2f} | ${:>10.2f} |".format(
                    id_venta, str(fecha), nombre, cantidad, precio, total
                ))

            # Línea final de la tabla
            print("+" + "-"*8 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")
        else:
            print(f"⚠️ No hay ventas registradas para '{nombre_producto}'.")
    except Exception as e:
        print(f"❌ Error al consultar ventas por producto: {e}")

    

def consultarInventario():
    borrarPantalla()
    print("📦 --- Inventario de Productos --- 📦")
    try:
        # Solo selecciona productos activos
        sql = "SELECT id, nombre, precio, stock FROM productos WHERE activo = 1"
        cursor.execute(sql)
        productos = cursor.fetchall()

        if productos:
            # Encabezado de la tabla con bordes
            print("+" + "-"*32 + "+" + "-"*14 + "+" + "-"*10 + "+")
            print("| {:^30} | {:^12} | {:^8} |".format(
                "Producto", "Precio", "Stock"
            ))
            print("+" + "-"*32 + "+" + "-"*14 + "+" + "-"*10 + "+")

            # Filas de la tabla
            for id_prod, nombre, precio, stock in productos:
                print("| {:<30} | ${:>10.2f} | {:^8} |".format(
                    nombre, precio, stock
                ))

                # Si el stock es 0, marcar como inactivo
                if stock == 0:
                    cursor.execute("UPDATE productos SET activo = 0 WHERE id = %s", (id_prod,))
                    conexion.commit()

            # Línea final de la tabla
            print("+" + "-"*32 + "+" + "-"*14 + "+" + "-"*10 + "+")
        else:
            print("⚠️ No hay productos registrados.")
    except Exception as e:
        print(f"❌ Error al consultar inventario: {e}")





def consultarVentasPorDia():
    borrarPantalla()
    print("📆 --- Consultar Ventas por Día --- 📆")
    fecha = input("📅 Ingresa la fecha (YYYY-MM-DD): ").strip()

    try:
        sql = """
            SELECT v.id_venta, v.fecha, p.nombre, dv.cantidad, dv.precio_unitario,
                   (dv.cantidad * dv.precio_unitario) AS total
            FROM ventas v
            INNER JOIN detalle_venta dv ON v.id_venta = dv.id_venta
            INNER JOIN productos p ON dv.id_producto = p.id
            WHERE v.fecha = %s
            ORDER BY v.id_venta
        """
        cursor.execute(sql, (fecha,))
        ventas = cursor.fetchall()

        if ventas:
            total_dia = sum(row[5] for row in ventas)

            # Encabezado
            print("\n+" + "-"*10 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")
            print("| {:^8} | {:^10} | {:^20} | {:^8} | {:^12} | {:^12} |".format(
                "ID Venta", "Fecha", "Producto", "Cant.", "Precio Unit.", "Total"
            ))
            print("+" + "-"*10 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")

            # Filas
            for id_venta, fecha_v, nombre, cantidad, precio, total in ventas:
                print("| {:^8} | {:^10} | {:<20} | {:^8} | ${:>10.2f} | ${:>10.2f} |".format(
                    id_venta, str(fecha_v), nombre, cantidad, precio, total
                ))

            # Línea final
            print("+" + "-"*10 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")

            # Total del día
            print("| {:^8} | {:^10} | {:<20} | {:^8} | {:^12} | ${:>10.2f} |".format(
                "TOTAL", "", "", "", "", total_dia
            ))
            print("+" + "-"*10 + "+" + "-"*12 + "+" + "-"*22 + "+" + "-"*10 + "+" + "-"*14 + "+" + "-"*14 + "+")
        else:
            print("⚠️ No hay ventas registradas para esa fecha.")
    except Exception as e:
        print(f"❌ Error al consultar ventas: {e}")

   


