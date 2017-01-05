import random


def main():
    final_game()

def roll_two_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    total = die_1 + die_2
    print ("You rolled {}".format(total))
    return total
    
def check_roll(dice_total):
    if dice_total < 7:
        return ("Under 7")
    elif dice_total == 7:
        return ("On 7")
    elif dice_total > 7:
        return ("Over 7")
    
def get_player_bet():
    player_bet = input("Would you like to bet on \n 1. Under 7 \n 2. On 7 \n 3. Over 7 \n Please enter the number of your choice. ")
    if player_bet == "1":
        return ("Under 7")
    elif player_bet == "2":
        return ("On 7")
    elif player_bet == "3":
        return ("Over 7")
    else:
        print ("That input was invalid. Try again.")
        
def get_player_bet_money(bank):
    while True:
        player_bet = int(input("How much money would you like to bet? "))
        if player_bet > bank:
            print ("That bet is invalid")
        else:
            break
    return player_bet
    
def final_game():
    bank = 100
    while True:
        if bank <= 0:
            print ("You lose!")
        else:
            print ("You have {} dollars.".format(bank))
            range_choice = get_player_bet()
            player_bet = get_player_bet_money(bank)
            dice_total = roll_two_dice()
            checked_roll = check_roll(dice_total)
            if checked_roll == range_choice and range_choice == "Over 7" or range_choice == "Under 7":
                print ("You won the roll")
                bank = bank + player_bet
            elif checked_roll == range_choice and range_choice == "On 7":
                bank = bank + (player_bet * 4)
            else:
                print ("You lost the roll")
                bank = bank - player_bet

       
main()