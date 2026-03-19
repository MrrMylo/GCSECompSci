m4_rented = input("How many days was the White BMW M4 Competition rented for? ")
while not m4_rented.isdigit():
    print("Error: Please enter a valid number.")
    m4_rented = input("How many days was the White BMW M4 Competition rented for? ")
m4_rented = int(m4_rented)

rs3_rented = input("How many days was the Red Audi RS3 rented for? ")
while not rs3_rented.isdigit():
    print("Error: Please enter a valid number.")
    rs3_rented = input("How many days was the Red Audi RS3 rented for? ")
rs3_rented = int(rs3_rented)

p11_rented = input("How many days was the Yellow Porsche 911 rented for? ")
while not p11_rented.isdigit():
    print("Error: Please enter a valid number.")
    p11_rented = input("How many days was the Yellow Porsche 911 rented for? ")
p11_rented = int(p11_rented)

gtr_rented = input("How many days was the Silver Nissan GTR rented for? ")
while not gtr_rented.isdigit():
    print("Error: Please enter a valid number.")
    gtr_rented = input("How many days was the Silver Nissan GTR rented for? ")
gtr_rented = int(gtr_rented)

ix_rented = input("How many days was the Black BMW iX rented for? ")
while not ix_rented.isdigit():
    print("Error: Please enter a valid number.")
    ix_rented = input("How many days was the Black BMW iX rented for? ")
ix_rented = int(ix_rented)

f500_rented = input("How many days was the Purple Fiat 500 rented for? ")
while not f500_rented.isdigit():
    print("Error: Please enter a valid number.")
    f500_rented = input("How many days was the Purple Fiat 500 rented for? ")
f500_rented = int(f500_rented)

vwg_rented = input("How many days was the White Volkswagon Golf R rented for? ")
while not vwg_rented.isdigit():
    print("Error: Please enter a valid number.")
    vwg_rented = input("How many days was the White Volkswagon Golf R rented for? ")
vwg_rented = int(vwg_rented)
for i in range(4):
    print()

days_rented = [m4_rented, rs3_rented, p11_rented, gtr_rented, ix_rented, f500_rented, vwg_rented]
car = ["White BMW M4 Competition", "Red Audi RS3", "Yellow Porsche 911", "Silver Nissan GTR", "Black BMW iX", "Purple Fiat 500", "White Volkswagon Golf R"]

for i in range(len(days_rented)):
    print(str(car[i]) + " was rented for " + str(days_rented[i]) + " days.")
