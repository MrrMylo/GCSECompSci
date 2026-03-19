wage = (int(input("Enter Wage: £ "))) 
tax = 0
if wage >= 12571 and wage <= 15397: 
    tax = wage * 0.19 
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage >= 15398 and wage <= 27491:
    tax = wage * 0.20 
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage >= 27492 and wage <= 43662: 
    tax = wage * 0.21 
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage >= 43663 and wage <= 75000: 
    tax = wage * 0.42 
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage >= 75001 and wage <= 125140: 
    tax = wage * 0.45 
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage >= 125141: 
    tax = wage * 0.48 
    takehome = wage - tax
    print("Wage after tax: £" + str(takehome))
elif wage < 12570:
    print("No tax to pay. Within personal allowance") 
