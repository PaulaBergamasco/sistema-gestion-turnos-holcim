"""Acceso a datos de TURNO."""
from conexion import conectar

def horarios_ocupados(fecha):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute("SELECT Hora FROM TURNO WHERE Fecha = %s", (fecha,))
            return {str(fila[0])[:5] for fila in cursor.fetchall()}
        finally:
            cursor.close()
    finally:
        conexion.close()


def registrar_turno(fecha, hora, dni_chofer, patente):
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            cursor.execute(
                "INSERT INTO TURNO (Fecha, Hora, DNI_Chofer, Patente) VALUES (%s, %s, %s, %s)",
                (fecha, hora, dni_chofer, patente),
            )
            conexion.commit()
            return cursor.lastrowid
        except Exception:
            conexion.rollback()
            raise
        finally:
            cursor.close()
    finally:
        conexion.close()
