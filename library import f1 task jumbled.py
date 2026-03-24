import math
import random
import time

print("Formula 1 Start Lights Reaction Test!")
print("Press Enter as soon as the its lights out and away we go")

for i in range(5):
    print("Red Light " + str(i+1))
    time.sleep(0.5)

time.sleep(random.randint(2, 5))
print("Its lights out and away we go!")

start = time.time()
input()
end = time.time()
reaction = end - start

reaction = math.ceil(reaction*1000)
print("Your reaction time: " + str(reaction) + "ms")

