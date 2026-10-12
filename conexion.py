"""Conexión común a MySQL. Las credenciales se leen desde .env."""
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "holcim_turnos"),
    )
