name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")

make = input("Enter the car's make: ")
model = input("Enter the car's model: ")
registration = input("Enter the car's registration: ")
year = int(input("Enter the year of original purchase: "))
mot = input("Does the car have a valid MOT certificate? (yes/no): ")
engine_size = float(input("Enter the engine size (e.g., 1.4): "))
mileage = int(input("Enter the current mileage: "))

current_year = 2025
age = current_year - year
base_price = 10000
price = base_price - (age * 500) - (mileage * 0.05)
if mot == "yes" or mot == "Yes":
    pass
else:
    price -= 500
if engine_size < 1.0:
    price -= 300
elif engine_size > 2.0:
    price += 200

if price < 500:
    price = 500

print("Your Name:", name)
print("Phone:", phone)
print("Email:", email)
print("Car:", make, model, registration)
print("Year:", year)
print("MOT valid:", mot)
print("Engine size:", engine_size)
print("Mileage:", mileage)
print("Estimated offer price: £" + str(round(price, 2)))