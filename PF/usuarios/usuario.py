from conexionBD import conexion, cursor
import hashlib

def hash_password(password):
    """Hashea la contraseña usando SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def registrar(nombre, apellidos, email, contrasena):
    """Registra un nuevo usuario (cliente o administrador)."""
    try:
        contrasena = hash_password(contrasena)
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password) VALUES (%s, %s, %s, %s)"
        val = (nombre, apellidos, email, contrasena)
        cursor.execute(sql, val)
        conexion.commit()
        print("✅ Usuario registrado correctamente.")
        return True
    except Exception as e:
        print("❌ Error al registrar usuario:", e)
        return False

def iniciar_sesion(email, contrasena):
    """Valida el inicio de sesión."""
    try:
        contrasena = hash_password(contrasena)
        sql = "SELECT nombre, apellidos, email FROM usuarios WHERE email=%s AND password=%s"
        val = (email, contrasena)
        cursor.execute(sql, val)
        resultado = cursor.fetchone()
        return resultado  # Devuelve (nombre, apellidos, email) o None
    except Exception as e:
        print("❌ Error al iniciar sesión:", e)
        return None

def verificar_usuario(email, contrasena):
    """Verifica si un usuario existe en la base de datos."""
    try:
        contrasena = hash_password(contrasena)
        sql = "SELECT * FROM usuarios WHERE email=%s AND password=%s"
        val = (email, contrasena)
        cursor.execute(sql, val)
        resultado = cursor.fetchone()
        return resultado is not None
    except Exception as e:
        print("❌ Error al verificar usuario:", e)
        return False

def eliminar_usuario(email, contrasena):
    """Elimina un usuario según sus credenciales."""
    try:
        contrasena = hash_password(contrasena)
        sql = "DELETE FROM usuarios WHERE email=%s AND password=%s"
        val = (email, contrasena)
        cursor.execute(sql, val)
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("❌ Error al eliminar usuario:", e)
        return False
