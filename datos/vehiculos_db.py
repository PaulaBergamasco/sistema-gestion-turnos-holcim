"""Acceso a datos de VEHICULO. Completar CRUD: responsable de Vehículos."""
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


