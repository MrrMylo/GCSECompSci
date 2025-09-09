wage = (int(input("Enter Wage: ")))

if wage > 10000 and wage < 30000:
    tax = wage * 0.25
elif wage >= 30000:
    tax = wage * 0.40

takehome = wage - tax
print("Wage after tax: £" + str(takehome))