noun = input("Enter a noun to pluralize:")
num = input("How many of the noun are there?")
num_int = int(num)
type_ending = 0
last_letters = noun[-2:]
if last_letters == "fe":
    type_ending = 1
elif last_letters == "ay" or last_letters == "oy" or last_letters == "ey" or last_letters == "uy":
    type_ending = 5
elif noun[-1] == "y":
    type_ending = 2
elif last_letters == "ch" or last_letters == "sh":
    type_ending = 3
elif last_letters == "us":
    type_ending = 4
else: 
    type_ending = 6

ending_added = ""    
part_kept = ""    
if type_ending == 1:
    part_kept = noun[:-2]
    ending_added = "ves"
elif type_ending == 2:
    part_kept = noun[:-1]
    ending_added = "ies"
elif type_ending == 3:
    part_kept = noun
    ending_added = "es"
elif type_ending == 4:
    part_kept = noun[:-2]
    ending_added = "i"
elif type_ending == 5:
    part_kept = noun
    ending_added = "s"
else:
    part_kept = part_kept
    ending_added = "s"

final = part_kept + ending_added
print ("There are {} {}".format(num,final))



    
    
    




    
    

    
