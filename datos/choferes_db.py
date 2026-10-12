"""Acceso a datos de CHOFER. Completar CRUD: responsable de Choferes."""
from conexion import conectar

def listar_choferes():
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT DNI, Nombre, Apellido FROM CHOFER ORDER BY Apellido, Nombre")
            return cursor.fetchall()
        finally:
            cursor.close()
    finally:
        conexion.close()


