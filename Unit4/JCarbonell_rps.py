import random 
import getpass
player_score = 0
computer_score = 0
num_of_ties = 0
def main():
    rps_game()
    

def get_p1_move():
    player_choice = input("Enter Rock,Paper,or Scissors: ")
    return player_choice

def get_comp_move():
    computer_choice = random.randint(1,3)
    return computer_choice

    
def get_rounds():
    num_of_rounds = int(input("Enter the number of rounds you wish to play: "))
    return num_of_rounds
    
    
def get_round_winner(player_choice,computer_choice):
    global player_score
    global computer_score
    global num_of_ties
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
            player_score = player_score + 1
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
    global player_score
    global computer_score
    global num_of_ties
    num_of_rounds = get_rounds()
    for x in range(num_of_rounds):
        if player_score > num_of_rounds / 2:
            print ("Player wins")
            break
        elif computer_score > num_of_rounds / 2:
            print("Computer wins")
            break
        p1_move = get_p1_move()
        comp_move = get_comp_move()
        print ("It is round {}".format(x + 1))
        print ("Player entered {}.".format(p1_move))
        print ("Computer entered {}.".format(get_full_move(comp_move)))
        round_winner = (get_round_winner(p1_move,comp_move))
        print ("{}".format(round_winner))
        print (print_score())
    if player_score > computer_score:
        print ("The player won! The final score was Computer:{} Player:{} Ties:{}".format(computer_score,player_score,num_of_ties))
    elif computer_score > player_score:
        print ("The computer won! The final score was Computer:{} Player:{} Ties:{}".format(computer_score,player_score,num_of_ties))
    elif computer_score == player_score:
        print ("It was a tie! Both player and computer had {} wins".format(player_score))
        
        



main()

    
    
        
    
    
    
    
        
        
        
    