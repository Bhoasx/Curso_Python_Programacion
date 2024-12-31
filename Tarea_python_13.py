
c0 = int(input("Ingresa un número natural: "))

if c0 <= 0:
    print("El número debe ser un entero positivo mayor que cero.")
else:
    pasos = 0 

    while c0 != 1:
        print(c0) 
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        pasos += 1 

    print(c0)
    print(f"Se necesitaron {pasos} pasos para alcanzar 1.")
