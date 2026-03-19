import random

p1 = random.randint(2, 11)
p2 = random.randint(2, 11)

player_total = p1 + p2
player_aces = 0
if p1 == 11:
    player_aces = player_aces + 1
if p2 == 11:
    player_aces = player_aces + 1

while player_total > 21 and player_aces > 0:
    player_total = player_total - 10
    player_aces = player_aces - 1

p1_show = p1
p2_show = p2
if p1 == 11:
    p1_show = "Ace"
if p2 == 11:
    p2_show = "Ace"

if (p1 == 11 or p2 == 11) and (p1 + p2 <= 21):
    print("Player cards:", p1_show, p2_show, " Total:", player_total, "(soft)")
else:
    print("Player cards:", p1_show, p2_show, "| Total:", player_total)

# Player turn.
while player_total < 21:
    choice = input("Hit or Stand? (h/s): ").lower()

    if choice == "h":
        new_card = random.randint(2, 11)

        player_total = player_total + new_card
        if new_card == 11:
            player_aces = player_aces + 1

        while player_total > 21 and player_aces > 0:
            player_total = player_total - 10
            player_aces = player_aces - 1

        if new_card == 11:
            print("You drew Ace | New total:", player_total)
        else:
            print("You drew", new_card, "| New total:", player_total)

        if player_total > 21:
            print("You went over 21. Game over.")
            print("Final player total:", player_total)
            raise SystemExit

    elif choice == "s":
        break

    else:
        print("Type h for hit or s for stand.")

print("Final player total:", player_total)


d1 = random.randint(2, 11)
d2 = random.randint(2, 11)

dealer_total = d1 + d2
dealer_aces = 0
if d1 == 11:
    dealer_aces = dealer_aces + 1
if d2 == 11:
    dealer_aces = dealer_aces + 1

while dealer_total > 21 and dealer_aces > 0:
    dealer_total = dealer_total - 10
    dealer_aces = dealer_aces - 1

d1_show = d1
d2_show = d2
if d1 == 11:
    d1_show = "Ace"
if d2 == 11:
    d2_show = "Ace"

if (d1 == 11 or d2 == 11) and (d1 + d2 <= 21):
    print("Dealer cards:", d1_show, d2_show, "| Total:", dealer_total, "(soft)")
else:
    print("Dealer cards:", d1_show, d2_show, "| Total:", dealer_total)

# Dealer stands on 17.
while dealer_total < 17:
    new_card = random.randint(2, 11)

    dealer_total = dealer_total + new_card
    if new_card == 11:
        dealer_aces = dealer_aces + 1

    while dealer_total > 21 and dealer_aces > 0:
        dealer_total = dealer_total - 10
        dealer_aces = dealer_aces - 1

    if new_card == 11:
        print("Dealer drew Ace | Dealer total:", dealer_total)
    else:
        print("Dealer drew", new_card, "| Dealer total:", dealer_total)

print("Final dealer total:", dealer_total)

if dealer_total > 21:
    print("Dealer busts. You win!")
elif player_total > dealer_total:
    print("You win!")
elif player_total < dealer_total:
    print("Dealer wins.")
else:
    print("Push.")
