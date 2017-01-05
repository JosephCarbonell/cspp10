from random import shuffle



def scramble_word(word):
    if len(word) > 3:
        len_of_word = len(word)
        first_and_last = []
        first_and_last.append(word[0])
        first_and_last.append(word[-1])
        edited_word = word[1:-1]
        edited_word = list(edited_word)
        print (edited_word)
        shuffle(edited_word)
        print (edited_word)
    
    
scramble_word("hello")