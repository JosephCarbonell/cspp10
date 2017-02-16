def print_board(board):
    print(" {} | {} | {}".format(board[0],board[1],board[2]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[3],board[4],board[5]))
    print("---+---+---")
    print(" {} | {} | {}".format(board[6],board[7],board[8]))
    


def take_player_move(current_player,current_board):
    while True:
        print_board(current_board)
        player_choice = input("Player {}, enter your move as a number from 1 to 9: ".format(current_player))
        if player_choice.isdigit() == True:
            player_choice = int(player_choice)
            position_in_list = player_choice - 1
            while True:  
                if current_board[position_in_list] == player_choice:
                    current_board[position_in_list] = current_player
                    break
                else:
                    print ("Invalid input, please try again")
            break
        else:
            print ("Invalid input, please try again")


            
def swap_player(current_player):
    if current_player == "X":
        return "O"
    elif current_player == "O":
        return "X"


def check_win_conditions(current_board):
    possible_win_conditions = [[0,3,6],
    [1,4,7],
    [2,5,8],
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,4,8],
    [2,4,6]
    ]
    first_check = ""
    second_check = ""
    third_check = ""
    for item in possible_win_conditions:
        first_check = current_board[item[0]]
        second_check = current_board[item[1]]
        third_check = current_board[item[2]]
        if first_check == second_check and first_check == third_check:
            if first_check == "X":
                return ("X wins!")
            elif first_check == "O":
                return ("O wins!")
                




def tic_tac_toe_game():
    board = [1,2,3,4,5,6,7,8,9]
    current_player = "X"
    while True:
        take_player_move(current_player, board)
        win_check = (check_win_conditions(board))
        if win_check == "X wins!":
            print("Player X wins!")
            break
        elif win_check == "O wins!":
            print("Player O wins!")
            break
        current_player = swap_player(current_player)
        
tic_tac_toe_game()
        
