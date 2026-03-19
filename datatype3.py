vote = False

name = input("Please enter your name")
age = int(input("Please enter your age"))

if age >= 18:
   vote = True
else:
    vote = False
if vote == True:
   print(name + ", you are old enough to vote")
elif vote == False:
   print(name + ", you are not old enough to vote")
