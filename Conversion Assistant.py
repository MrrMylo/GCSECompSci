print("Welcome to the Conversion Assistant")
print()

# Celsius to Fahrenheit
choice = input("Do you want to convert Celsius to Fahrenheit and Kelvin? (yes/no): ")
if choice == "yes":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = round((celsius * 9/5) + 32)
    kelvin = round(celsius + 273)
    print("Temperature in Fahrenheit: " + str(fahrenheit))
    print("Temperature in Kelvin: " + str(kelvin))

# KG to LB
choice = input("Do you want to convert Kilograms to Pounds? (yes/no): ")
if choice == "yes":
    kg = float(input("Enter weight in Kilograms: "))
    pounds = round(kg * 2.20462)
    print("Weight in Pounds:" + str(pounds))

# Grams to Ounces
choice = input("Do you want to convert Grams to Ounces? (yes/no): ")
if choice == "yes":
    grams = float(input("Enter weight in Grams: "))
    ounces = round(grams / 28.3495)
    print("Weight in Ounces:" + str(ounces))
    print()
    print("Thank you for using the Conversion Assistant!")
else:
    print("Thank you for using the Conversion Assistant!")
    
