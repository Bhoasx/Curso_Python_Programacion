beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

for miembro in ["Stu Sutcliffe", "Pete Best"]:
    nuevo_miembro = input(f"Ingresa el nombre de {miembro}: ")
    beatles.append(nuevo_miembro)
print("Paso 3:", beatles)

del beatles[-2:] 
print("Paso 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)

print("Los Beatles finales:", beatles)