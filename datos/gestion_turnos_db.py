"""Funciones propias de Gestión de Turnos."""

from conexion import conectar


def listar_turnos():
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        try:
            cursor.execute("""
                SELECT
                    T.ID,
                    DATE_FORMAT(T.Fecha, '%d/%m/%Y'),
                    TIME_FORMAT(T.Hora, '%H:%i'),
                    CONCAT(C.Nombre, ' ', C.Apellido),
                    CONCAT(V.Patente, ' - ', V.Marca, ' ', V.Modelo),
                    T.Estado
                FROM TURNO T
                JOIN CHOFER C ON T.DNI_Chofer = C.DNI
                JOIN VEHICULO V ON T.Patente = V.Patente
                ORDER BY T.Fecha, T.Hora
            """)

            return cursor.fetchall()

        finally:
            cursor.close()

    finally:
        conexion.close()


def modificar_turno(id_turno, fecha, hora):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        try:
            cursor.execute(
                """
                UPDATE TURNO
                SET Fecha = %s, Hora = %s
                WHERE ID = %s
                """,
                (fecha, hora, id_turno)
            )

            conexion.commit()

        except Exception:
            conexion.rollback()
            raise

        finally:
            cursor.close()

    finally:
        conexion.close()


def cambiar_estado(id_turno, nuevo_estado):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        try:
            cursor.execute(
                """
                UPDATE TURNO
                SET Estado = %s
                WHERE ID = %s
                """,
                (nuevo_estado, id_turno)
            )

            conexion.commit()

        except Exception:
            conexion.rollback()
            raise

        finally:
            cursor.close()

    finally:
        conexion.close()


def eliminar_turno(id_turno):
    conexion = conectar()

    try:
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "DELETE FROM TURNO WHERE ID = %s",
                (id_turno,)
            )

            conexion.commit()

        except Exception:
            conexion.rollback()
            raise

        finally:
            cursor.close()

    finally:
        conexion.close()
