from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, apellidos, email,):
    try:
        fetch=datatime.datatime.now()
        sql="insert into (nombre, apellidos, email, password, fecha) values ($s,$s,$s,$s,$s)"

        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False

def inicio_sesion(email,contrasena):
    try:
        sql="slect * from usuarios where email=$s and password=$s"
        val=(email,contrasena)
        cursor.execute(sql,val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
        
