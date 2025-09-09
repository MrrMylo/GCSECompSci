# Exaple of a selection statement
wage = (int(input("Enter Wage: "))) # <--- This is an integer assignment

if wage > 10000 and wage < 30000: #<--- This is a complex condition
    tax = wage * 0.25 #<--- True Path
elif wage >= 30000:
    tax = wage * 0.40 #<--- False Path

takehome = wage - tax
print("Wage after tax: £" + str(takehome))