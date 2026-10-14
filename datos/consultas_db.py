"""Consultas de turnos"""
from conexion import conectar

def buscar_turnos(criterio="Patente / Vehículo", termino=""):
    columnas = {
        "Patente / Vehículo": "V.Patente",
        "DNI / Chofer": "C.DNI",
        "Número de Turno": "T.ID",
        "Estado": "T.Estado",
    }
    if criterio not in columnas:
        raise ValueError("Criterio de búsqueda inválido")
    conexion = conectar()
    try:
        cursor = conexion.cursor()
        try:
            sql = """SELECT T.ID, V.Patente, C.DNI,
                     CONCAT(C.Nombre, ' ', C.Apellido),
                     DATE_FORMAT(T.Fecha, '%d/%m/%Y'),
                     TIME_FORMAT(T.Hora, '%H:%i'), T.Estado
                     FROM TURNO T
                     JOIN CHOFER C ON C.DNI = T.DNI_Chofer
                     JOIN VEHICULO V ON V.Patente = T.Patente"""
            parametros = ()
            if termino:
                sql += " WHERE " + columnas[criterio] + " LIKE %s"
                parametros = ("%" + termino + "%",)
            sql += " ORDER BY T.Fecha, T.Hora"
            cursor.execute(sql, parametros)
            return [(id_, patente, dni, nombre, f"{fecha} {hora}", estado)
                    for id_, patente, dni, nombre, fecha, hora, estado in cursor.fetchall()]
        finally:
            cursor.close()
    finally:
        conexion.close()
