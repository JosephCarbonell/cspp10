import random 
import getpass
def main():
    rps_game()
    
# def rps_game():
#     print ("Welcome to Rock Paper Scissor!")
#     global computer_score
#     global player_score
#     computer_score = 0
#     player_score = 0
#     num_of_rounds = int(input("How many rounds would you like to play?"))
#     for x in range(num_of_rounds):
#         print("It is round {}.".format(x + 1))
#         print("The current score is Computer:{} to Player:{}".format(computer_score, player_score))
#         player_choice = input("Enter Rock,Paper,or Scissors: ")
#         computer_choice = random.randint(1,3)
#         #1 is rock, 2 is paper, 3 is scissors
#         if computer_choice == 1:
#             print("Computer chose Rock")
#         elif computer_choice == 2:
#             print("Computer chose Paper")
#         else:
#             print("Computer chose Scissors")
            
#         if player_choice == "Rock":
#             if computer_choice == 1:
#                 print("It was a tie")
#             elif computer_choice == 2:
#                 print("The computer won")
#                 computer_score = computer_score + 1
#             else:
#                 print("The player won")
#                 player_score = player_score + 1
#         elif player_choice == "Paper":
#             if computer_choice == 1:
#                 print("The player won")
#                 player_score = player_score + 1
#             elif computer_choice == 2:
#                 print("It was a tie")
#             else:
#                 print("The computer won")
#                 computer_score = computer_score + 1
#         else:
#             if computer_choice == 1:
#                 print("The computer won")
#                 computer_score = computer_score + 1
#             elif computer_choice == 2:
#                 print("The player won")
#                 player_score = player_score + 1
#             else:
#                 print("It was a tie")
            
#         if player_score > num_of_rounds / 2:
#             print("The player won! The score was Player:{} to Computer:{}".format(player_score, computer_score))
#             break
#         elif computer_score > num_of_rounds / 2:
#             print("The computer won! The score was Player:{} to Computer:{}".format(player_score, computer_score))
#             break
            
def get_p1_move():
    player_choice = input("Enter Rock,Paper,or Scissors: ")
    return player_choice

def get_comp_move():
    computer_choice = random.randint(1,3)
    return computer_choice

    
def get_rounds():
    num_of_rounds = int(input("Enter the number of rounds you wish to play"))
    return num_of_rounds
    
    
def get_round_winner(player_choice,computer_choice):
    global player_score
    global computer_score
    global num_of_ties
    player_score = 0
    computer_score = 0
    num_of_ties = 0
    if player_choice == "Rock":
        if computer_choice == 1:
            num_of_ties = num_of_ties + 1
            return ("It was a tie")
        elif computer_choice == 2:
            computer_score = computer_score + 1
            return ("The winner is computer")
        else:
            player_score = player_score + 1
            return ("The winner is player")
    elif player_choice == "Paper":
        if computer_choice == 1:
            player_choice = player_choice + 1
            return("The winner is player")
        elif computer_choice == 2:
            num_of_ties = num_of_ties + 1
            return("It was a tie")
        else:
            computer_score = computer_score + 1
            return("The winner is computer")
    else:
        if computer_choice == 1:
            computer_score = computer_score + 1
            return("The winner is computer")
        elif computer_choice == 2:
            player_score = player_score + 1
            return("The winner is player")
        else:
            num_of_ties = num_of_ties + 1
            return("It was a tie")
            
def get_full_move(com_choice):
    if com_choice == 1:
        return ("Rock")
    elif com_choice == 2:
        return("Paper")
    else:
        return("Scissors")

def keep_score(winner):
    global player_score
    global computer_score
    global num_of_ties
    if winner == "player":
        player_score = player_score + 1
    elif winner == "computer":
        computer_score = computer_score + 1
    else:
        num_of_ties = num_of_ties + 1
        
        

def print_score():
    global player_score
    global computer_score
    global num_of_ties
    return("The score is Computer:{} Player:{} and Ties:{}.".format(computer_score,player_score,num_of_ties))

def rps_game():
    print("Welcome to Rock,Paper,Scissors!")
    for x in range(get_rounds()):
        p1_move = get_p1_move()
        comp_move = get_comp_move()
        print ("It is round {}".format(x + 1))
        print ("Player entered {}.".format(p1_move))
        print ("Computer entered {}.".format(get_full_move(comp_move)))
        keep_score(get_round_winner(p1_move,comp_move))
        print ("{}".format(get_round_winner(p1_move,comp_move)))
        print (print_score())
        
        



main()

    
    
        
    
    
    
    
        
        
        
    