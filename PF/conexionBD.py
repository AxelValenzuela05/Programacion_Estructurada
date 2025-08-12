import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_tiendita"  # <- Cambia este nombre si usarás otro
    )
    cursor = conexion.cursor(buffered=True)
except:
    print("⚠️ En este momento no es posible comunicarse con la base de datos. Inténtalo más tarde.")
