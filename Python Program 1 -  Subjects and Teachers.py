print ("Welcome to 4th Form!")
print ("Let's make our first proper Python program.")
print()

num_subjects = int(input("How many subjects are you taking? "))

for i in range (num_subjects):
    subject = input("Enter subject: ")
    teacher = input("Enter teacher: ")
    print(subject + ", " + teacher)