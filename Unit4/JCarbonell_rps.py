import random 
import getpass
def main():
    rps_game()
    
def rps_game():
    print ("Welcome to Rock Paper Scissor!")
    global computer_score
    global player_score
    computer_score = 0
    player_score = 0
    num_of_rounds = int(input("How many rounds would you like to play?"))
    for x in range(num_of_rounds):
        print("It is round {}.".format(x + 1))
        print("The current score is Computer:{} to Player:{}".format(computer_score, player_score))
        player_choice = input("Enter Rock,Paper,or Scissors: ")
        computer_choice = random.randint(1,3)
        #1 is rock, 2 is paper, 3 is scissors
        if computer_choice == 1:
            print("Computer chose Rock")
        elif computer_choice == 2:
            print("Computer chose Paper")
        else:
            print("Computer chose Scissors")
            
        if player_choice == "Rock":
            if computer_choice == 1:
                print("It was a tie")
            elif computer_choice == 2:
                print("The computer won")
                computer_score = computer_score + 1
            else:
                print("The player won")
                player_score = player_score + 1
        elif player_choice == "Paper":
            if computer_choice == 1:
                print("The player won")
                player_score = player_score + 1
            elif computer_choice == 2:
                print("It was a tie")
            else:
                print("The computer won")
                computer_score = computer_score + 1
        else:
            if computer_choice == 1:
                print("The computer won")
                computer_score = computer_score + 1
            elif computer_choice == 2:
                print("The player won")
                player_score = player_score + 1
            else:
                print("It was a tie")
            
        if player_score > num_of_rounds / 2:
            print("The player won! The score was Player:{} to Computer:{}".format(player_score, computer_score))
            break
        elif computer_score > num_of_rounds / 2:
            print("The computer won! The score was Player:{} to Computer:{}".format(player_score, computer_score))
            break
            

main()       
    