import random
player1_bank = 100
player2_bank = 100


def main():
    craps_game()

def get_bet(player):
    bet = 0
    while True == True:
        bet = float(input("How much would you like to bet? "))
        if player == 1 and bet > player1_bank:
            print("You can not bet more than you have in your bank.")
        elif player == 2 and bet > player2_bank:
            print("You can not bet more than you have in your bank.")
        elif bet < 0 or bet != int(bet):
            print("That bet type is invalid, make sure you use a positive integer as your bet.")
        else:
            print("That is a valid bet.")
            return bet

def roll_2_dice():
    num_1 = random.randint(1,6)
    num_2 = random.randint(1,6)
    print ("The dice are thrown {} and {}, {} total.".format(num_1,num_2,num_1+num_2))
    return num_1 + num_2

def player_swap(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1
        
def check_first_roll(first_roll):
    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        print ("You lost the roll.")
        return ("loss")
    elif first_roll == 7 or first_roll == 11:
        print ("You won the roll.")
        return ("win")
    else:
        print ("Your point number is {}.".format(first_roll))
        return (first_roll)

def check_point_number(point_number):
    while True == True:
        roll = roll_2_dice()
        if roll == point_number:
            print("You won the roll.")
            return ("win")
        elif roll == 7:
            print("You lost the roll")
            return ("loss")
        else:
            print("You didn't win or lose. Reroll!")
            x = input("Press enter to roll again: ")
            if x == "":
                y = 2
            else:
                break
        
    
def play_round(player):
    print("Player {} is the shooter!".format(player))
    first_roll = roll_2_dice()
    result = check_first_roll(first_roll)
    if result == ("loss"):
        return ("loss")
    elif result == ("win"):
        return ("win")
    else:
        point_number = result
        result = check_point_number(point_number)
        return result
        
def change_value(result):
    global bet
    global bet2
    global player1_bank
    global player2_bank
    if result == "win":
        player1_bank = player1_bank + bet1 
        player2_bank = player2_bank + bet2
    if result == "loss":
        player1_bank = player1_bank - bet1
        player2_bank = player2_bank - bet2

        
            
        
    

def craps_game():
    global player1_bank
    global player2_bank
    global bet1
    global bet2
    print("Player 1 has {} dollars and Player 2 has {} dollars.".format(player1_bank,player2_bank))
    player = 1
    while player1_bank > 0 and player2_bank > 0:
        print("Player {} is the shooter.".format(player))
        print("It is Player 1's turn to bet")
        bet1 = get_bet(player)
        player = player_swap(player)
        print("It is Player 2's turn to bet")
        bet2 = get_bet(player)
        player = player_swap(player)
        result = play_round(player)
        change_value(result)
        print ("Player 1 has {} dollars and Player 2 has {} dollars.".format(player1_bank,player2_bank))

    if player1_bank == 0 and player2_bank == 0:
        print("Both players went broke!")
    elif player1_bank == 0:
        print ("Player 2 won!")
    elif player2_bank == 0:
        print ("Player 1 won!") 
        
            
        
main()    
        
        
        
    
    
    
    