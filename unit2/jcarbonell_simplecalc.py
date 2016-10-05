operation = input("Enter your equation:")
length_of_term_1 = input("What was the length of the first term in your equation?")
length_of_term_2 = input("What was the length of the second term in your equation?")
n = int(length_of_term_1)
m = n + 1
x = operation[n]
a = int(operation[0:n])
b = int(operation[m:])
y = 0
if x == "+":
    y = a + b
elif x == "-":
    y = a - b
elif x == "*":
    y = a * b
elif x == "/":
    y = a / b
elif x == "%":
    y = a % b
else:
    print ("Your input is invalid")

print("The result is {}." .format(y))
