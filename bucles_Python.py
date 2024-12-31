largest_number = -999999999

number = int(input("Introduce un número o escribe -1 para detener: "))

while number != -1:
    if number > largest_number:
        largest_number = number
    number = int(input("Introduce un número o escribe -1 para detener: "))

print("El número más grande es:", largest_number)


odd_numbers = 0
even_numbers = 0

number = int(input("Introduce un número o escribe 0 para detener: "))

while number != 0:
    if number % 2 == 1:
        odd_numbers += 1
    else:
        even_numbers += 1.
    number = int(input("Introduce un número o escribe 0 para detener: "))

print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

#-----------------------------------------------

for i in range(2, 8):
    print("El valor de i es", i)