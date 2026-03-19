print("Welcome to the Rock, Paper, Scissors game.")
game = int(input("How many rounds would you like to play?: "))
for i in range(game):
    print("Player 2, Please look away while Player 1 makes their choice.")
    print()

    player1 = input("Player 1, please enter your choice (R (rock), P (paper), (S) scissors): ")
    if player1 == "R" or player1 == "r":
        player1 = "Rock"
    elif player1 == "P" or player1 == "p":
            player1 = "Paper"
    elif player1 == "S" or player1 == "s":
            player1 = "Scissors"
    print()
    print()
    

    for i in range(15):
        print()
    
    print("Player 1, Please look away while Player 2 makes their choice.")
    player2 = input("Player 2, please enter your choice R (rock), P (paper), (S) scissors): ")
    if player2 == "R" or player2 == "r":
        player2 = "Rock"
    elif player2 == "P" or player2 == "p":
        player2 = "Paper"
    elif player2 == "S" or player2 == "s":
        player2 = "Scissors"
    print()
    print()

    if player1 == player2:
        print("It's a draw!")
    elif player1 == "Rock" and player2 == "Scissors":
            print("Player 1 wins!")
    elif player1 == "Paper" and player2 == "Rock":
            print("Player 1 wins!")
    elif player1 == "Scissors" and player2 == "Paper":
            print("Player 1 wins!")
    elif player2 == "Rock" and player1 == "Scissors":
            print("Player 2 wins!")
    elif player2 == "Paper" and player1 == "Rock":
            print("Player 2 wins!")
    elif player2 == "Scissors" and player1 == "Paper":
            print("Player 2 wins!")
    
print("Thank you for playing!")

