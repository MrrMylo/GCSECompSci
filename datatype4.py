print("Welcometo the dice scorer")
print("Please roll 3 dice")
number1 = int(input("Enter the first dice number: "))
number2 = int(input("Enter the second dice number: "))
number3 = int(input("Enter the third dice number: "))

if number1 == number2 == number3:
    score = number1 + number2 + number3 
elif number1 == number2:
    score = (number1 + number2) - number3
elif number1 == number3:
    score = (number1 + number3) - number2
elif number2 == number3:
    score = (number2 + number3) - number1
else:
        score = 0.5
print("Your score is: " + str(score))
