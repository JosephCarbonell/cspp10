int_start = (int(input("Enter the first number in the sequence: ")))
int_end = (int(input("Enter the last number in the sequence: ")))


for x in range(int_start, int_end + 1):
    if "3" in str(x) and "5" in str(x) or x % 3 == 0 and x % 5 == 0:
        print ("FizzBuzz", end = " ")
    elif "5" in str(x):
        print ("Buzz", end = " ")
    elif "3" in str(x):
        print ("Fizz", end = " ")
    else:
        if x % 3 == 0:
            print ("Fizz", end = " ")
        elif x % 5 == 0:
            print ("Buzz", end = " ")
        else:
                print (x, end = " ")
    

            
            