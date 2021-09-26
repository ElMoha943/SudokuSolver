def isSafe(board, x, y, value): #Verificacion de que la jugada es valida
    for i in range(9):
        if(board[x][i] == value): #El numero se repite en la misma columna?
            return False
        elif(board[i][y] == value): #El numero se repite en la misma fila?
            return False
    startRow = x - x % 3
    startCol = y - y % 3
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == value: #El numero se repite en la misma caja?
                return False
    return True


def searchBlank(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return(i, j)
    return None

def solve(board): #Backtrack que resuelve el problema
    aux = searchBlank(board)  #Busca un espacio vacio en el tablero, devuelve una variable vacia (falso) si no lo encuentra.
    if aux:
        x, y = aux
    else:
        return True
    for i in range(1,10): #Prueba todos los numeros posibles para esa posicion.
        if(isSafe(board, x, y, i)): 
            board[x][y] = i #Aplica los cambios si el movimiento es valido
            if(solve(board)):
                return True 
            else:
                board[x][y] = 0 #Deshace los cambios si se encontro un error.
    return False #Avisa al paso anterior que ubo un error.


#Inicialziacion del tablero
board = [
    [0,0,6,5,7,0,0,0,8],
    [0,0,0,8,0,0,3,0,0],
    [0,5,9,0,0,6,0,0,2],
    [0,3,0,0,5,0,0,0,4],
    [0,4,5,2,6,0,8,7,0],
    [0,0,0,0,0,0,5,0,0],
    [9,0,4,0,8,7,2,5,0],
    [0,6,0,0,0,0,0,0,0],
    [0,8,0,0,3,4,6,0,0]
]

if(solve(board)): #Muestra el tablero resuelto
    for i in range(9):
        print('\n')
        for j in range(9):
            print(board[i][j], end =" ")
            if j == 2 or j == 5 or j == 9:
                print('|', end =" ")
        if i == 2 or i == 5 or i == 9:
                print('\n---------------------', end =" ")
else:
    print("Este sudoku no tiene solucion!")
