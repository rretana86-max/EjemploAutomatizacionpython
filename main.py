



#print("Citas programadas: ")
from citas import obtener_cita_por_fecha ,obtener_citas

#bnio¿¿from notificaciones import enviar_notificacion

""" for cita in obtener_citas(): # Llamar a la función obtener_citas para obtener la lista de citas programadas
 print(f"ID: {cita['id']}, Paciente: {cita['paciente']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}")  # Imprimir los  """

""" print("\nCitas por fecha: ") 
fecha_busqueda = "2026-09-14"
citas_encontradas = obtener_cita_por_fecha(fecha_busqueda)
 """
# validamos si esta vacía la lista de citas encontradas
""" if not citas_encontradas:
    print(f"No se encontraron citas para la fecha {fecha_busqueda}.")
 """


#************************Imprimir los detalles de las citas encontradas para la fecha especificada**********************************

""" for cita in citas_encontradas:
    print(f"ID: {cita['id']}, Paciente: {cita['paciente']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}")

 """



#****************************************Genera  la notificacion  para el paciente ***************************************************   


""" print("\nNotificaciones:c ")

for cita in citas_encontradas:
       if cita['estado'] == "Programada":
           print(f"hola {cita['paciente']}  le recordamos que tienes una cita programada  para el {cita['fecha']} a las {cita['hora']}.")

 """






 # ***************************** send notification through whatsApp ******************************************
""" for cita in citas_encontradas:
       if cita['estado'] == "Programada":
          enviar_notificacion(cita) 
 """



from leerjson import leer_json 

from citasdb import  obtener_citas as leer_citas_db


for cita in leer_citas_db():
    print(f"ID:{cita['id']},P")
""" leerjson = leer_json("Jsonejemplo.txt")

for cita in leerjson:
    print(f"ID: {cita['id']}, Paciente: {cita['paciente']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}")
"""