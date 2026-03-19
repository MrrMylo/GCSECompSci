valid_email = False

while not valid_email:
    email = input("Enter your email address: ")
    
    # Check if email has spaces
    if " " in email:
        print("Error: Email cannot contain spaces")
    # Check if email starts or ends with @
    elif email.startswith("@") or email.endswith("@"):
        print("Error: Email cannot start or end with @")
    # Count how many @ symbols
    elif email.count("@") != 1:
        print("Error: Email must contain exactly one @")
    # Check if there is a . after the @
    elif "@" not in email or "." not in email.split("@")[1]:
        print("Error: Email must have at least one . after the @")
    else:
        print("Email accepted!")
        valid_email = True


# PASSWORD VALIDATION SECTION
valid_password = False

while not valid_password:
    password = input("Enter your password: ")
    
    # Check length
    if len(password) < 8:
        print("Error: Password must be at least 8 characters long")
    else:
        # Check for uppercase letter
        has_uppercase = False
        for character in password:
            if character.isupper():
                has_uppercase = True
        
        if not has_uppercase:
            print("Error: Password must contain at least one uppercase letter")
        else:
            # Check for lowercase letter
            has_lowercase = False
            for character in password:
                if character.islower():
                    has_lowercase = True
            
            if not has_lowercase:
                print("Error: Password must contain at least one lowercase letter")
            else:
                # Check for a number
                has_number = False
                for character in password:
                    if character.isdigit():
                        has_number = True
                
                if not has_number:
                    print("Error: Password must contain at least one number")
                else:
                    print("Password accepted!")
                    valid_password = True


# FINAL MESSAGE
print("Account successfully created!")
