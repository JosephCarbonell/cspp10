import random
word_bank = ["cat","rock","dragon", "Afghanistan", "school", "fourteen", "nuts", "Facebook", "chicken","car","Tran","floor","butterfly","earth","computer","phone","dog","blue","red"]

def main():
    hangman_game()
    
def pick_word(word_bank):
    num_of_words = len(word_bank)
    index_of_word = random.randint(0,num_of_words - 1)
    return (word_bank[index_of_word])
    
def print_blanks(word_as_list):
    blank = "_"
    num_of_items = 0
    for item in word_as_list:
        num_of_items = num_of_items + 1
    return (blank * num_of_items)
        
    
def pick_a_letter():
    chosen_letter = input("Guess a letter to see if it is part of the word: ")
    return chosen_letter

def convert_str_to_list(word):
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
    for item in indexes_of_letter:
        num = item
        word_as_blanks[num] = chosen_letter
    return word_as_blanks
            
def hangman_game():
    print ("In this game your goal will be to fill in the blanks to reveal the word. You will have 8 chances to guess a letter, and for each correct letter, the corresponding blanks will be filled in.")
    word = pick_word(word_bank)
    word_as_list = convert_str_to_list(word)
    word_as_blanks = print_blanks(word_as_list)
    print ("Fill in the blanks: " + word_as_blanks)
    chosen_letter = pick_a_letter()
    indexes_of_letter = check_for_letter(word_as_list,chosen_letter)
    edited_word = edit_word_with_blanks(word_as_blanks,chosen_letter,indexes_of_letter)
    print (str(edited_word))
main()
