import random

count = int(input("How many random floats do you want?: "))

for i in range(count):
    number = random.random()
    number = round(number, 2)
    print(number)