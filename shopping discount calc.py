bill = float(input("Enter your total shopping bill: "))

while bill < 5 or bill > 500:
    print("Error: Please enter a value between £5 and £500.")
    bill = float(input("Enter your total shopping bill: "))

if bill >= 200:
    discount = 0.20
elif bill >= 100:
    discount = 0.10
else:
    discount = 0.0

final_price = bill * (1 - discount)

loyalty = input("Do you have a loyalty card? (yes/no): ")
if loyalty == "yes" or loyalty == "Yes":
    final_price *= 0.95  # Extra 5% discount

print("Original bill: £" + str(round(bill, 2)))
print("Final amount to pay: £" + str(round(final_price, 2)))
