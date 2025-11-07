mode = input("Scramble or Unscramble? (S/U): ").upper()
while mode not in ("S", "U"):
    print("Please type S or U.")
    mode = input("Scramble or Unscramble? (S/U): ").upper()

if mode == "S":
    while True:
        word1 = input("Enter first 5-letter word: ")
        if word1.isalpha() and len(word1) == 5:
            break
        print("Please enter exactly 5 letters (letters only).")

    while True:
        word2 = input("Enter second 5-letter word: ")
        if word2.isalpha() and len(word2) == 5:
            break
        print("Please enter exactly 5 letters (letters only).")

    new1 = word2[4] + word1[1:4] + word2[0]
    new2 = word1[4] + word2[1:4] + word1[0]

    print("Result:", new2 + " " + new1)

else: 
    while True:
        s1 = input("Enter first scrambled word (the one printed first): ")
        if s1.isalpha() and len(s1) == 5:
            break
        print("Please enter exactly 5 letters (letters only).")

    while True:
        s2 = input("Enter second scrambled word (the one printed second): ")
        if s2.isalpha() and len(s2) == 5:
            break
        print("Please enter exactly 5 letters (letters only).")

    orig1 = s1[4] + s2[1:4] + s1[0]
    orig2 = s2[4] + s1[1:4] + s2[0]

    print("Original words:", orig1 + " " + orig2)