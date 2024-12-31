original_list = [1, 2, 3, 4, 3, 2, 1, 5, 6, 5, 7, 8, 7]

unique_list = []

for number in original_list:
    if number not in unique_list:
        unique_list.append(number)

print("Lista original:", original_list)
print("Lista sin duplicados:", unique_list)