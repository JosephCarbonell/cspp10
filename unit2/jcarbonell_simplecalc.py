operation = input("Enter your equation:")
length_of_term_1 = input("What was the length of the first term in your equation?")
length_of_term_2 = input("What was the length of the second term in your equation?")
last_digit_num_1 = int(length_of_term_1)
start_of_num_2 = last_digit_num_1 + 1
operator = operation[last_digit_num_1]
num_1 = int(operation[0:last_digit_num_1])
num_2 = int(operation[start_of_num_2:])
total = 0
if operator == "+":
    total = num_1 + num_2
elif operator == "-":
    total = num_1 - num_2
elif operator == "*":
    total = num_1 * num_2
elif operator == "/":
    total = num_1 / num_2
elif operator == "%":
    total = num_1 % num_2
else:
    print ("Your input is invalid")

print("The result is {}." .format(total))
