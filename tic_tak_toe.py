import random

#dashborad..
board=["1","2","3","4","5","6","7","8","9"]

#print the board...
def show():
    print()
    print(board[0],"|", board[1],"|",  board[2])
    print("---------")
    print(board[3],"|", board[4],"|",  board[5])
    print("---------")
    print(board[6],"|", board[7],"|",  board[8])
    print()

#check for win..
def check_win(player):
    wins=[(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]        
    for i,j,k in wins:
        if board[i]==board[j]==board[k]==player:
            return True
    return False

#check for draw..
def is_draw():
    return all(cell in['X','O'] for cell in board)

#player move..
def player_move():
    while True:
        move = input("__YOUR MOVE__(1,9): ")
        if move not in board:
            print("__INVALID OR  ALREADY TAKEN..TRY AGAIN__")
        else:
            board[board.index(move)]="X"
            break

#computer move..
def computer_move():
    available=[cell for cell in board if cell not in ['X','O']]
    move= random.choice(available)
    board[board.index(move)]="O"
    print(f"__Computer Chose__ {move}")

#main game loop..
def play():
    print("__YB ! TIC TAC TOE !__")
    print("You are 'X', Computer is 'O'")
    show()

    while True:
        player_move()
        show()

        if check_win("X"):
            print("🎉 You Win!")
            break
        if is_draw():
            print("It's a Draw!")
            break

        computer_move()
        show()
        if check_win("O"):
            print("💻 Computer Wins!")
            break
        if is_draw():
            print("It's a Draw!")
            break

play()

