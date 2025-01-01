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

pruebas = [
    (1900, 2, 28), 
    (2000, 2, 29), 
    (2023, 4, 30),
    (2024, 2, 29),
    (2023, 13, None),  
    (2023, 0, None), 
    (-1, 1, None),
    (2023, 1, 31),
]

for anio, mes, esperado in pruebas:
    resultado = dias_en_mes(anio, mes)
    if resultado == esperado:
        print(f"Año {anio}, Mes {mes}: OK (Días: {resultado})")
    else:
        print(f"Año {anio}, Mes {mes}: Error (Esperado: {esperado}, Obtenido: {resultado})")