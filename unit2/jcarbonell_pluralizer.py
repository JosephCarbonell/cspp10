noun = input("Enter a noun to pluralize:")
num = input("How many of the noun are there?")
num_int = int(num)
x = 0
a = noun[-2:]
if a == "fe":
    x = 1
elif a == "ay" or a == "oy" or a == "ey" or a == "uy":
    x = 5
elif noun[-1] == "y":
    x = 2
elif a == "ch" or a == "sh":
    x = 3
elif a == "us":
    x = 4
else: 
    x = 6

b = ""    
y = ""    
if x == 1:
    y = noun[:-2]
    b = "ves"
elif x == 2:
    y = noun[:-1]
    b = "ies"
elif x == 3:
    y = noun
    b = "es"
elif x == 4:
    y = noun[:-2]
    b = "i"
elif x == 5:
    y = noun
    b = "s"
else:
    y = y
    b = "s"

final = y + b
print ("There are {} {}".format(num,final))



    
    
    




    
    

    
