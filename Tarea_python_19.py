def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

def dias_en_mes(anio, mes):
    """Devuelve el número de días en un mes para un año dado."""
    if mes < 1 or mes > 12 or anio < 1:
        return None
    
    dias_por_mes = [31, 29 if es_bisiesto(anio) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dias_por_mes[mes - 1]

def dia_del_anio(anio, mes, dia):
    """Devuelve el día correspondiente del año para una fecha dada."""
    if mes < 1 or mes > 12 or anio < 1 or dia < 1:
        return None 

    dias_en_este_mes = dias_en_mes(anio, mes)
    if not dias_en_este_mes or dia > dias_en_este_mes:
        return None
    dia_anual = 0
    for m in range(1, mes):
        dia_anual += dias_en_mes(anio, m)
    
    dia_anual += dia
    return dia_anual

pruebas = [
    (2023, 1, 1, 1), 
    (2023, 12, 31, 365),
    (2024, 12, 31, 366),
    (2024, 2, 29, 60),  
    (2023, 4, 30, 120), 
    (2023, 2, 29, None), 
    (2023, 13, 1, None), 
    (-1, 1, 1, None),    
]

for anio, mes, dia, esperado in pruebas:
    resultado = dia_del_anio(anio, mes, dia)
    if resultado == esperado:
        print(f"Año {anio}, Mes {mes}, Día {dia}: OK (Resultado: {resultado})")
    else:
        print(f"Año {anio}, Mes {mes}, Día {dia}: Error (Esperado: {esperado}, Obtenido: {resultado})")