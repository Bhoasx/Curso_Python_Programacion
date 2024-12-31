
bloques = int(input("Ingresa el número de bloques: "))

altura = 0
bloques_usados = 0

while bloques_usados + (altura + 1) <= bloques:
    altura += 1
    bloques_usados += altura

print(f"La altura de la pirámide es: {altura}")