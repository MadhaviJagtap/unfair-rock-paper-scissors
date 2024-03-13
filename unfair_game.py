import art as a

print(a.logo)

while True:
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

    if user not in [0, 1, 2]:
        print("You haven't entered a valid input. Thanks for playing!")
        break

    if user == 0:
        print("\nYou chose Rock!\n", a.rock)
        comp = 1
    elif user == 1:
        print("\nYou chose Paper!\n", a.paper)
        comp = 2
    elif user == 2:
        print("\nYou chose Scissors!\n", a.scissors)
        comp = 0

    print("Computer chose:")
    if comp == 0:
        print("\nRock!\n", a.rock)
    elif comp == 1:
        print("\nPaper!\n", a.paper)
    else:
        print("\nScissors!\n", a.scissors)

    if user != comp:
        print("You lose!")
        break
    else:
        print("You win!")
        break
