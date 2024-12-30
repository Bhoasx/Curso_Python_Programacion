
hora_inicio = 12
minuto_inicio = 17

duracion = 59

minutos_totales = minuto_inicio + duracion
hora_final = hora_inicio + minutos_totales // 60
minuto_final = minutos_totales % 60

hora_final = hora_final % 24

print(f"El evento termina a las {hora_final:02}:{minuto_final:02}")
