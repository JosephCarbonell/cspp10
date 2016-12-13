import random
word_bank = ["cat","rock","dragon", "Afghanistan", "school", "fourteen", "nuts", "Facebook", "chicken","car","Tran","floor","butterfly","earth","computer","phone","dog","blue","red"]

def main():
    hangman_game()
    
def pick_word(word_bank):
    num_of_words = len(word_bank)
    index_of_word = random.randint(0,num_of_words - 1)
    return (word_bank[index_of_word])
    
def print_blanks(word):
    len_word = len(word)
    blank = "_ "
    return (blank * len_word)
    
def hangman_game():
    print ("In this game your goal will be to fill in the blanks to reveal the word. You will have 8 chances to guess a letter, and for each correct letter, the corresponding blanks will be filled in.")
    word = pick_word(word_bank)
    print ("Fill in the blanks: " + print_blanks(word))
    
main()

