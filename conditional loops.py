sweets = "Y" # Sets the sweets variable to "Y"
num = 0 # Sets the num variable to 0

while sweets == "Y" or sweets == "y": # conditional loop of if sweets are "Y" or "y"
    sweets = input("Enter Sweet Y or N: ")
    if sweets == "Y" or sweets == "y": # Fixed loop of if sweets are "Y" or "y"
        num = num + 1 # if sweets is "Y" or "y" it adds one to the count and restarts the conditional loop
        
print("You bought " + str(num) + " sweets!") # prints output
