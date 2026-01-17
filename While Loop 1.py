borrow = "Y"
count = 0 

while borrow == "Y" or borrow == "y": 
    borrow = input("Do you want to borrow a book? (Y/N): ")

    while (borrow != "Y" and borrow != "y") and (borrow != "N" and borrow != "n"):
        print("Invalid input. Please enter Y or N.")
        borrow = input("Do you want to borrow a book? (Y/N): ")
    if borrow == "Y" or borrow == "y":
        count += 1
    
print("You have borrowed " + str(count) + " books.")