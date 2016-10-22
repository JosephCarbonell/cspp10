import random
ending_number = input("Enter the number for the end of the range:")
print ("The number is between 1 and {}.".format(ending_number))
answer = random.randint(1, int(ending_number))
number_of_guess = 0
guess = -1
while guess != answer:
    number_of_guess = number_of_guess + 1
    guess = int(input("Guess what the random number is:"))
    if guess < answer:
        print("Too high. Try again.")
    elif guess > answer:
        print("Too low. Try again.")
print ("You were correct! It took you {} guesses.".format(number_of_guess))