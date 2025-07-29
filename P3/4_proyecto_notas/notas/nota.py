from conexionBD import *

def crear(usuario_id,titulo,descripcion):
    try:
        cursor.execute("insert into (usuario_id,titulo,descripcion,fecha) values (%s,%s,%s,NOW())",(usuario_id,titulo,descripcion))
        conexion.commit()
        return True
    except:
        return False

def mostrar(usuario_id):

    try:
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        cursor.fetchall()
        if len(lista)>0:
            return lista
        else:
            return []
    except: 
        return[]
    

def cambiar(id, titulo,descripcion):
    try:
        cursor.execute("update notas set titulo=%s,descripcion=%s,fecha=NOW()"where id=%s,(titulo,descripcion,id))
        conexion.commit()
        return True
    except:
        return False