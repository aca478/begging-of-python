import random

user_wins = 0
computer_wins = 0

options = ["kamen", "papir", "makaze"]

while True:
    user_input = input("Type kamen, papir or makaze or press q to quit. ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue 

    random_number = random.randint(0, 2)
    #rock:0 paper:1 scissors:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "kamen" and computer_pick == "makaze":
        print("You won!")
        user_wins += 1

    elif user_input == "papir" and computer_pick == "kamen":
        print("You won!")
        user_wins += 1

    elif user_input == "makaze" and computer_pick == "papir":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("The computer won!", computer_wins, "times.")
print("You won!", user_wins, "times.")
print("Goodbye!")