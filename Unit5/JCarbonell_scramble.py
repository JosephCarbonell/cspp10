from random import shuffle

word_to_scramble = input("Enter the word you want to scramble: ")

def scramble_word(word):
    if len(word) > 3:
        first_and_last = []
        first_and_last.append(word[0])
        first_and_last.append(word[-1])
        edited_word = word[1:-1]
        edited_word = list(edited_word)
        shuffle(edited_word)
        edited_word.insert(0,first_and_last[0])
        edited_word.append(first_and_last[-1])
        print(edited_word)
    
    
scramble_word(word_to_scramble)