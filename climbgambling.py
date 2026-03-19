import random

fell = False
stopped = False

print("Mountain Climb")
maxheight = int(input("How high is your mountain in feet:" ))
currentheight = 0

while fell == False and stopped == False and currentheight < maxheight:
    choice = input("Climb or Stop?: ").lower()
    
    if choice == "climb":
        chance = random.random()
        chance = round(chance, 2)
        
        if chance < 0.10:
            print("You slipped and fell!")
            fell = True
        
        else:
            currentheight = currentheight + 100
            print("You climbed 100 feet. Your new height is " + str(currentheight) + " feet.")
            
            
            if currentheight >= maxheight:
                print("You reached the summit!")
                
    elif choice == "stop":
        stopped = True
    
print("Final Height: " + str(currentheight))

if fell == True:
    ("You fell in the abyss, and died.")
elif stopped == True:
    print("You stopped " + str(maxheight - currentheight) + " feet from the summit.")
else:
    print("You made it to the summit alive!")