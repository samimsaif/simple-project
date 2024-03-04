import random

Diceroll = True
while Diceroll:
    print(random.randint(1,6))
    Playagain = input("Do you want to roll again [y/n]")
    if Playagain == "y":
        continue
    else:
        print("Game Over")
        break