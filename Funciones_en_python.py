print("Ingresa un valor: ")
a = int(input())

print("Ingresa un valor: ")
b = int(input())

print("Ingresa un valor: ")
c = int(input())


def message():
    print("Ingresar valor: ")

print("Inicia aqui.")
message()
print("Termina aqui.")

def message():
    print("Ingresar valor: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

def message(number):
    print("Ingresa un número:", number)

message(1)

def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)

def message(number):
    print("Ingresa un número:", number)

number = 1234
message(1)
print(number)

def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

introduction()

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return

    print("¡Feliz año nuevo!")

def strange_function(n):
    if(n % 2 == 0):
        return True
    
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))