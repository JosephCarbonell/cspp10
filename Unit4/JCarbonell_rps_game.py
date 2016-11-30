import JCarbonell_rps_functions


player1_score = 0
player2_score =  0
num_of_ties = 0
def main():
    rps_game()

def rps_game():
    print("Welcome to Rock,Paper,Scissors!")
    print("-------------------------------")
    global player1_score
    global player2_score
    global num_of_ties
    num_of_rounds = JCarbonell_rps_functions.get_rounds()
    print ("Please note that this is a Player vs Player game, so your choice will not be displayed, but will be registered.")
    for x in range(num_of_rounds):
        if player1_score > num_of_rounds / 2:
            print ("Player 1 wins")
            break
        elif player2_score > num_of_rounds / 2:
            print("Player 2 wins")
            break
        p1_move = JCarbonell_rps_functions.get_p1_move()
        p2_move = JCarbonell_rps_functions.get_p2_move()
        print ("It is round {}".format(x + 1))
        print ("Player 1 entered {}.".format(p1_move))
        print ("Player 2 entered {}.".format(p2_move))
        round_winner = (JCarbonell_rps_functions.get_round_winner(p1_move,p2_move))
        print ("{}".format(round_winner))
        print (JCarbonell_rps_functions.print_score())
        print("-------------------------------")
    if player1_score > player2_score:
        print ("The player won! The final score was Player 1: {} Player 2: {} Ties: {}".format(player1_score,player2_score,num_of_ties))
    elif player2_score > player1_score:
        print ("The computer won! The final score was Player 1: {} Player 2: {} Ties: {}".format(player1_score,player2_score,num_of_ties))
    elif player2_score == player1_score:
        print ("It was a tie! Both Player 1 and Player 2 had {} wins".format(player1_score))
   

main()