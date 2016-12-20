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


def hangman_graphics(incorrect_guesses):
    character_pieces = ["O","|","/","\\","/","\\"]
    character_pieces_used = [" "," "," "," "," "," "]
    for x in range(incorrect_guesses):
        character_pieces_used.remove(character_pieces_used[x])
        character_pieces_used.insert(x,character_pieces[x])
    print("_____")
    print("|/  |")
    print("|   {}".format(character_pieces_used[0]))
    print("|  {}{}{}".format(character_pieces_used[2],character_pieces_used[1],character_pieces_used[3]))
    print("|  {} {}".format(character_pieces_used[4],character_pieces_used[5]))
    print("|")
    print("+-----+")
    










        
def hangman_game():
    print ("In this game your goal will be to fill in the blanks to reveal the word. You will have 6 chances to guess a letter, and for each correct letter, the corresponding blanks will be filled in.")
    print ("Make sure you enter lower case letters, as uppercase letters will not fit into the word accurately.")
    print ("Also, make sure you don't put a letter twice!")
    word = pick_word(word_bank)
    word_as_list = list(word)
    word_as_blanks = print_blanks(word_as_list)
    word_as_list_secondary = []
    for index in range(len(word)):
        word_as_list_secondary.append(word[index])
        word_as_list_secondary.append(" ")
    incorrect_guesses = 0
    win_or_lose = 0
    unused_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    used_letters = []
    while incorrect_guesses < 6:
        print ("You have {} incorrect guesses".format(incorrect_guesses))
        print ("Your unused letters are: {}".format(str(unused_letters)))
        print ("Your used letters are {}".format(str(used_letters)))
        print ("Fill in the blanks: " + word_as_blanks)
        chosen_letter = pick_a_letter()
        if chosen_letter in unused_letters:
            unused_letters.remove(chosen_letter)
            used_letters.append(chosen_letter)
        indexes_of_letter = check_for_letter(word_as_list,chosen_letter)
        edited_blanks = edit_word_with_blanks(word_as_blanks,chosen_letter,indexes_of_letter)
        word_as_blanks = edited_blanks
        edited_blanks_as_list = list(edited_blanks)
        for item in edited_blanks_as_list:
            if item == " ":
                edited_blanks_as_list.remove(item)
        if chosen_letter not in word:
            incorrect_guesses = incorrect_guesses + 1
        if word_as_list == edited_blanks_as_list:
            win_or_lose = "win"
            break
        print (edited_blanks)
        hangman_graphics(incorrect_guesses)
    if win_or_lose == "win":
        print ("You won!")
    else:
        print ("Your word was {}".format(word))
        print ("You lose... Try again!")
        
main()

        
    
    
    
    