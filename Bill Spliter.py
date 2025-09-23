bill = float(input("Enter the total bill amount: £"))
num_people = int(input("Enter the number of people to split the bill: "))
if num_people <= 0:
    print("Number of people must be greater than zero.")
else:
    amount_per_person = bill / num_people
    print(f"Each person should pay: £{amount_per_person:.2f}")

tip = input("Would you like to add a tip? (yes/no): ").strip().lower()
if tip == "yes":
    tip_percentage = float(input("Enter % of tip to add (e.g., 10 for 10%): "))
    tip_amount = (tip_percentage / 100) * bill
    total_bill = bill + tip_amount
    amount_per_person = total_bill / num_people
    print(f"With a {tip_percentage}% tip, each person should pay: £{amount_per_person:.2f}")    