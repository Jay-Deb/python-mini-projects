# Rock Paper Scissor Game
# Play until user types 'quit'

import random

userwin = 0
computerwin = 0

choices = ["rock", "paper", "scissor"]

while True:
    userchoice = input("Enter your choice (rock, paper, scissor, quit): ")
    userchoice = userchoice.lower()

    if userchoice == "quit":
        print("---Game ended---")
        break

    if userchoice not in choices:
        print("Invalid input, try again!!")
        continue

    computerchoice = random.choice(choices)
    print("Computer chose:", computerchoice)

    if userchoice == computerchoice:
        print("Draw")

    elif userchoice == "rock" and computerchoice == "scissor":
        print("You win")
        userwin = userwin + 1

    elif userchoice == "paper" and computerchoice == "rock":
        print("You win")
        userwin = userwin + 1

    elif userchoice == "scissor" and computerchoice == "paper":
        print("You win")
        userwin = userwin + 1

    else:
        print("You lose")
        computerwin = computerwin + 1


print("Final Result:")
print("You won", userwin, "times")
print("Computer won", computerwin, "times")

if userwin > computerwin:
    print("You are winner")
elif computerwin > userwin:
    print("Computer is winner")
else:
    print("Match is draw") 