import math
import random

def encrypt(key,message):
    rows = math.ceil(len(message) / key)
    rows = int(rows)
    cols = key
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pointer = 0
    encrypted = ''
    table = [[''] * cols for i in range(rows)]
    for row in range(len(table)):
        for column in range(len(table[0])):
            if pointer <= len(message):
                table[row][column] = message[pointer]
                pointer = pointer + 1
    for column in range(len(table[0])):
        for row in range(len(table)):
            encrypted = encrypted + table[column][row]
    
encrypt(3,"Hello there.")
        
