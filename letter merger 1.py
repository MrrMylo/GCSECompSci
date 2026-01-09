text = input("Enter a string of words: ")

words = text.split()


result = ""

for word in words:
    result = result+ word[0]
    
print(result)
 