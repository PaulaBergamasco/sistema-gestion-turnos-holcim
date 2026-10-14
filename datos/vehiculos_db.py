"""Acceso a datos de VEHICULO."""
from conexion import conectar

def listar_vehiculos():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT Patente, Marca, Modelo FROM VEHICULO ORDER BY Patente")
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        conexion.close()

def registrar_vehiculo(patente, marca, modelo):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            sql = "INSERT INTO VEHICULO (Patente, Marca, Modelo) VALUES (%s, %s, %s)"
            cursor.execute(sql, (patente, marca, modelo))
            conexion.commit()
            return True
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
    finally:
        conexion.close()

def eliminar_vehiculo(identificador):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("DELETE FROM VEHICULO WHERE Patente = %s", (identificador,))
            conexion.commit()
            return cursor.rowcount
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
    finally:
        conexion.close()
