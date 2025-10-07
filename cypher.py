text = input("Input Text You would like to Cypher: ")

if not text.isupper():
    print("Please only use Capital Letters.")
else:
    shift = int(input("How much would you like to shift by?: "))
    result = ""

    for c in text:
        result = result + chr((ord(c) - 65 + shift) % 26 + 65)

    print(result)
