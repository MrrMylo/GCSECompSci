students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92, 78, 90]

for i in range(len(students)):
    print(str(students[i]) + " scored " + str(scores[i]))

highest_score = scores[0]
highest_position = 0

for i in range(len(scores)):
    if scores[i] > highest_score:
        highest_score = scores[i]
        highest_position = i

print(students[highest_position] + " has the highest score of " + str(highest_score))
