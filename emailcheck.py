dot_location = False
email = input("Enter your email: ")

while True:
    at_index = email.find("@")
    at_count = email.count("@")

    if " " in email:
        print("Your Password Contains a Space. Please try again")
        email = input("Enter your email: ")
        continue

    if email.startswith("@") or email.endswith("@"):
        print("Your Password cannot start or end with an @. Please try again")
        
    elif at_count != 1:
        print("Your password must only contain one @. Please only use one and try again")
        
    elif at_index < 5:
        print("Your password must have at least 5 characters before the @. Please try again")
        
    else:
        after_at = email.split("@", 1)[1]
        
        if after_at.count(".") != 1:
            print("Your password does not contain exactly one dot after the @. Please try again.")
            
        elif after_at.startswith(".") or after_at.endswith("."):
            print("Your password has the dot in the wrong place. Please try again.")
            
        else:
            break

    email = input("Enter your email: ")
        
print("Email Accepted")

