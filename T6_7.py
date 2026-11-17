#create a coundown from 10

import time, random

# read the colours
file = open("colours.txt" , "r")
contents = file.read()
file.close()

colours = [colour.strip().upper() for colour in contents.split("|")]

#choose the correct sabotage_colour
sabotage_colour = random.choice(colours)

print("Choose a colour to sabotage launch")
print("Your options are:", colours)

choice = input("Enter your colour:").upper().strip()

# countdown
countdown = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

for number in countdown:

    time.sleep(1)
     
    if number == 5:
        print( "T MINUS 5 SECONDS")

        if choice == sabotage_colour.upper():
            print("SABOTAGE SUCCESSFUL")
            break
        else:
            print("WRONG COLOUR")
        
    else: 
        print(number)
    
    if number == 0:
        print("LIFT OFF")
    



