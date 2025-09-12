liters = float(input("How many liters of fuel would you like to purchase? "))
price_per_liter = 1.9
cost = liters * price_per_liter

# Discount Calculationsa
while liters <10 or liters > 75:
    print("Error: Please enter a value between 10 and 75 liters.")
    liters = float(input("How many liters of fuel would you like to purchase? "))
if liters >= 50:
    discount = 0.9
    finalprice = round(cost * discount,2)
    print("Discount Applied: 10%")
    print("£" + str(finalprice))
elif liters >= 30:
    discount = 0.95
    finalprice = round(cost * discount,2)
    print("Discount Applied: 5%")
    print("£" + str(finalprice))
elif liters >=11:
    discount = 0
    finalprice = cost
    print("No discount applied.")
    print("Total cost: £"+ str(finalprice))
