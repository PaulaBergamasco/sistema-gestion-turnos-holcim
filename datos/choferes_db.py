"""Acceso a datos de CHOFER."""
from conexion import conectar

def listar_choferes():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DNI, Nombre, Apellido, Telefono, Email FROM CHOFER ORDER BY Apellido, Nombre")
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        conexion.close()

def registrar_chofer(dni, nombre, apellido, telefono, email):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO CHOFER (DNI, Nombre, Apellido, Telefono, Email) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (dni, nombre, apellido, telefono, email))
            conexion.commit()
            return True
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
    finally:
        conexion.close()

def eliminar_chofer(identificador):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM CHOFER WHERE DNI = %s", (identificador,))
            conexion.commit()
            return cursor.rowcount
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
    finally:
        conexion.close()
