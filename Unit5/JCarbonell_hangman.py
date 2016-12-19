import random
word_bank = ["cat","rock","dragon", "school", "fourteen", "nuts", "chicken","car","floor","butterfly","earth","computer","phone","dog","blue","red"]

def main():
    hangman_game()
    
def pick_word(word_bank):
    num_of_words = len(word_bank)
    index_of_word = random.randint(0,num_of_words - 1)
    return (word_bank[index_of_word])
    
def print_blanks(word_as_list):
    blank = "_ "
    num_of_items = 0
    for item in word_as_list:
        num_of_items = num_of_items + 1
    return (blank * num_of_items)
        
    
def pick_a_letter():
    chosen_letter = input("Guess a letter to see if it is part of the word: ")
    return chosen_letter

def convert_list_to_str(word):
    word_as_list = []
    for item in range(len(word)):
        word_as_list.append(item)
    return word_as_list
    
def check_for_letter(word_as_list,chosen_letter):
    indexes_of_letter = []
    for number in range(len(word_as_list)):
        if word_as_list[number] == chosen_letter:
            indexes_of_letter.append(number)
    return indexes_of_letter
             
def edit_word_with_blanks(word_as_blanks,chosen_letter,indexes_of_letter):
    word_as_blanks = list(word_as_blanks)
    for item in word_as_blanks:
        if item == " ":
            word_as_blanks.remove(item)
    for item in indexes_of_letter:
        num = item
        word_as_blanks[num] = chosen_letter
    final_string = ""
    for item in word_as_blanks:
        final_string = final_string + item + " "
    return final_string

        
def hangman_game():
    print ("In this game your goal will be to fill in the blanks to reveal the word. You will have 8 chances to guess a letter, and for each correct letter, the corresponding blanks will be filled in.")
    print ("Make sure you enter lower case letters, as uppercase letters will not fit into the word accurately.")
    word = pick_word(word_bank)
    word_as_list = list(word)
    word_as_blanks = print_blanks(word_as_list)
    word_as_list_secondary = []
    for index in range(len(word)):
        word_as_list_secondary.append(word[index])
        word_as_list_secondary.append(" ")
    chances_left = 8
    win_or_lose = 0
    while chances_left > 0:
        print ("You have {} chances left!".format(chances_left))
        print ("Fill in the blanks: " + word_as_blanks)
        chosen_letter = pick_a_letter()
        indexes_of_letter = check_for_letter(word_as_list,chosen_letter)
        edited_blanks = edit_word_with_blanks(word_as_blanks,chosen_letter,indexes_of_letter)
        word_as_blanks = edited_blanks
        edited_blanks_as_list = list(edited_blanks)
        for item in edited_blanks_as_list:
            if item == " ":
                edited_blanks_as_list.remove(item)
        if chosen_letter not in word:
            chances_left = chances_left - 1
        if word_as_list == edited_blanks_as_list:
            win_or_lose = "win"
            break
        print (edited_blanks)
    if win_or_lose == "win":
        print ("You won!")
    else:
        print ("Your word was {}".format(word))
        print ("You lose... Try again!")
        
main()
