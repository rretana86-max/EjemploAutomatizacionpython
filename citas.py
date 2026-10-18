def obtener_citas():
    # Lista de citas programadas con datos de ejemplo
    citas_programadas =[
        {
            "id": 1,
            "paciente": "Ana García",
            "fecha": "2026-09-14",
            "hora": "09:30",
            "motivo": "Consulta general",
            "estado": "Pendiente"
        },
        {
            "id": 2,
            "paciente": "Luis Pérez",
            "fecha": "2026-09-14",
            "hora": "11:00",
            "motivo": "Control de presión",
            "estado": "Programada"
        },

        {
            "id": 3,
            "paciente": "Sofía López",
            "fecha": "2026-09-15",
            "hora": "15:45",
            "motivo": "Revisión médica",
            "estado": "Pendiente"
        }

    ]
    return citas_programadas

def crear_cita():
    # Función para crear una nueva cita (simulación)
    nueva_cita = {
        "id": 4,
        "paciente": "Carlos Martínez",
        "fecha": "2026-09-16",
        "hora": "10:15",
        "motivo": "Consulta de seguimiento",
        "estado": "Programada"
    }
    return nueva_cita   
   

def obtener_cita_por_fecha(fecha):
    # Función para obtener citas por fecha
    citas = obtener_citas()
    citas_por_fecha = [cita for cita in citas if cita['fecha'] == fecha]
    return citas_por_fecha