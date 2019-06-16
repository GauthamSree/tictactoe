import itertools

game_board = [['-','-','-'], 
              ['-','-','-'],
              ['-','-','-']]

def Game():
    print()
    for row in game_board:
        for col in row:
            print(col,end=' ')
        print()  
    print()    

def Tie():
    tie = True
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if game_board[row][col] == '-':
                tie = False
                return False      
    if tie:
        return tie

def Game_Win():

    def all_same(check):
        if check.count(check[0]) == len(check) and check[0] != '-':
            return True

    # Horizontal
    for row in game_board:
        if all_same(row):
            return True
   
    # Vertical
    for col in range(len(game_board)):
        check = []
        for row in game_board:
            check.append(row[col])
        if all_same(check):
            return True    

    # Diagonal
    check = []
    check1 = []
    for row in range(len(game_board)):
        for col in range(len(game_board)):
            if row == col:
                check.append(game_board[row][col])
            if (row + col) == (len(game_board) - 1):
                check1.append(game_board[row][col])     
    if all_same(check) or all_same(check1):
        return True     



player_choice = itertools.cycle(['X', 'O'])
Game()
while(True):      
    current_player = next(player_choice)
    
    while True :
        print("Player {}".format(current_player))
        row = int(input("Enter row(1, 2 or 3): "))
        col = int(input("Enter column(1, 2 or 3) : "))
        if row in [1, 2, 3] and col in [1, 2, 3]:
            if game_board[row-1][col-1] == '-':
                game_board[row-1][col-1] = current_player
                break
            else:
                print("Try Again! You can't play that move.\n")
        else:
            print("Try Again! You must input either 1, 2, or 3\n")        
    
    Game()
    tie_game = Tie()
    con = Game_Win()
    if(con):
        print("\nCongrats! Player {} has Won\n".format(current_player))
        break
    if(tie_game):
        print("\nTie\n")
        break    
