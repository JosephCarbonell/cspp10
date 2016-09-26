seconds = input("Enter a number of seconds: ")
seconds = int(seconds)
x = seconds % 60
y = seconds - x
minutes = y / 60
a = minutes % 60
b = minutes - a 
hours = b / 60
seconds = str(seconds)
seconds_string = str(x)
minutes_string = str(a)
hours_string = str(hours)
print (seconds + " seconds is " + hours_string + " hours, " + minutes_string + " minutes, and " + seconds_string + " seconds.")