answer = "Y"
workouts = 0

while answer == "Y" or answer == "y":
    answer = input("Did you complete a workout today? (Y or N)")
    
    while (answer != "Y" and answer != "y") and (answer != "N" and answer != "n"):
        print("Invalid input. Please enter Y or N.")
        answer = input("Did you complete a workout today? (Y or N)")
    if answer == "Y" or answer == "y":
        workouts = workouts + 1

print("You completed " + str(workouts) + " Workouts this week!")
 