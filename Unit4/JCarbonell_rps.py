import random 
import getpass
player1_score = 0
player2_score = 0
num_of_ties = 0
def main():
    rps_game()
    

def get_p1_move():
    player1_choice = getpass.getpass("Player 1: Enter Rock, Paper, Scissors, Lizard, or Spock: ")
    return player1_choice

def get_p2_move():
    player2_choice = getpass.getpass("Player 2: Enter Rock, Paper, Scissors, Lizard, or Spock: ")
    return player2_choice

    
def get_rounds():
    num_of_rounds = int(input("Enter the number of rounds you wish to play: "))
    return num_of_rounds
    
    
def get_round_winner(player1_choice,player2_choice):
    global player1_score
    global player2_score
    global num_of_ties
    
    if player1_choice == "Rock":
        if player2_choice == "Rock":
            num_of_ties = num_of_ties + 1
            return ("It was a tie")
        elif player2_choice == "Paper" or player2_choice == "Spock":
            player2_score = player2_score + 1
            return ("The winner is Player 2")
        elif player2_choice == "Scissors" or player2_choice == "Lizard":
            player1_score = player1_score + 1
            return ("The winner is Player 1")
    
    elif player1_choice == "Paper":
        if player2_choice == "Rock" or player2_choice == "Spock":
            player1_score = player1_score + 1
            return("The winner is Player 1")
        elif player2_choice == "Paper":
            num_of_ties = num_of_ties + 1
            return("It was a tie")
        elif player2_choice == "Scissors" or player2_choice == "Lizard":
            player2_score = player2_score + 1
            return("The winner is Player 2")
    
    elif player1_choice == "Scissors":
        if player2_choice == "Rock" or player2_choice == "Spock":
            player2_score = player2_score + 1
            return("The winner is Player 2")
        elif player2_choice == "Paper" or player2_choice == "Lizard":
            player1_score = player1_score + 1
            return("The winner is Player 1")
        else:
            return("It was a tie")
            num_of_ties = num_of_ties + 1
    
    elif player1_choice == "Lizard":
        if player2_choice == "Rock" or player2_choice == "Scissors":
            player2_score = player2_score + 1
            return("The winner is Player 2")
        elif player2_choice == "Paper" or player2_choice == "Spock":
            player1_score = player1_score + 1
            return("The winner is Player 1")
        else:
            num_of_ties = num_of_ties + 1
            return("It was a tie")
    
    elif player1_choice == "Spock":
        if player2_choice == "Paper" or player2_choice == "Lizard":
            player2_score = player2_score + 1
            return("The winner is Player 2")
        elif player2_choice == "Rock" or player2_choice == "Scissors":
            player1_score = player1_score + 1
            return("The winner is Player 1")
        else:
            num_of_ties = num_of_ties + 1
            return("It was a tie")
    
    else:
        return("Try again, that option was invalid")
            
        

def print_score():
    global player1_score
    global player2_score
    global num_of_ties
    return("The score is Player 1: {} Player 2: {} and Ties: {}.".format(player1_score,player2_score,num_of_ties))

def rps_game():
    print("Welcome to Rock,Paper,Scissors!")
    global player1_score
    global player2_score
    global num_of_ties
    num_of_rounds = get_rounds()
    for x in range(num_of_rounds):
        if player1_score > num_of_rounds / 2:
            print ("Player 1 wins")
            break
        elif player2_score > num_of_rounds / 2:
            print("Player 2 wins")
            break
        p1_move = get_p1_move()
        p2_move = get_p2_move()
        print ("It is round {}".format(x + 1))
        print ("Player 1 entered {}.".format(p1_move))
        print ("Player 2 entered {}.".format(p2_move))
        round_winner = (get_round_winner(p1_move,p2_move))
        print ("{}".format(round_winner))
        print (print_score())
    if player1_score > player2_score:
        print ("The player won! The final score was Player 1: {} Player 2: {} Ties: {}".format(player1_score,player2_score,num_of_ties))
    elif player2_score > player1_score:
        print ("The computer won! The final score was Player 1: {} Player 2: {} Ties: {}".format(player1_score,player2_score,num_of_ties))
    elif player2_score == player1_score:
        print ("It was a tie! Both Player 1 and Player 2 had {} wins".format(player1_score))
        
        



main()

    
    
        
    
    
    
    
        
        
        
    