import art as a

print(a.logo)

user = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
comp = []

if user == 0:
    print("\nYou chose Rock!\n", a.rock)
    comp = 1
elif user == 1:
    print("\nYou chose Paper!\n", a.paper)
    comp = 2
elif user == 2:
    print("\nYou chose Scissors!\n", a.scissors)
    comp = 0
else:
    print("Enter valid input")

print("Computer chose:")
if comp == 0:
    print("\nRock!\n", a.rock)
elif comp == 1:
    print("\nPaper!\n", a.paper)
else
    print("\nScissors!\n", a.scissors)

# rock 0
# paper 1
# scissors 2

if user != comp:
    print("You lose!")
else:
    print("You win!")
