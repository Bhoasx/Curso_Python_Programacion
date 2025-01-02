from random import randrange

def display_board(board):
    """Muestra el tablero en su estado actual."""
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|  " + "  |  ".join(row) + "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    """Permite al usuario ingresar su movimiento."""
    while True:
        try:
            move = int(input("Ingresa tu movimiento: "))
            if move < 1 or move > 9:
                raise ValueError
            for row in range(3):
                for col in range(3):
                    if board[row][col] == str(move):
                        board[row][col] = 'O'
                        return
            print("El cuadro ya está ocupado. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entre 1 y 9.")

def make_list_of_free_fields(board):
    """Crea una lista de cuadros libres."""
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ('O', 'X'):
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    """Determina si el jugador con 'sign' ha ganado."""
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def draw_move(board):
    """Realiza el movimiento de la máquina de forma aleatoria."""
    free_fields = make_list_of_free_fields(board)
    row, col = free_fields[randrange(len(free_fields))]
    board[row][col] = 'X'

board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
board[1][1] = 'X'

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("¡La máquina ha ganado!")
        break
    if not make_list_of_free_fields(board):
        print("¡Es un empate!")
        break
    enter_move(board)
    if victory_for(board, 'O'):
        display_board(board)
        print("¡Has ganado!")
        break
    if not make_list_of_free_fields(board):
        print("¡Es un empate!")
        break
    draw_move(board)