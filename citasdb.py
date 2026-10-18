import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def connection_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def obtener_citas():
    conexion = connection_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, paciente, fecha, hora, motivo, estado FROM citas")
    filas = cursor.fetchall()
    conexion.close()

    citas = []
    for fila in filas:
        citas.append({
            "id": fila[0],
            "paciente": fila[1],
            "fecha": str(fila[2]),
            "hora": str(fila[3]),
            "motivo": fila[4],
            "estado": fila[5]
        })
    return citas