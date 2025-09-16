drink_price = 1.25  

print("Welcome to the Python Snack Shop!")  
name = input("What is your name? ")  
welcome_message = "Hello " + name + "! Thanks for shopping with us."
print(welcome_message)

print("Each drink costs £" + str(drink_price))
print("\n--- Integer Operations ---")  
drinks = int(input("How many cans of drink do you want? ")) 
print("\n--- String Concatenation ---") 
print("You chose " + str(drinks) + " drinks.") 
print("Total drink cost = " + str(round(drinks * drink_price, 2)))  
if drinks > 2:  
    print("You're going to be really hydrated!") 
chocolates = int(input("How many chocolates do you want? "))
print("You chose " + str(chocolates) + " chocolates.")   
if chocolates > 5:  
    print("Wow, that's a lot of chocolates!")  
 
print("If each chocolate costs £2, total = " + str(chocolates * 2)) 

print("\n--- Checking Your Order ---") 

total_bill = (chocolates * 2) + (drinks * drink_price) 
total_bill = round(total_bill, 2)  

if total_bill > 20:  
    print("Big spender alert!") 
else:  
    print("That’s a reasonable snack choice.")

print("Your total bill is: £" + str(total_bill)) 