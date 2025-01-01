def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    return False

datos_prueba = [1900, 2000, 2004, 2100, 2200, 2400, 2023]
resultados_esperados = [False, True, True, False, False, True, False]

for i in range(len(datos_prueba)):
    anio = datos_prueba[i]
    resultado = es_bisiesto(anio)
    if resultado == resultados_esperados[i]:
        print(f"Año {anio}: OK")
    else:
        print(f"Año {anio}: Error (Esperado: {resultados_esperados[i]}, Obtenido: {resultado})")