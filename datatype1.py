firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
telephoneNumber = input("Enter your telephone number: ")
membershipStatus = input("Enter your membership status (Yes/No): ")
if membershipStatus == "yes" or membershipStatus == "Yes":
    membershipStatus = True
elif membershipStatus == "no" or membershipStatus == "No":
    membershipStatus = False

print("First Name: " + str(firstname))
print("Surname: " + str(surname))
print("Age: " + str(age))
print("Telephone Number: " + str(telephoneNumber))
print("Membership Status: " + str(membershipStatus))
print()
