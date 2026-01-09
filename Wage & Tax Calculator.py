# Exaple of a selection statement
wage = (int(input("Enter Wage: "))) # <--- This is an integer assignment
tax = 0
if wage >= 10000 and wage <= 30000: #<--- This is a complex condition
    tax = wage * 0.25 #<--- True Path
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage >= 30000:
    tax = wage * 0.48 #<--- False Path
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage < 12570:
    print("No tax to pay") #<--- False Path
