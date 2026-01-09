print("MERRY CHRISTMAS!")
rows = int(input("Enter number of rows you would like in your christmas tree: "))

print("Here is your Christmas tree:")

tree = 1
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * tree)
    tree += 2
for i in range(3):
    print(" " * (rows - 1) + "|")

print("Nice Tree!")