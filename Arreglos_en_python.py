numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers) 

numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)

numbers[0] = 111
print("\nPrevio contenido de la lista:", numbers) 

numbers[1] = numbers[4]
print("Nuevo contenido de la lista:", numbers) 