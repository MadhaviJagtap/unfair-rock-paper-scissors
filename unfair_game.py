import art as a

print(a.logo)

user = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
comp = []

if user == 0:
    print("\nYou chose Rock!\n", a.rock)
    comp = 0
elif user == 1:
    print("\nYou chose Paper!\n", a.paper)
    comp = 2
elif user == 2:
    print("\nYou chose Scissors!\n", a.scissors)
    comp = 1
else:
    print("Enter valid input")

print("Computer chose:")
if comp == 0:
    print("\nRock!\n", a.rock)
elif comp == 1:
    print("\nPaper!\n", a.paper)
elif comp == 2:
    print("\nScissors!\n", a.scissors)
else:
    print("Enter valid input")

# rock 0
# paper 1
# scissors 2

if user == "0" and comp == "2":
    print("You win!")
elif user == "2" and comp == "1":
    print("You win!")
elif user == "1" and comp == "0":
    print("You win!")
else:
    print("You lose!")
