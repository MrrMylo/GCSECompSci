mode = input("Encode, or Decode? (E/D): ").upper()
while mode not in ("E", "D"):
    print("Please type E, C")
    mode = input("Encode or Decode? (E/D): ").upper()
else:
    message = input("Enter message: ")

    if mode == "E":
        letter_shift = 2
        digit_shift = 2
    else:
        letter_shift = -2
        digit_shift = -2

    result = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                base = ord('A')
                result += chr((ord(c) - base + letter_shift) % 26 + base)
            else:
                base = ord('a')
                result += chr((ord(c) - base + letter_shift) % 26 + base)
        elif c.isdigit():
            base = ord('0')
            result += chr((ord(c) - base + digit_shift) % 10 + base)
        else:
            result += c

    print("Result:", result)