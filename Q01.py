# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
decimalCode = 60
num = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
num = int(input("Input Number: "))

# Check that the inputted number is between 5 and 30 (inclusive)
if num >= 5 and num <= 30:
    decimalCode = num + decimalCode
    # Output the character for the decimal code
    print(str(num) + " is equal to " + chr(decimalCode))
else:
    print("Invalid Input - Number must be between 5 and 30")
