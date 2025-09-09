# Science Department Average Calculator
bio = int(input("Enter the Biology Result: "))
chem = int(input("Enter the Chemistry Result: "))
physics = int(input("Enter the Physics Result: "))

average = round((bio + chem + physics) / 3, 2)

resulttype = (input("Is this a GCSE or Letter System result? (Enter G for GCSE or L for Letter System): ")).upper()

if resulttype == "G":
    nine_Bound = 75
    eight_Bound = 68
    seven_Bound = 60
    six_Bound = 55
    five_Bound = 50
    four_Bound = 40
    fail_Bound = 0

    if average >= nine_Bound:
        grade = "9"
    elif average >= eight_Bound:
        grade = "8"
    elif average >= seven_Bound:
        grade = "7"
    elif average >= six_Bound:
        grade = "6"
    elif average >= five_Bound:
        grade = "5"
    elif average >= four_Bound:
        grade = "4"
    elif average >= fail_Bound:
        grade = "Fail"

elif resulttype == "L":
    AStar_Bound = 75
    A_Bound = 68
    B_Bound = 60
    C_Bound = 55
    D_Bound = 50
    E_Bound = 30
    F_Bound = 0

    if average >= AStar_Bound:
        grade = "A*"
    elif average >= A_Bound:
        grade = "A"
    elif average >= B_Bound:
        grade = "B"
    elif average >= C_Bound:
        grade = "C"
    elif average >= D_Bound:
        grade = "D"
    elif average >= E_Bound:
        grade = "E"
    elif average >= F_Bound:
        grade = "F"

print("Average: " + str(average) + "%") 
print("Grade: " + grade)
